# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 22:18:45 2016

@author: showard
"""

try:
    from PyQt4 import QtGui
except ImportError:
    from PySide import QtGui
import pyaudio
import scimpy.speakertest as speakertest


class ImpTester(QtGui.QWidget):
    """Widget to control and analyze impedance measurements"""
    def __init__(self, parent):
        super(ImpTester, self).__init__(parent)
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
