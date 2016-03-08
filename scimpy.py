#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:20:04 2016

@author: showard
"""

import sys
try:
    from PyQt4 import QtGui, QtCore
except ImportError:
    from PySide import QtGui, QtCore
import pyaudio
import scimpy.speakertest as speakertest
import scimpy.speakermodel as speakermodel
import numpy as np
from math import sqrt


class ImpTester(QtGui.QWidget):
    """Widget to control and analyze impedance measurements"""
    def __init__(self):
        super(ImpTester, self).__init__()
        self.measurement_engine = speakertest.SpeakerTestEngine()
        self.init_ui()

    def init_ui(self):
        """Method to initialize UI and widget callbacks"""
        def update_input_textbox(current):
            """When input device selection changes, this function updates the
            displayed device information and sets the output device index"""
            new_row = inlistwidg.row(current)
            print(sc_info[new_row])
            in_infotext.setText("Name: {0}\n"
                                "Default Sampling Rate (Hz): {1}\n"
                                "Max Input Channels: {2}\n"
                                "Suggested Input Buffer (frames): {3}-{4}\n"
                                .format(sc_info[new_row]["name"],
                                        sc_info[new_row]["defaultSampleRate"],
                                        sc_info[new_row]["maxInputChannels"],
                                        int(sc_info[new_row]
                                            ["defaultLowInputLatency"] *
                                            sc_info[new_row]
                                            ["defaultSampleRate"]),
                                        int(sc_info[new_row]
                                            ["defaultHighInputLatency"] *
                                            sc_info[new_row]
                                            ["defaultSampleRate"])))
            test2lineedit.setText(str(sc_info[new_row]["defaultSampleRate"]))
            self.measurement_engine.set_input_device_ndx(new_row)

        def update_output_textbox(current):
            """When output device selection changes, this function updates the
            displayed device information and sets the output device index"""
            new_row = outlistwidg.row(current)
            print(sc_info[new_row])
            out_infotext.setText("Name: {0}\n"
                                 "Default Sampling Rate (Hz): {1}\n"
                                 "Max Output Channels: {2}\n"
                                 "Suggested Output Buffer (frames): {3}-{4}\n"
                                 .format(sc_info[new_row]["name"],
                                         sc_info[new_row]["defaultSampleRate"],
                                         sc_info[new_row]["maxOutputChannels"],
                                         int(sc_info[new_row]
                                             ["defaultLowOutputLatency"] *
                                             sc_info[new_row]
                                             ["defaultSampleRate"]),
                                         int(sc_info[new_row]
                                             ["defaultHighOutputLatency"] *
                                             sc_info[new_row]
                                             ["defaultSampleRate"])))
            test2lineedit.setText(str(sc_info[new_row]["defaultSampleRate"]))
            self.measurement_engine.set_output_device_ndx(new_row)

        def get_sc_info():
            """Returns a list of available devices on the default host api
            along with the information on the default input device"""
            pya = pyaudio.PyAudio()
            sc_info = [pya.get_device_info_by_index(n)
                       for n in range(pya.get_device_count())]
            default_device = pya.get_default_host_api_info()[
                "defaultInputDevice"]
            # TODO also return default output device, and use that info
            return [sc_info, default_device]

        def verify_sc_settings():
            """Tests whether current settings are supported and displays result
            in statusbar"""
            pya = pyaudio.PyAudio()
            try:
                supported = pya.is_format_supported(
                    rate=float(test2lineedit.text()),
                    input_device=inlistwidg.row(inlistwidg.currentItem()),
                    input_channels=2,
                    input_format=pya.get_format_from_width(
                        int(test4combobox.currentText())/8),
                    output_device=outlistwidg.row(outlistwidg.currentItem()),
                    output_channels=2,
                    output_format=pya.get_format_from_width(
                        int(test4combobox.currentText())/8))
                if supported:
                    statusbar.showMessage(
                        "These settings are supported!", 3000)
            except ValueError as err:
                statusbar.showMessage("ERROR: "+str(err), 3000)

        def run_measurement():
            """Performs measurement with user selected settings"""
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

        in_infotext = QtGui.QLabel()
        out_infotext = QtGui.QLabel()

        # TODO make each widget its own class,
        # with get/set functions to access data
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

        inputcardgroup = QtGui.QGroupBox("Input Device")
        # Input sound card list
        inlistwidg = QtGui.QListWidget()
        for k in sc_info:
            if k['maxInputChannels'] > 0:
                # Just show cards with inputs
                inlistwidg.addItem("%s" % k["name"])
            else:
                # Adding a hidden item for devices with
                # no inputs to maintain the index offset
                hiddenitem = QtGui.QListWidgetItem()
                hiddenitem.setText("%s" % k["name"])
                inlistwidg.addItem(hiddenitem)
                hiddenitem.setHidden(True)
        inlistwidg.currentItemChanged.connect(update_input_textbox)
        inlistwidg.setCurrentItem(inlistwidg.item(default_device))
        inputcardlayout = QtGui.QVBoxLayout()
        inputcardlayout.addWidget(inlistwidg)
        inputcardlayout.addWidget(in_infotext)
        inputcardgroup.setLayout(inputcardlayout)

        outputcardgroup = QtGui.QGroupBox("Output Device")
        # Output sound card list
        outlistwidg = QtGui.QListWidget()
        for k in sc_info:
            if k['maxOutputChannels'] > 0:
                # Just show cards with outputs
                outlistwidg.addItem("%s" % k["name"])
            else:
                # Adding a hidden item for devices with
                # no outputs to maintain the index offset
                hiddenitem = QtGui.QListWidgetItem()
                hiddenitem.setText("%s" % k["name"])
                outlistwidg.addItem(hiddenitem)
                hiddenitem.setHidden(True)
        outlistwidg.currentItemChanged.connect(update_output_textbox)
        outlistwidg.setCurrentItem(outlistwidg.item(default_device))
        outputcardlayout = QtGui.QVBoxLayout()
        outputcardlayout.addWidget(outlistwidg)
        outputcardlayout.addWidget(out_infotext)
        outputcardgroup.setLayout(outputcardlayout)

        layout.addWidget(inputcardgroup, 0, 0)
        layout.addWidget(outputcardgroup, 0, 1)
        layout.addWidget(btn, 1, 0)
        layout.addWidget(runbtn, 2, 0)
        layout.addWidget(formwidget, 0, 2, 3, 1)
        layout.addWidget(statusbar, 3, 0, 1, 4)

        self.setLayout(layout)

        self.setWindowTitle('Impedance Tester')
        self.center()

    def center(self):
        """Method to center widget on screen"""
        framegeo = self.frameGeometry()
        centerpoint = QtGui.QDesktopWidget().availableGeometry().center()
        framegeo.moveCenter(centerpoint)
        self.move(framegeo.topLeft())


# eventually just pass the whole widget as the argument below
# or we can keep an object somewhere that keeps all
# of these and pass that object to each widget
class SealedBoxWidget(QtGui.QGroupBox):
    """Widget for entering parameters for modeling sealed box enclosures"""
    def __init__(self,
                 title,
                 fslineedit,
                 qtslabel,
                 vasllineedit,
                 vasflineedit):
        def set_f3():
            """Updates f3 using available data"""
            qt_ = float(qtlabel.text())
            alpha = float(vasflineedit.text())/float(vbflineedit.text())
            f3_ = float(fslineedit.text()) * sqrt(alpha + 1) * \
                sqrt((1/qt_**2-2+sqrt((2-1/qt_**2)**2+4))/2)
            f3lineedit.setText("{0:.0f}".format(f3_))

        def reset_params():
            """Set all UI values to that of an infinite baffle"""
            self.vbllineedit.setText("inf")
            vbflineedit.setText("inf")
            f3lineedit.setText("")
            qt_ = float(qtslabel.text())
            qtlabel.setText("{0:0.2g}".format(qt_))
            set_f3()
            self.loveralineedit.setText("inf")

        def calc_ideal_params():
            """Calculate values for B2 closed box"""
            reset_params()
            alpha_inv = 2*float(qtslabel.text())**2 / \
                (1-2*float(qtslabel.text())**2)
            # f3 = float(fslineedit.text()) * sqrt(1/alpha_inv +1)
            vbflineedit.setText("{0:.2g}".format(
                float(vasflineedit.text())*alpha_inv))
            self.vbllineedit.setText(
                "{0:.2g}".format(float(vasllineedit.text())*alpha_inv))
            qtlabel.setText("{0:0.2g}".format(1/sqrt(2)))
            # f3lineedit.setText("{0:.0f}".format(f3))
            set_f3()

        def vbflineedit_callback():
            """When Vb in ft^3 changes, update Qt and f3"""
            alpha = float(vasflineedit.text())/float(vbflineedit.text())
            qt_ = float(qtslabel.text()) * sqrt(alpha+1)
            qtlabel.setText("{0:0.2g}".format(qt_))
            self.vbllineedit.setText(
                "{0:0.2g}".format(float(vbflineedit.text())*0.0283168*1000))
            set_f3()

        def vbllineedit_callback():
            """When Vb in litres changes, update Qt and f3"""
            alpha = float(vasllineedit.text())/float(self.vbllineedit.text())
            qt_ = float(qtslabel.text()) * sqrt(alpha+1)
            qtlabel.setText("{0:0.2g}".format(qt_))
            vbflineedit.setText(
                "{0:0.2g}".format(
                    float(self.vbllineedit.text())/0.0283168/1000))
            set_f3()

        # TODO - one class that all these layout widgets belong to, and this
        # class also holds all the lineedits and what nots as members so each
        # member subclass can access them? Or hold all those lineedits
        # in some other class and they are just assigned to layouts in widgets.

        # not including acoustic radiation effects on acoustic inductance
        # easy to include "radiation correction" later

        # possibly move this whole vented box part over to another widget
        def calc_ideal_ported_params():
            """Calculate Values for QB3-B4-C4 ported box"""
            reset_params()
            if float(qtslabel.text()) > 0.383:
                alpha, h__ = speakermodel.find_ported_params_C4(
                    float(qtslabel.text()))
            else:
                alpha, h__ = speakermodel.find_ported_params_QB3(
                    float(qtslabel.text()))
            vbflineedit.setText(
                "{0:0.2g}".format(float(vasflineedit.text())/alpha))
            self.vbllineedit.setText(
                "{0:0.2g}".format(float(vasllineedit.text())/alpha))
            print("fb Hz = ", float(fslineedit.text())*h__,
                  " h = ", h__,
                  " alpha = ", alpha)
            wbox = float(fslineedit.text())*h__*2*np.pi
            print(wbox, float(self.vbllineedit.text()))
            area_to_length_ratio = (wbox**2) * \
                (float(self.vbllineedit.text())/1000)/(345**2)
            print("A/l in m = ", area_to_length_ratio,
                  ' for 6" diameter, length inches = ',
                  (np.pi*(6*0.0254/2)**2/area_to_length_ratio)/0.0254)
            f3lineedit.setText("TBD")
            qtlabel.setText("TBD")
            self.loveralineedit.setText(
                "{0:3.0f}".format(1/area_to_length_ratio))

        super(SealedBoxWidget, self).__init__(title)
        layout = QtGui.QFormLayout()
        self.vbllineedit = QtGui.QLineEdit()
        self.vbllineedit.editingFinished.connect(vbllineedit_callback)
        layout.addRow("Box Volume (Vb) litres:", self.vbllineedit)
        vbflineedit = QtGui.QLineEdit()
        vbflineedit.editingFinished.connect(vbflineedit_callback)
        layout.addRow("Box Volume (Vb) ft^3:", vbflineedit)
        qtlabel = QtGui.QLabel()
        layout.addRow("Qt:", qtlabel)
        f3lineedit = QtGui.QLineEdit()
        layout.addRow("Cutoff Frequency (f3) Hz:", f3lineedit)
        self.loveralineedit = QtGui.QLineEdit()
        layout.addRow("Port/Vent Length over Area (av) m^-1:",
                      self.loveralineedit)

        resetbtn = QtGui.QPushButton("Set to Infinite Baffle")
        resetbtn.clicked.connect(reset_params)
        idealbtn = QtGui.QPushButton("Set to B2 Closed Box")
        idealbtn.clicked.connect(calc_ideal_params)
        idealportedbtn = QtGui.QPushButton("Set to QB3-B4-C4 Ported Box")
        idealportedbtn.clicked.connect(calc_ideal_ported_params)
        layout.addRow(resetbtn)
        layout.addRow(idealbtn)
        layout.addRow(idealportedbtn)
        reset_params()
        self.setLayout(layout)


class SpeakerModelWidget(QtGui.QWidget):
    """Widget for modeling speaker performance based on T/S values"""
    def __init__(self):
        super(SpeakerModelWidget, self).__init__()
        self.init_ui()

    def init_ui(self):
        """Method to initialize UI and widget callbacks"""
        def set_eta0(sd_, re_, mms, bl_):
            """Find and update set reference efficiency"""
            efficiency = sd_**2 * 1.18/345/2/np.pi/re_/(mms/bl_**2)**2/bl_**2
            eta0label.setText("{0:2.1f} %".format(efficiency*100))
            spllabel.setText(
                "{0:.0f} dB 1w1m".format(112.1+10*np.log10(efficiency)))

        # TODO these three methods all do the same thing
        def find_enclosure():
            """Calculates and displays closed box SPL, phase, and group
            delay"""
            speakermodel.calc_impedance(re_=float(relineedit.text()),
                                        le_=float(lelineedit.text())/1000,
                                        cms=float(cmslineedit.text())/1000,
                                        mms=float(mmslineedit.text())/1000,
                                        rms=float(rmslineedit.text()),
                                        sd_=float(sdlineedit.text())/(100*100),
                                        bl_=float(bllineedit.text()),
                                        vb_=float(
                                            sealedboxwidg.vbllineedit.text()
                                            )/1000)

#        def find_infinite_baffle_enclosure():
#            """Calculates and displays infinite baffle SPL, phase, and group
#            delay"""
#            speakermodel.calc_impedance(re=float(relineedit.text()),
#                                        le=float(lelineedit.text())/1000,
#                                        cms=float(cmslineedit.text())/1000,
#                                        mms=float(mmslineedit.text())/1000,
#                                        rms=float(rmslineedit.text()),
#                                        sd=float(sdlineedit.text())/(100*100),
#                                        bl=float(bllineedit.text()))

        def find_ported_enclosure():
            """Calculates and displays ported box SPL, phase, and group
            delay"""
            speakermodel.calc_impedance(re_=float(relineedit.text()),
                                        le_=float(lelineedit.text())/1000,
                                        cms=float(cmslineedit.text())/1000,
                                        mms=float(mmslineedit.text())/1000,
                                        rms=float(rmslineedit.text()),
                                        sd_=float(sdlineedit.text())/(100*100),
                                        bl_=float(bllineedit.text()),
                                        vb_=float(
                                            sealedboxwidg.vbllineedit.text()
                                            )/1000,
                                        l_over_a=float(
                                            sealedboxwidg.loveralineedit
                                            .text()))

        def calc_component_params():
            """Calculates physical measurements of components from system
            composite values (e.g., find mechanical resistance from Qes
            Qms and Re)"""
            try:
                re_ = float(relineedit.text())
                qes = float(qeslineedit.text())
                qms = float(qmslineedit.text())
                bl_ = float(bllineedit.text())
                sd_ = float(sdlineedit.text())/(100*100)
                fs_ = float(fslineedit.text())

                rms = bl_**2/(qms/qes*re_)
                rmslineedit.setText("{0:.2g}".format(rms))
                cms = (1/2/np.pi/fs_/qms/rms)*1000  # mm/N
                cmslineedit.setText("{0:.2g}".format(cms))
                mms = 1/(cms*(2*np.pi*fs_)**2)*1000  # grams
                mmslineedit.setText("{0:.2g}".format(mms*1000))

                cmslineedit_set()

                set_eta0(sd_, re_, mms, bl_)

                qtslabel.setText("{0:.2g}".format(qms*qes/(qms+qes)))
            except ValueError:
                pass  # might not be set yet

        def calc_system_params():
            """Calculates system composite characteristics from physical
            measurements of components (e.g., Qes from Cms Mms and Res)"""
            try:
                re_ = float(relineedit.text())
                cms = float(cmslineedit.text())/1000
                mms = float(mmslineedit.text())/1000
                rms = float(rmslineedit.text())
                sd_ = float(sdlineedit.text())/(100*100)
                bl_ = float(bllineedit.text())

                fs_ = 1/2/np.pi/sqrt(cms*mms)
                qes = 2*np.pi*fs_*mms*re_/bl_**2
                qms = 2*np.pi*fs_*mms/rms
                qts = qms*qes/(qms+qes)
                set_eta0(sd_, re_, mms, bl_)

                fslineedit.setText("{0:2.0f}".format(fs_))
                qeslineedit.setText("{0:1.2g}".format(qes))
                qmslineedit.setText("{0:1.2g}".format(qms))
                qtslabel.setText("{0:1.2g}".format(qts))
            except ValueError:
                pass  # might not be set yet

        def vasflineedit_callback():
            """On Vas in ft^3 change, find and update Cms (which then updates
            Vas in litres)"""
            sd_ = float(sdlineedit.text())/(100*100)
            vas = float(vasflineedit.text())*0.0283168
            cms = vas/(1.18*345**2*sd_**2)*1000
            cmslineedit.setText("{0:.2g}".format(cms))
            cmslineedit_callback()

        def vasllineedit_callback():
            """On Vas in litres change, find and update Cms (which then updates
            Vas in ft^3)"""
            sd_ = float(sdlineedit.text())/(100*100)
            vas = float(vasllineedit.text())/1000
            cms = vas/(1.18*345**2*sd_**2)*1000
            cmslineedit.setText("{0:.2g}".format(cms))
            cmslineedit_callback()

        def cmslineedit_set():
            """Find and update Vas in ft^3 and litres from Cms"""
            sd_ = float(sdlineedit.text())/(100*100)
            vas = (float(cmslineedit.text())/1000) * 1.18*345**2*sd_**2
            vasf = vas/0.0283168
            vasl = vas*1000  # litres
            vasflineedit.setText("{0:.2g}".format(vasf))
            vasllineedit.setText("{0:.2g}".format(vasl))

        def cmslineedit_callback():
            """On Cms change, find and update Vas in ft^3 and litres"""
            cmslineedit_set()
            calc_system_params()

        layout = QtGui.QGridLayout()

        formwidget = QtGui.QGroupBox("Component T/S Parameters")
        formwidgetlayout = QtGui.QFormLayout()
        relineedit = QtGui.QLineEdit("6")
        relineedit.editingFinished.connect(calc_system_params)
        formwidgetlayout.addRow("*DC Resistance (Re) Ohms:", relineedit)
        lelineedit = QtGui.QLineEdit("0.1")
        lelineedit.editingFinished.connect(calc_system_params)
        formwidgetlayout.addRow("*Voice Coil Inductance (Le) mH:", lelineedit)
        sdlineedit = QtGui.QLineEdit("25")
        sdlineedit.editingFinished.connect(calc_system_params)
        formwidgetlayout.addRow(
            "*Surface Area of Cone (Sd) cm^2:", sdlineedit)
        bllineedit = QtGui.QLineEdit("4.5")
        bllineedit.editingFinished.connect(calc_system_params)
        formwidgetlayout.addRow(
            "*Mag. Flux Density - Length (BL) Tm:", bllineedit)
        cmslineedit = QtGui.QLineEdit("0.16")
        cmslineedit.editingFinished.connect(cmslineedit_callback)
        formwidgetlayout.addRow(
            "Mechanical Compliance of Suspension (Cms) mm/N:", cmslineedit)
        vasllineedit = QtGui.QLineEdit("0.14")
        vasllineedit.editingFinished.connect(vasllineedit_callback)
        formwidgetlayout.addRow(
            "Driver Compliance Volume (Vas) litres:", vasllineedit)
        vasflineedit = QtGui.QLineEdit("0.005")
        vasflineedit.editingFinished.connect(vasflineedit_callback)
        formwidgetlayout.addRow(
            "Driver Compliance Volume (Vas) ft^3:", vasflineedit)
        mmslineedit = QtGui.QLineEdit("1.8")
        mmslineedit.editingFinished.connect(calc_system_params)
        formwidgetlayout.addRow(
            "Diaphragm Mass w/ Airload (Mms) g:", mmslineedit)
        rmslineedit = QtGui.QLineEdit("3.4")
        rmslineedit.editingFinished.connect(calc_system_params)
        formwidgetlayout.addRow(
            "Mechanical Resistance (Rms) Ns/m=Mech. ohm:", rmslineedit)

        formwidget.setLayout(formwidgetlayout)

        runbtn = QtGui.QPushButton(
            'Model Speaker Impedance and Infinite/Closed Baffle Performance')
        runbtn.clicked.connect(find_enclosure)  # can sepearate these two

        systemformwidget = QtGui.QGroupBox("Speaker T/S Parameters")
        systemformwidgetlayout = QtGui.QFormLayout()
        fslineedit = QtGui.QLineEdit("300")
        fslineedit.editingFinished.connect(calc_component_params)
        systemformwidgetlayout.addRow("Resonant Freq. (Fs) Hz:", fslineedit)
        qtslabel = QtGui.QLabel("0.5")
        systemformwidgetlayout.addRow("Qts:", qtslabel)
        qeslineedit = QtGui.QLineEdit("1")
        qeslineedit.editingFinished.connect(calc_component_params)
        systemformwidgetlayout.addRow("Qes:", qeslineedit)
        qmslineedit = QtGui.QLineEdit("1")
        qmslineedit.editingFinished.connect(calc_component_params)
        systemformwidgetlayout.addRow("Qms:", qmslineedit)
        eta0label = QtGui.QLabel("0.4 %")
        systemformwidgetlayout.addRow(
            "Reference Efficiency (eta0):", eta0label)
        spllabel = QtGui.QLabel("88 dB 1W1m")
        systemformwidgetlayout.addRow(
            "Sound Power Level (SPL):", spllabel)

        systemformwidget.setLayout(systemformwidgetlayout)

        sealedboxwidg = SealedBoxWidget("Enclosure Parameters",
                                        fslineedit,
                                        qtslabel,
                                        vasllineedit,
                                        vasflineedit)
        sealedboxbtn = QtGui.QPushButton("Calculate Sealed Box Performace")
        sealedboxbtn.clicked.connect(find_ported_enclosure)

        layout.addWidget(runbtn, 1, 0, 1, 2)
        layout.addWidget(formwidget, 0, 0, 1, 1)
        layout.addWidget(systemformwidget, 0, 1, 1, 1)
        layout.addWidget(sealedboxwidg, 0, 2, 1, 1)
        layout.addWidget(sealedboxbtn, 1, 2, 1, 1)
        self.setLayout(layout)

        self.setWindowTitle('Speaker Performance')
        self.center()

    def center(self):
        """Method to center widget on screen"""
        framegeo = self.frameGeometry()
        centerpoint = QtGui.QDesktopWidget().availableGeometry().center()
        framegeo.moveCenter(centerpoint)
        self.move(framegeo.topLeft())


#class SpeakerModelMainWindow(QtGui.QMainWindow):
#    """Main application widget"""
#    def __init__(self):
#        super(SpeakerModelMainWindow, self).__init__()
#        placeholder = QtGui.QWidget()
#        self.setCentralWidget(placeholder)
#        imptestdock = QtGui.QDockWidget("testing")
#        imptest = ImpTester()
#        imptestdock.setWidget(imptest)
#        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, imptestdock)
#        imptestdock.setFeatures(QtGui.QDockWidget.DockWidgetMovable)
#        imptestdock.setFeatures(QtGui.QDockWidget.DockWidgetFloatable)


def main():
    """Starts Scimpy Speaker Design Suite"""
    app = QtGui.QApplication(sys.argv)
    imptesterwidg = ImpTester()
    speakermodelwidg = SpeakerModelWidget()
    imptesterwidg.show()
    speakermodelwidg.show()
    # mainwindow = SpeakerModelMainWindow()
    # mainwindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
