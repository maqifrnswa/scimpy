#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:20:04 2016

@author: showard
"""

import sys
# from PySide import QtGui, QtCore
from PyQt4 import QtGui
import pyaudio
import speakertest
import speakermodel


class ImpTester(QtGui.QWidget):
    def __init__(self):
        super(ImpTester, self).__init__()
        self.measurement_engine = speakertest.SpeakerTestEngine()
        self.init_ui()

    def init_ui(self):
        def update_textbox(current, previous):
            new_row = listwidg.row(current)
            print(sc_info[new_row])
            infotext.setText("Name: {0}\n"
                             "Default Sampling Rate (Hz): {1}\n"
                             "Max Input Channels: {2}\n"
                             "Max Output Channels: {3}\n"
                             "Suggested Output Buffer (frames): {4}-{5}\n"
                             .format(sc_info[new_row]["name"],
                                     sc_info[new_row]["defaultSampleRate"],
                                     sc_info[new_row]["maxInputChannels"],
                                     sc_info[new_row]["maxOutputChannels"],
                                     int(sc_info[new_row][
                                         "defaultLowOutputLatency"] *
                                         sc_info[new_row]["defaultSampleRate"]
                                        ),
                                     int(sc_info[new_row][
                                         "defaultHighOutputLatency"] *
                                         sc_info[new_row]["defaultSampleRate"])
                                    ))
            test2lineedit.setText(str(sc_info[new_row]["defaultSampleRate"]))

        def get_sc_info():
            pya = pyaudio.PyAudio()
            sc_info = [pya.get_device_info_by_index(n)
                       for n in range(pya.get_device_count())]
            default_device = pya.get_default_host_api_info()[
                "defaultInputDevice"]
            return [sc_info, default_device]

        def verify_sc_settings():
            pya = pyaudio.PyAudio()
            try:
                supported = pya.is_format_supported(
                    rate=float(test2lineedit.text()),
                    input_device=listwidg.row(listwidg.currentItem()),
                    input_channels=2,
                    input_format=pya.get_format_from_width(
                        int(test4combobox.currentText())/8),
                    output_device=listwidg.row(listwidg.currentItem()),
                    output_channels=2,
                    output_format=pya.get_format_from_width(
                        int(test4combobox.currentText())/8))
                if supported:
                    statusbar.showMessage(
                        "These settings are supported!", 3000)
            except ValueError as err:
                statusbar.showMessage("ERROR: "+str(err), 3000)

        def run_measurement():
            print(test2lineedit.text())
            self.measurement_engine.run(
                framesize=int(test3lineedit.text()),
                datarate=int(float(test2lineedit.text())),
                duration=float(test6lineedit.text()),
                width=int(test4combobox.currentText())/8)

        [sc_info, default_device] = get_sc_info()

        statusbar = QtGui.QStatusBar(self)

        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))

        # self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QtGui.QPushButton('Verify Soundcard Capabillities')
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.clicked.connect(verify_sc_settings)

        runbtn = QtGui.QPushButton('Begin Test')
        runbtn.clicked.connect(run_measurement)

        layout = QtGui.QGridLayout()

        infotext = QtGui.QLabel()
        #  TODO do I want group box here? is that the right thing to use?
        formwidget = QtGui.QGroupBox("Measurement Parameters")
        formwidgetlayout = QtGui.QFormLayout()
        test2lineedit = QtGui.QLineEdit()
        test3lineedit = QtGui.QLineEdit("1024")
        test4combobox = QtGui.QComboBox()
        test4combobox.addItem("8")
        test4combobox.addItem("16")
        test4combobox.addItem("32")
        test4combobox.setCurrentIndex(1)
        test5lineedit = QtGui.QLineEdit("10")
        test6lineedit = QtGui.QLineEdit("2")
        formwidgetlayout.addRow("Sampling Rate (kHz):", test2lineedit)
        formwidgetlayout.addRow("I/O Buffer Size (frames, 0=auto):",
                                test3lineedit)
        formwidgetlayout.addRow("Data width (bits):", test4combobox)
        formwidgetlayout.addRow("Display Freq Resolution (Hz):", test5lineedit)
        formwidgetlayout.addRow("Measurement Duration (s):", test6lineedit)
        formwidget.setLayout(formwidgetlayout)

        listwidg = QtGui.QListWidget()
        [listwidg.addItem("%s" % n["name"]) for n in sc_info]
        listwidg.currentItemChanged.connect(update_textbox)
        listwidg.setCurrentItem(listwidg.item(default_device))

        layout.addWidget(listwidg, 0, 0)
        layout.addWidget(btn, 1, 0)
        layout.addWidget(runbtn, 2, 0)
        layout.addWidget(infotext, 0, 1)
        layout.addWidget(formwidget, 0, 3, 3, 1)
        layout.addWidget(statusbar, 3, 0, 1, 2)

        self.setLayout(layout)

        self.setWindowTitle('Impedance Tester')
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class SpeakerModel(QtGui.QWidget):
    def __init__(self):
        super(SpeakerModel, self).__init__()
        self.init_ui()

    def init_ui(self):
        def find_enclosure():
            re = float(relineedit.text())
            le = float(lelineedit.text())/1000
            cms = float(cmslineedit.text())/1000
            mms = float(mmslineedit.text())/1000
            res = float(reslineedit.text())
            sd = float(sdlineedit.text())/(100*100)
            bl = float(bllineedit.text())
            speakermodel.calcImpedance(re, le, cms, mms, res, sd, bl)
            return 0

        def calc_params():
            systeminfotext.setText("")
            fs = float(fslineedit.text())
            qes = float(qeslineedit.text())
            qms = float(qmslineedit.text())
            qts = qes*qms/(qes+qms)
            re = float(relineedit.text())
            res = qms/qes*re

            #  Vas -> Cms code block
            try:
                vas = float(vasflineedit.text())*0.0283168  # m^3
            except ValueError:
                try:
                    vas = float(vasllineedit.text())/1000  # m^3
                except ValueError:
                    pass
            try:
                sd = float(sdlineedit.text())/100/100  # m^2
                cms = vas/(1.18*345**2*sd**2)*1000  # mm/N
                systeminfotext.setText(
                    systeminfotext.text() + "Cms: {0:.3g} mm/N\n".format(cms))
            except:
                pass

            systeminfotext.setText(
                systeminfotext.text() +
                "Qts: {0:.3g}\nRes: {1:.3g} Ohms\nScott do Rms here!\n"
                .format(qts, res))

        layout = QtGui.QGridLayout()

        formwidget = QtGui.QGroupBox("Component T/S Parameters")
        formwidgetlayout = QtGui.QFormLayout()
        relineedit = QtGui.QLineEdit("6")
        formwidgetlayout.addRow("DC Resistance (Re) Ohms:", relineedit)
        lelineedit = QtGui.QLineEdit(".1")
        formwidgetlayout.addRow("Voice Coil Inductance (Le) mH:", lelineedit)
        cmslineedit = QtGui.QLineEdit(".1")
        formwidgetlayout.addRow(
            "Mechanical Compliance of Suspension (Cms) mm/N:", cmslineedit)
        mmslineedit = QtGui.QLineEdit("1.7")
        formwidgetlayout.addRow(
            "Diaphragm Mass w/ Airload (Mms) g:", mmslineedit)
        reslineedit = QtGui.QLineEdit("15")
        formwidgetlayout.addRow(
            "Mech. Equiv. Elec. Resistance (Res) Ohms:", reslineedit)
        sdlineedit = QtGui.QLineEdit("25")
        formwidgetlayout.addRow(
            "Surface Area of Cone (Sd) cm^2:", sdlineedit)
        bllineedit = QtGui.QLineEdit("4.5")
        formwidgetlayout.addRow(
            "Mag. Flux Density - Length (BL) Tm:", bllineedit)

        formwidget.setLayout(formwidgetlayout)

        runbtn = QtGui.QPushButton(
            'Model Speaker Impedance and Infinite Baffle Performance')
        runbtn.clicked.connect(find_enclosure)

        systemformwidget = QtGui.QGroupBox("System T/S Parameters")
        systemformwidgetlayout = QtGui.QFormLayout()
        fslineedit = QtGui.QLineEdit("300")
        systemformwidgetlayout.addRow("Resonant Freq. (Fs) Hz:", fslineedit)
        qeslineedit = QtGui.QLineEdit("1")
        systemformwidgetlayout.addRow("Qes:", qeslineedit)
        qmslineedit = QtGui.QLineEdit("1")
        systemformwidgetlayout.addRow("Qms:", qmslineedit)
        vasllineedit = QtGui.QLineEdit("2")
        systemformwidgetlayout.addRow(
            "Driver compliance Volume (Vas) litres:", vasllineedit)
        vasflineedit = QtGui.QLineEdit(".07")
        systemformwidgetlayout.addRow(
            "Driver compliance Volume (Vas) ft^3:", vasflineedit)

        systemformwidget.setLayout(systemformwidgetlayout)
        systeminfotext = QtGui.QLabel("testing")

        systembtn = QtGui.QPushButton('Calculate Component Parameters')
        systembtn.clicked.connect(calc_params)

        layout.addWidget(formwidget, 0, 0, 2, 1)
        layout.addWidget(runbtn, 2, 0, 1, 1)
        layout.addWidget(systemformwidget, 0, 1, 1, 1)
        layout.addWidget(systeminfotext, 1, 1, 1, 1)
        layout.addWidget(systembtn, 2, 1, 1, 1)
        self.setLayout(layout)

        self.setWindowTitle('Speaker Performance')
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def main():
    app = QtGui.QApplication(sys.argv)
    imp_tester = ImpTester()
    speaker_model = SpeakerModel()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
