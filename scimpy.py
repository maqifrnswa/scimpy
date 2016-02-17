#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:20:04 2016

@author: showard
"""

import sys
#from PySide import QtGui, QtCore
from PyQt4 import QtGui, QtCore
import pyaudio
import speakertest


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.measurementEngine = speakertest.SpeakerTestEngine()
        self.initUI()

    def initUI(self):
        def update_textbox(current,previous):
            new_row=listwidg.row(current)
            print(sc_info[new_row])
            infotext.setText("Name: {0}\n\
Default Sampling Rate (Hz): {1}\n\
Max Input Channels: {2}\n\
Max Output Channels: {3}\n\
Suggested Ourput Buffer (frames): {4}-{5}\n".format(sc_info[new_row]["name"],
                                   sc_info[new_row]["defaultSampleRate"],
                                   sc_info[new_row]["maxInputChannels"],
                                   sc_info[new_row]["maxOutputChannels"],
int(sc_info[new_row]["defaultLowOutputLatency"]*sc_info[new_row]["defaultSampleRate"]),
int(sc_info[new_row]["defaultHighOutputLatency"]*sc_info[new_row]["defaultSampleRate"])))
            test2LineEdit.setText(str(sc_info[new_row]["defaultSampleRate"]))
            #test3LineEdit.setText(str(int(sc_info[new_row]["defaultHighInputLatency"]*sc_info[new_row]["defaultSampleRate"])))
        
        def get_sc_info():
            pya=pyaudio.PyAudio()
            sc_info = [ pya.get_device_info_by_index(n) for n in range(pya.get_device_count()) ]
            default_device=pya.get_default_host_api_info()["defaultInputDevice" ]      
            return [sc_info, default_device]
            
        def verify_sc_settings():
            pya=pyaudio.PyAudio()
            try:
                supported=pya.is_format_supported(rate=float(test2LineEdit.text()),
                                          input_device=listwidg.row(listwidg.currentItem()),
                                          input_channels=2,
                                          input_format=
                                              pya.get_format_from_width(int(test4ComboBox.currentText())/8),
                                          output_device=listwidg.row(listwidg.currentItem()),
                                          output_channels=2,
                                          output_format=
                                              pya.get_format_from_width(int(test4ComboBox.currentText())/8))
                if supported==True: statusbar.showMessage("These settings are supported!",3000)
            except ValueError as e:
                statusbar.showMessage("ERROR: "+str(e), 3000)
                
        def runMeasurement():
            print(test2LineEdit.text())
            self.measurementEngine.run(framesize=int(test3LineEdit.text()),
                                       datarate=int(float(test2LineEdit.text())),
                                       duration=float(test6LineEdit.text()),
                                       width=int(test4ComboBox.currentText())/8)
                
        
        [sc_info, default_device] = get_sc_info()
        
        statusbar = QtGui.QStatusBar(self)
        
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        
        #self.setToolTip('This is a <b>QWidget</b> widget')
        
        btn = QtGui.QPushButton('Verify Soundcard Capabillities')
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.clicked.connect(verify_sc_settings)
        
        runbtn = QtGui.QPushButton('Verify Soundcard Capabillities')
        runbtn.clicked.connect(runMeasurement)
        #QtCore.QObject.connect(btn,QtCore.SIGNAL("clicked()"),self.verift_sc_settings())
        #btn.resize(btn.sizeHint())  
        
        layout=QtGui.QGridLayout()
        
        infotext=QtGui.QLabel()
        
        formwidget=QtGui.QGroupBox("Measurement Parameters")
        formwidgetlayout=QtGui.QFormLayout()
        test2LineEdit=QtGui.QLineEdit()
        test3LineEdit=QtGui.QLineEdit("1024")
        test4ComboBox=QtGui.QComboBox()
        test4ComboBox.addItem("8")
        test4ComboBox.addItem("16")
        test4ComboBox.addItem("32")
        test4ComboBox.setCurrentIndex(1)
        test5LineEdit=QtGui.QLineEdit("10")
        test6LineEdit=QtGui.QLineEdit("2")
        formwidgetlayout.addRow("Sampling Rate (kHz):",test2LineEdit)
        formwidgetlayout.addRow("I/O Buffer Size (frames, 0=auto):",test3LineEdit)
        formwidgetlayout.addRow("Data width (bits):",test4ComboBox)
        formwidgetlayout.addRow("Display Freq Resolution (Hz):",test5LineEdit)
        formwidgetlayout.addRow("Measurement Duration (s):",test6LineEdit)
        formwidget.setLayout(formwidgetlayout)
        
        listwidg=QtGui.QListWidget()
        [ listwidg.addItem("%s" % n["name"]) for n in sc_info ]
        listwidg.currentItemChanged.connect(update_textbox)
        # QtCore.QObject.connect(listwidg,QtCore.SIGNAL("currentItemChanged()"),update_textbox())
        listwidg.setCurrentItem(listwidg.item(default_device))
        
        layout.addWidget(listwidg,0,0)
        layout.addWidget(btn,1,0)
        layout.addWidget(runbtn,2,0)
        layout.addWidget(infotext,0,1)
        layout.addWidget(formwidget,0,3,3,1)
        layout.addWidget(statusbar,3,0,1,2)
        
        self.setLayout(layout)
        
        self.setWindowTitle('Impedance Tester')
        self.center()
        self.show()
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()