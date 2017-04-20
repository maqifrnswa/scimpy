# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 22:23:03 2016

@author: showard
"""
import logging
import os
import json
import scimpy.speakermodel as speakermodel
import numpy as np
from PyQt5 import QtWidgets, QtCore


logger = logging.getLogger(__name__)


# eventually just pass the whole widget as the argument below
# or we can keep an object somewhere that keeps all
# of these and pass that object to each widget
class SealedBoxWidget(QtWidgets.QGroupBox):
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
            f3_ = float(fslineedit.text()) * np.sqrt(alpha + 1) * \
                np.sqrt((1/qt_**2-2+np.sqrt((2-1/qt_**2)**2+4))/2)
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
            # f3 = float(fslineedit.text()) * np.sqrt(1/alpha_inv +1)
            vbflineedit.setText("{0:.2g}".format(
                float(vasflineedit.text())*alpha_inv))
            self.vbllineedit.setText(
                "{0:.2g}".format(float(vasllineedit.text())*alpha_inv))
            qtlabel.setText("{0:0.2g}".format(1/np.sqrt(2)))
            # f3lineedit.setText("{0:.0f}".format(f3))
            set_f3()

        def vbflineedit_callback():
            """When Vb in ft^3 changes, update Qt and f3"""
            alpha = float(vasflineedit.text())/float(vbflineedit.text())
            qt_ = float(qtslabel.text()) * np.sqrt(alpha+1)
            qtlabel.setText("{0:0.2g}".format(qt_))
            self.vbllineedit.setText(
                "{0:0.2g}".format(float(vbflineedit.text())*0.0283168*1000))
            set_f3()

        def vbllineedit_callback():
            """When Vb in litres changes, update Qt and f3"""
            alpha = float(vasllineedit.text())/float(self.vbllineedit.text())
            qt_ = float(qtslabel.text()) * np.sqrt(alpha+1)
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
                alpha, h__ = speakermodel.find_ported_params_c4(
                    float(qtslabel.text()))
            else:
                alpha, h__ = speakermodel.find_ported_params_qb3(
                    float(qtslabel.text()))
            vbflineedit.setText(
                "{0:0.2g}".format(float(vasflineedit.text())/alpha))
            self.vbllineedit.setText(
                "{0:0.2g}".format(float(vasllineedit.text())/alpha))
            logger.info("fb Hz = %f, h = %f, alpha = %f" %
                        (float(fslineedit.text())*h__, h__, alpha))

            wbox = float(fslineedit.text())*h__*2*np.pi
            area_to_length_ratio = (wbox**2) * \
                (float(self.vbllineedit.text())/1000)/(345**2)
            logger.info('A/l in m = %f, for 2" diameter, length inches = %f' %
                        (area_to_length_ratio,
                         (np.pi*(2*0.0254/2)**2/area_to_length_ratio)/0.0254))
            f3lineedit.setText("TBD, not implimented")
            qtlabel.setText("TBD")
            self.loveralineedit.setText(
                "{0:.3g}".format(1/area_to_length_ratio/100))

        super(SealedBoxWidget, self).__init__(title)
        layout = QtWidgets.QFormLayout()
        self.vbllineedit = QtWidgets.QLineEdit()
        self.vbllineedit.editingFinished.connect(vbllineedit_callback)
        self.vbllineedit.setToolTip("Box Volume")
        layout.addRow("Vb (litres):", self.vbllineedit)
        vbflineedit = QtWidgets.QLineEdit()
        vbflineedit.editingFinished.connect(vbflineedit_callback)
        vbflineedit.setToolTip("Box Volume")
        layout.addRow("Vb (ft^3):", vbflineedit)
        qtlabel = QtWidgets.QLabel()
        layout.addRow("Qt:", qtlabel)
        f3lineedit = QtWidgets.QLabel()  # changed to QLabel from QLineEdit
        f3lineedit.setToolTip("3 dB Cutoff Frequency")
        layout.addRow("f3 (Hz):", f3lineedit)
        self.loveralineedit = QtWidgets.QLineEdit()
        self.loveralineedit.setToolTip("Port/Vent Length to Area Ratio")
        layout.addRow("L/A (cm^-1):", self.loveralineedit)

        resetbtn = QtWidgets.QPushButton("Set to Infinite Baffle")
        resetbtn.clicked.connect(reset_params)
        idealbtn = QtWidgets.QPushButton("Set to B2 Closed Box")
        idealbtn.clicked.connect(calc_ideal_params)
        idealportedbtn = QtWidgets.QPushButton("Set to QB3-B4-C4 Ported Box")
        idealportedbtn.clicked.connect(calc_ideal_ported_params)
        layout.addRow(resetbtn)
        layout.addRow(idealbtn)
        layout.addRow(idealportedbtn)
        reset_params()
        self.setLayout(layout)


def find_main_window():
    for widget in QtWidgets.QApplication.topLevelWidgets():
        if isinstance(widget, QtWidgets.QMainWindow):
            return widget


class SpeakerModelWidget(QtWidgets.QWidget):
    """Widget for modeling speaker performance based on T/S values"""
    def __init__(self):
        super(SpeakerModelWidget, self).__init__()
        self.driver_params = {}  # TODO save values in this dict! just pass this!
        # TDOD use driver_params rather than constantly getting text values
        self.init_ui()

    def calc_system_params(self):
        """Calculates system composite characteristics from physical
        measurements of components (e.g., Qes from Cms Mms and Res)"""
        try:
            re_ = float(self.relineedit.text())
            cms = float(self.cmslineedit.text())/1000
            mms = float(self.mmslineedit.text())/1000
            rms = float(self.rmslineedit.text())
            sd_ = float(self.sdlineedit.text())/(100*100)
            bl_ = float(self.bllineedit.text())

            fs_ = 1/2/np.pi/np.sqrt(cms*mms)
            qes = 2*np.pi*fs_*mms*re_/bl_**2
            qms = 2*np.pi*fs_*mms/rms
            qts = qms*qes/(qms+qes)
            self.set_eta0(sd_, re_, mms, bl_)

            self.fslineedit.setText("{0:2.0f}".format(fs_))
            self.qeslineedit.setText("{0:1.2g}".format(qes))
            self.qmslineedit.setText("{0:1.2g}".format(qms))
            self.qtslabel.setText("{0:1.2g}".format(qts))
        except ValueError:
            pass  # might not be set yet

    def calc_component_params(self):
        """Calculates physical measurements of components from system
        composite values (e.g., find mechanical resistance from Qes
        Qms and Re)"""
        try:
            re_ = float(self.relineedit.text())
            qes = float(self.qeslineedit.text())
            qms = float(self.qmslineedit.text())
            bl_ = float(self.bllineedit.text())
            sd_ = float(self.sdlineedit.text())/(100*100)
            fs_ = float(self.fslineedit.text())

            rms = bl_**2/(qms/qes*re_)
            self.rmslineedit.setText("{0:.2g}".format(rms))
            cms = (1/2/np.pi/fs_/qms/rms)*1000  # mm/N
            self.cmslineedit.setText("{0:.2g}".format(cms))
            mms = 1/(cms*(2*np.pi*fs_)**2)*1000  # grams
            self.mmslineedit.setText("{0:.2g}".format(mms*1000))

            self.cmslineedit_set()

            self.set_eta0(sd_, re_, mms, bl_)

            self.qtslabel.setText("{0:.2g}".format(qms*qes/(qms+qes)))
        except ValueError:
            pass  # might not be set yet

    def set_eta0(self, sd_, re_, mms, bl_):
        """Find and update set reference efficiency"""
        efficiency = sd_**2 * 1.18/345/2/np.pi/re_/(mms/bl_**2)**2/bl_**2
        self.eta0label.setText("{0:2.1f} %".format(efficiency*100))
        self.spllabel.setText(
            "{0:.0f} dB 1w1m".format(112.1+10*np.log10(efficiency)))

    def cmslineedit_set(self):
        """Find and update Vas in ft^3 and litres from Cms"""
        sd_ = float(self.sdlineedit.text())/(100*100)
        vas = (float(self.cmslineedit.text())/1000) * 1.18*345**2*sd_**2
        vasf = vas/0.0283168
        vasl = vas*1000  # litres
        self.vasflineedit.setText("{0:.2g}".format(vasf))
        self.vasllineedit.setText("{0:.2g}".format(vasl))

    def init_ui(self):
        """Method to initialize UI and widget callbacks"""
        def update_driver_dict():
            self.driver_params["re"] = float(relineedit.text())
            self.driver_params["le"] = float(lelineedit.text())/1000
            self.driver_params["cms"] = float(cmslineedit.text())/1000
            self.driver_params["mms"] = float(mmslineedit.text())/1000
            self.driver_params["rms"] = float(rmslineedit.text())
            self.driver_params["sd"] = float(sdlineedit.text())/(100*100)
            self.driver_params["bl"] = float(bllineedit.text())
            self.driver_params["n"] = float(nlineedit.text())

        def update_driver_fields():
            relineedit.setText(str(self.driver_params["re"]))
            lelineedit.setText(str(self.driver_params["le"]*1000.0))
            cmslineedit.setText(str(self.driver_params["cms"]*1000.0))
            mmslineedit.setText(str(self.driver_params["mms"]*1000.0))
            rmslineedit.setText(str(self.driver_params["rms"]))
            sdlineedit.setText(str(self.driver_params["sd"]*(100*100.0)))
            bllineedit.setText(str(self.driver_params["bl"]))
            nlineedit.setText(str(self.driver_params["n"]))
            self.cmslineedit_set()
            self.calc_system_params()

        def savedriver():
            update_driver_dict()
            basedirectory = QtCore.QStandardPaths.writableLocation(
                QtCore.QStandardPaths.DocumentsLocation)
            driverdir = basedirectory+"/Scimpy/drivers"
            if not os.path.isdir(driverdir):
                os.makedirs(driverdir)
            filters = "Driver Files (*.drv);;All Files (*.*)"
            filename = QtWidgets.QFileDialog.getSaveFileName(self,
                                                         "Save Driver Specs",
                                                         driverdir,
                                                         filters)[0]
            if os.path.splitext(filename)[-1] == "":
                filename = filename+".drv"
            with open(filename, 'w') as outfile:
                json.dump(self.driver_params, outfile)

        def loaddriver():
            basedirectory = QtCore.QStandardPaths.writableLocation(
                QtCore.QStandardPaths.DocumentsLocation)
            driverdir = basedirectory+"/Scimpy/drivers"
            if not os.path.isdir(driverdir):
                os.makedirs(driverdir)
            filters = "Driver Files (*.drv);;All Files (*.*)"
            filename = QtWidgets.QFileDialog.getOpenFileName(self,
                                                         "Load Driver Specs",
                                                         driverdir,
                                                         filters)[0]
            if filename != '':
                with open(filename, 'r') as infile:
                    self.driver_params = json.load(infile)
                update_driver_fields()

        def find_ported_enclosure():
            """Calculates and displays ported box SPL, phase, and group
            delay"""
            plotwidget = find_main_window().plotwidget.canvas
            speakermodel.calc_impedance(plotwidget=plotwidget,
                                        re_=float(relineedit.text()),
                                        le_=float(lelineedit.text())/1000,
                                        n_=float(nlineedit.text()),
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
                                            .text())*100)

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

        def cmslineedit_callback():
            """On Cms change, find and update Vas in ft^3 and litres"""
            self.cmslineedit_set()
            self.calc_system_params()

        formwidget = QtWidgets.QGroupBox("Component T/S Parameters")
        formwidgetlayout = QtWidgets.QFormLayout()
        relineedit = QtWidgets.QLineEdit("6")
        relineedit.editingFinished.connect(self.calc_system_params)
        relineedit.setToolTip("DC Resistance *Required*")
        formwidgetlayout.addRow("*Re (ohms):", relineedit)
        lelineedit = QtWidgets.QLineEdit("0.1")
        lelineedit.editingFinished.connect(self.calc_system_params)
        lelineedit.setToolTip("Leach K, if n=1 Voice Coil Inductance *Required*")
        formwidgetlayout.addRow("*Le (mH) or K*1000:", lelineedit)
        nlineedit = QtWidgets.QLineEdit("1")
        nlineedit.editingFinished.connect(self.calc_system_params)
        nlineedit.setToolTip("Leach n parameter (if n=1, then K=Le) *Required*")
        formwidgetlayout.addRow("*n:", nlineedit)
        sdlineedit = QtWidgets.QLineEdit("25")
        sdlineedit.editingFinished.connect(self.calc_system_params)
        sdlineedit.setToolTip("Cone Surface Area *Required*")
        formwidgetlayout.addRow(
            "*Sd (cm^2):", sdlineedit)
        bllineedit = QtWidgets.QLineEdit("4.5")
        bllineedit.editingFinished.connect(self.calc_system_params)
        bllineedit.setToolTip("Mag. Flux Density x Length *Required*")
        formwidgetlayout.addRow("*BL (Tm):", bllineedit)
        cmslineedit = QtWidgets.QLineEdit("0.16")
        cmslineedit.editingFinished.connect(cmslineedit_callback)
        cmslineedit.setToolTip("Driver Compliance")
        formwidgetlayout.addRow("Cms (mm/N):", cmslineedit)
        vasllineedit = QtWidgets.QLineEdit("0.14")
        vasllineedit.editingFinished.connect(vasllineedit_callback)
        vasllineedit.setToolTip("Driver Compliance Volume")
        formwidgetlayout.addRow("Vas (litres):", vasllineedit)
        vasflineedit = QtWidgets.QLineEdit("0.005")
        vasflineedit.editingFinished.connect(vasflineedit_callback)
        vasflineedit.setToolTip("Driver Compliance Volume")
        formwidgetlayout.addRow("Vas (ft^3):", vasflineedit)
        mmslineedit = QtWidgets.QLineEdit("1.8")
        mmslineedit.editingFinished.connect(self.calc_system_params)
        mmslineedit.setToolTip("Diaphragm Mass w/ Airload")
        formwidgetlayout.addRow("Mms (g):", mmslineedit)
        rmslineedit = QtWidgets.QLineEdit("3.4")
        rmslineedit.editingFinished.connect(self.calc_system_params)
        rmslineedit.setToolTip("Mechanical Resistance (Mech. ohm=N s/m")
        formwidgetlayout.addRow("Rms (Mech. ohm):", rmslineedit)

        formwidget.setLayout(formwidgetlayout)

        systemformwidget = QtWidgets.QGroupBox("Speaker T/S Parameters")
        systemformwidgetlayout = QtWidgets.QFormLayout()
        fslineedit = QtWidgets.QLineEdit("300")
        fslineedit.editingFinished.connect(self.calc_component_params)
        fslineedit.setToolTip("Driver Suspension Resonant Frequency")
        systemformwidgetlayout.addRow("Fs (Hz):", fslineedit)
        qtslabel = QtWidgets.QLabel("0.5")
        systemformwidgetlayout.addRow("Qts:", qtslabel)
        qeslineedit = QtWidgets.QLineEdit("1")
        qeslineedit.editingFinished.connect(self.calc_component_params)
        systemformwidgetlayout.addRow("Qes:", qeslineedit)
        qmslineedit = QtWidgets.QLineEdit("1")
        qmslineedit.editingFinished.connect(self.calc_component_params)
        systemformwidgetlayout.addRow("Qms:", qmslineedit)
        eta0label = QtWidgets.QLabel("0.4 %")
        eta0label.setToolTip("Reference Efficiency")
        systemformwidgetlayout.addRow(
            "eta0:", eta0label)
        spllabel = QtWidgets.QLabel("88 dB 1W1m")
        spllabel.setToolTip("Sound Power Level")
        systemformwidgetlayout.addRow(
            "SPL:", spllabel)

        systemformwidget.setLayout(systemformwidgetlayout)

        sealedboxwidg = SealedBoxWidget("Enclosure Parameters",
                                        fslineedit,
                                        qtslabel,
                                        vasllineedit,
                                        vasflineedit)
        sealedboxbtn = QtWidgets.QPushButton("Calculate && Plot")
        sealedboxbtn.clicked.connect(find_ported_enclosure)

        driverfileopwidg = QtWidgets.QWidget()
        fileoplayout = QtWidgets.QHBoxLayout()
        savebtn = QtWidgets.QPushButton("Save Driver")
        savebtn.clicked.connect(savedriver)
        loadbtn = QtWidgets.QPushButton("Load Driver")
        loadbtn.clicked.connect(loaddriver)
        fileoplayout.addWidget(savebtn)
        fileoplayout.addWidget(loadbtn)
        driverfileopwidg.setLayout(fileoplayout)

        # TODO below is a hack, find a better way
        self.sdlineedit = sdlineedit
        self.relineedit = relineedit
        self.lelineedit = lelineedit
        self.nlineedit = nlineedit
        self.rmslineedit = rmslineedit
        self.cmslineedit = cmslineedit
        self.mmslineedit = mmslineedit
        self.bllineedit = bllineedit
        self.fslineedit = fslineedit
        self.qeslineedit = qeslineedit
        self.qmslineedit = qmslineedit
        self.qtslabel = qtslabel
        self.eta0label = eta0label
        self.spllabel = spllabel
        self.vasflineedit = vasflineedit
        self.vasllineedit = vasllineedit

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(driverfileopwidg)
        layout.addWidget(formwidget)  # , 0, 0, 1, 1)
        layout.addWidget(systemformwidget)  # , 0, 1, 1, 1)
        layout.addWidget(sealedboxwidg)  # , 0, 2, 1, 1)
        # layout.addWidget(sealedboxbtn, 1, 2, 1, 1)
        layout.addWidget(sealedboxbtn)  # , 1, 0, 1, 2)
        self.setLayout(layout)

        self.setWindowTitle('Speaker Performance')
