# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 10:18:29 2016

@author: rf2antennallc
"""
#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
import math as m
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtW

class MainWindow(QtW.QWidget):

    def __init__(self):
        
        inputStyle = "font-size: 20px; qproperty-alignment: AlignJustify; font-family: Times New Roman; background: white" 
        outputStyle = "font-style: bold; font-size: 20px; qproperty-alignment: AlignJustify; font-family: Times New Roman; background: yellow"
        
        QtW.QWidget.__init__(self)

        layout = QtW.QGridLayout()
        coilCommon = QtW.QGroupBox("Common Parameters")
        coilParameters = QtW.QGroupBox("Coil Parameters")
        coilMatchingComponents = QtW.QGroupBox("Matching Components")
        coilEfficiency = QtW.QGroupBox("Coil Efficiency")
        
        ###########################
        
        coilCommonLayout = QtW.QFormLayout()
        
        self.e01 = QtW.QLineEdit()
        self.e01.setValidator(QtGui.QDoubleValidator(1e-6,1e50,16))
        self.e01.setStyleSheet(inputStyle)
        coilCommonLayout.addRow("Frequency (Hz)", self.e01)
        
        coilCommon.setLayout(coilCommonLayout)
        
        ##############################################
        
        coilParametersLayout = QtW.QFormLayout()

        self.e11 = QtW.QLineEdit()
        self.e11.setValidator(QtGui.QDoubleValidator(1e-6,1e6,16))
        self.e11.setStyleSheet(inputStyle)
        coilParametersLayout.addRow("Coil Diameter (m)", self.e11)
        
        self.e12 = QtW.QLineEdit()
        self.e12.setValidator(QtGui.QDoubleValidator(1e-20,1e6,16))
        self.e12.setStyleSheet(inputStyle)
        coilParametersLayout.addRow("Wire Diameter (m)", self.e12)
        
        self.e15 = QtW.QLineEdit()
        self.e15.setValidator(QtGui.QDoubleValidator(1e-20,1e30,16))
        self.e15.setStyleSheet(inputStyle)
        coilParametersLayout.addRow("Wire Conductivity (S/m)", self.e15)
        
        self.e13 = QtW.QLineEdit()
        self.e13.setValidator(QtGui.QDoubleValidator(1,1e20,16))
        self.e13.setStyleSheet(inputStyle)
        coilParametersLayout.addRow("Winding Number of Turns", self.e13)
        
        self.e14 = QtW.QLineEdit()
        self.e14.setValidator(QtGui.QDoubleValidator(1e-20,1e6,16))
        self.e14.setStyleSheet(inputStyle)
        coilParametersLayout.addRow("Winding Height (m)", self.e14)

        self.o11 = QtW.QLineEdit("...")
        self.o11.setReadOnly(True)
        self.o11.setStyleSheet(outputStyle)
        coilParametersLayout.addRow("Wire Cross Section Area (m^2)",self.o11)

        self.o12 = QtW.QLineEdit("...")
        self.o12.setReadOnly(True)
        self.o12.setStyleSheet(outputStyle)
        coilParametersLayout.addRow("Wire Length (m)",self.o12)

        self.o13 = QtW.QLineEdit("...")
        self.o13.setReadOnly(True)
        self.o13.setStyleSheet(outputStyle)
        coilParametersLayout.addRow("Winding Thickness (m)",self.o13)

        self.o14 = QtW.QLineEdit("...")
        self.o14.setReadOnly(True)
        self.o14.setStyleSheet(outputStyle)
        coilParametersLayout.addRow("Winding AC Resistance (Ohm)",self.o14)

        self.o15 = QtW.QLineEdit("...")
        self.o15.setReadOnly(True)
        self.o15.setStyleSheet(outputStyle)
        coilParametersLayout.addRow("Winding Effective Builk Conductivity (S/m)",self.o15)
        
        self.b11 = QtW.QPushButton("Calculate")
        self.b11.clicked.connect(self.calcCoilParam)
        coilParametersLayout.addRow(self.b11)
        
        coilParameters.setLayout(coilParametersLayout)
        
        #####################################################
        
        coilMatchingComponentsLayout = QtW.QFormLayout()

        self.e21 = QtW.QLineEdit()
        self.e21.setValidator(QtGui.QDoubleValidator(1e-20,1e20,16))
        self.e21.setStyleSheet(inputStyle)
        coilMatchingComponentsLayout.addRow("Source Resistance RS (Ohm)", self.e21)
        
        self.e22 = QtW.QLineEdit()
        self.e22.setValidator(QtGui.QDoubleValidator(1e-20,1e20,16))
        self.e22.setStyleSheet(inputStyle)
        coilMatchingComponentsLayout.addRow("Load Resistance RL (Ohm)", self.e22)
        
        self.e23 = QtW.QLineEdit()
        self.e22.setValidator(QtGui.QDoubleValidator(1e-20,1e20,16))
        self.e23.setStyleSheet(inputStyle)
        coilMatchingComponentsLayout.addRow("Tx Resistance R1 (Ohm)", self.e23)
        
        self.e24 = QtW.QLineEdit()
        self.e22.setValidator(QtGui.QDoubleValidator(1e-20,1e20,16))
        self.e24.setStyleSheet(inputStyle)
        coilMatchingComponentsLayout.addRow("Tx Inductance L1 (H)", self.e24)
        
        self.e25 = QtW.QLineEdit()
        self.e22.setValidator(QtGui.QDoubleValidator(1e-20,1e20,16))
        self.e25.setStyleSheet(inputStyle)
        coilMatchingComponentsLayout.addRow("Rx Resistance R2 (Ohm)", self.e25)
        
        self.e26 = QtW.QLineEdit()
        self.e22.setValidator(QtGui.QDoubleValidator(1e-20,1e20,16))
        self.e26.setStyleSheet(inputStyle)
        coilMatchingComponentsLayout.addRow("Rx Inductance L2 (H)", self.e26)
        
        self.e27 = QtW.QLineEdit()
        self.e22.setValidator(QtGui.QDoubleValidator(1e-20,1e20,16))
        self.e27.setStyleSheet(inputStyle)
        coilMatchingComponentsLayout.addRow("Mutual Resistance R12 (Ohm)", self.e27)
        
        self.e28 = QtW.QLineEdit()
        self.e22.setValidator(QtGui.QDoubleValidator(1e-20,1e20,16))
        self.e28.setStyleSheet(inputStyle)
        coilMatchingComponentsLayout.addRow("Coupling Factor K", self.e28)
        
        
        self.o21 = QtW.QLineEdit("...")
        self.o21.setReadOnly(True)
        self.o21.setStyleSheet(outputStyle)
        coilMatchingComponentsLayout.addRow("Tx Q Factor",self.o21)
        
        self.o22 = QtW.QLineEdit("...")
        self.o22.setReadOnly(True)
        self.o22.setStyleSheet(outputStyle)
        coilMatchingComponentsLayout.addRow("Rx Q Factor",self.o22)
        
        self.o23 = QtW.QLineEdit("...")
        self.o23.setReadOnly(True)
        self.o23.setStyleSheet(outputStyle)
        coilMatchingComponentsLayout.addRow("Source Shunt Inductance LS (H)",self.o23)
        
        self.o24 = QtW.QLineEdit("...")
        self.o24.setReadOnly(True)
        self.o24.setStyleSheet(outputStyle)
        coilMatchingComponentsLayout.addRow("Source Series Capacitance CS (F)",self.o24)
        
        self.o25 = QtW.QLineEdit("...")
        self.o25.setReadOnly(True)
        self.o25.setStyleSheet(outputStyle)
        coilMatchingComponentsLayout.addRow("Load Shunt Inductance LL (H)",self.o25)
        
        self.o26 = QtW.QLineEdit("...")
        self.o26.setReadOnly(True)
        self.o26.setStyleSheet(outputStyle)
        coilMatchingComponentsLayout.addRow("Load Series Capacitance CL (F)",self.o26)
        
        self.o27 = QtW.QLineEdit("...")
        self.o27.setReadOnly(True)
        self.o27.setStyleSheet(outputStyle)
        coilMatchingComponentsLayout.addRow("Mutual Inductance L12 (H)",self.o27)
        
        
        self.b21 = QtW.QPushButton("Calculate")
        self.b21.clicked.connect(self.calcCoilMatching)
        coilMatchingComponentsLayout.addRow(self.b21)
        
        coilMatchingComponents.setLayout(coilMatchingComponentsLayout)        
        
        ###########################################################
        coilEfficiencyLayout = QtW.QFormLayout()

        self.e31 = QtW.QLineEdit()
        self.e31.setValidator(QtGui.QDoubleValidator(1e-20,1e20,16))
        self.e31.setStyleSheet(inputStyle)
        coilEfficiencyLayout.addRow("Input Voltage (V)", self.e31)
        
        self.e32 = QtW.QLineEdit()
        self.e32.setValidator(QtGui.QDoubleValidator(1e-20,1e20,16))
        self.e32.setStyleSheet(inputStyle)
        coilEfficiencyLayout.addRow("Source Shunt Inductance LS (H)", self.e32)
        
        self.e33 = QtW.QLineEdit()
        self.e33.setValidator(QtGui.QDoubleValidator(1e-20,1e20,16))
        self.e33.setStyleSheet(inputStyle)
        coilEfficiencyLayout.addRow("Source Series Capacitance CS (F)", self.e33)
        
        self.e34 = QtW.QLineEdit()
        self.e34.setValidator(QtGui.QDoubleValidator(1e-20,1e20,16))
        self.e34.setStyleSheet(inputStyle)
        coilEfficiencyLayout.addRow("Load Shunt Inductance LL (H)", self.e34)
        
        self.e35 = QtW.QLineEdit()
        self.e35.setValidator(QtGui.QDoubleValidator(1e-20,1e20,16))
        self.e35.setStyleSheet(inputStyle)
        coilEfficiencyLayout.addRow("Load Series Capacitance CL (F)", self.e35)
        
        
        self.o31 = QtW.QLineEdit("...")
        self.o31.setReadOnly(True)
        self.o31.setStyleSheet(outputStyle)
        coilEfficiencyLayout.addRow("Input Voltage (V)",self.o31)
        
        self.o32 = QtW.QLineEdit("...")
        self.o32.setReadOnly(True)
        self.o32.setStyleSheet(outputStyle)
        coilEfficiencyLayout.addRow("Output Voltage (V)",self.o32)
        
        self.o33 = QtW.QLineEdit("...")
        self.o33.setReadOnly(True)
        self.o33.setStyleSheet(outputStyle)
        coilEfficiencyLayout.addRow("Input Current (A)",self.o33)
        
        self.o34 = QtW.QLineEdit("...")
        self.o34.setReadOnly(True)
        self.o34.setStyleSheet(outputStyle)
        coilEfficiencyLayout.addRow("Output Current (A)",self.o34)
        
        self.o35 = QtW.QLineEdit("...")
        self.o35.setReadOnly(True)
        self.o35.setStyleSheet(outputStyle)
        coilEfficiencyLayout.addRow("Input Power (W)",self.o35)
        
        self.o36 = QtW.QLineEdit("...")
        self.o36.setReadOnly(True)
        self.o36.setStyleSheet(outputStyle)
        coilEfficiencyLayout.addRow("Output Power (W)",self.o36)
        
        self.o37 = QtW.QLineEdit("...")
        self.o37.setReadOnly(True)
        self.o37.setStyleSheet(outputStyle)
        coilEfficiencyLayout.addRow("Power Transfer Efficiency (%)",self.o37)
        
        self.b31 = QtW.QPushButton("Calculate")
        self.b31.clicked.connect(self.calcCoilEfficiency)
        coilEfficiencyLayout.addRow(self.b31)
        
        coilEfficiency.setLayout(coilEfficiencyLayout)      
        
        ##################################################
        
        
        layout.addWidget(coilCommon,0,0)
        layout.addWidget(coilParameters,1,0)
        layout.addWidget(coilMatchingComponents,1,1)
        layout.addWidget(coilEfficiency,1,3)
        layout.setSizeConstraint(QtW.QLayout.SetFixedSize)
        self.setLayout(layout)
        
        self.setWindowTitle("Cylindrical Coil Parameters Calculator")

        self.show()

        
    def calcCoilParam(self, text):      
               
        if self.e01.text() != '' and self.e11.text() != '' and self.e12.text() != ''and self.e13.text() != '' and self.e14.text() != '' and self.e15.text() != '':

            # Get the inputs            
            freq = float (self.e01.text())            
            coil_diameter = float (self.e11.text())
            wire_diameter = float (self.e12.text())
            wire_conductivity = float (self.e15.text())
            winding_num_turns = int (self.e13.text())
            winding_height = float (self.e14.text())     
            
            # Calculate wire cross section area
            wire_crossSection_area = m.pi*m.pow(wire_diameter/2,2)
            
            # Calculate winding thickness
            winding_num_turns_per_layer = winding_height / wire_diameter
            winding_num_layers = winding_num_turns / winding_num_turns_per_layer
            
            wire_length = 0.0
            for ilayer in range(int(winding_num_layers)):
                wire_length = wire_length + m.pi*(coil_diameter+wire_diameter+2*(ilayer-1)*wire_diameter*m.cos(30/180*m.pi))*winding_num_turns_per_layer
            wire_length = wire_length + m.pi*(coil_diameter+wire_diameter+2*int(winding_num_layers)*wire_diameter*m.cos(30/180*m.pi))*winding_num_turns_per_layer*(winding_num_layers-int(winding_num_layers))
              
            winding_volume = wire_crossSection_area*wire_length    
            winding_thickness = m.sqrt((winding_volume/winding_height + m.pi*m.pow(coil_diameter/2,2))/m.pi)-coil_diameter/2
            
            # Calculate skin depth
            wire_skin_depth = m.sqrt ( 1 / (m.pi*freq*wire_conductivity*4*m.pi*1e-7) )

            # Calculate winding AC resistance        
            skp = wire_skin_depth * (1-m.exp(-wire_diameter/2/wire_skin_depth))
            Z = 0.62006 * wire_diameter / 2 / wire_skin_depth
            Y = 0.189774 / m.pow((1+0.272481*m.pow((m.pow(Z,1.82938)-m.pow(Z,-0.99457)),2)),1.0941)
            aeff = m.pi * (wire_diameter*skp-m.pow(skp,2))*(1+Y)
            
            winding_AC_resistance = wire_length / aeff / wire_conductivity

            # Calculate winding effective bulk conductivity
            winding_eff_bulk_sigma = wire_length / winding_AC_resistance / wire_crossSection_area
            
            # Display results
            self.o11.setText(str('{:.6g}'.format(wire_crossSection_area)))
            self.o12.setText(str('{:.6g}'.format(wire_length)))
            self.o13.setText(str('{:.6g}'.format(winding_thickness)))
            self.o14.setText(str('{:.6g}'.format(winding_AC_resistance)))
            self.o15.setText(str('{:.6g}'.format(winding_eff_bulk_sigma)))
            
        else:
            msgBox = QtW.QMessageBox()
            msgBox.setWindowTitle("Error !")
            msgBox.critical (msgBox,"Error", "Please enter all input values for Coil Parameters calculation !")
            
    def calcCoilMatching(self, text):  
        if self.e01.text() != '' and self.e21.text() != '' and self.e22.text() != ''and self.e23.text() != '' and self.e24.text() != '' and self.e25.text() != '' and self.e26.text() != '' and self.e27.text() != '' and self.e28.text() != '':

            # Get the inputs            
            freq = float (self.e01.text())            
            RS = float (self.e21.text())
            RL = float (self.e22.text())
            R1 = float (self.e23.text())
            L1 = float (self.e24.text())
            R2 = float (self.e25.text())
            L2 = float (self.e26.text())
            R12 = float (self.e27.text())
            K = float (self.e28.text())
            L12 = m.sqrt(L1*L2)*K
            
            if RL <= R2:
                msgBox = QtW.QMessageBox()
                msgBox.setWindowTitle("Error !")
                msgBox.critical (msgBox,"Error", "RL must be greater than R2 !")
            else:
            
                w = 2 * m.pi * freq
                
                Z11 = R1 + 1j * w * L1
                Z22 = R2 + 1j * w * L2
                Z12 = Z21 = R12 + 1j * w * L12
                
                Q1 = w * L1 / R1
                Q2 = w * L2 / R2
                
                LL = RL/w*m.sqrt(R2/(RL-R2))
                CL = 1/w/(w*L2+m.sqrt(R2*(RL-R2)))
                
                ZL = Z22.conjugate()
    
                Zin=Z11-(Z12*Z21)/(Z22+ZL)      
                
                R1p = Zin.real
                L1p = Zin.imag / w
            
                if RS <= R1p or R1p < R1:
                    msgBox = QtW.QMessageBox()
                    msgBox.setWindowTitle("Error !")
                    msg = "Converted input resistance (R1 prime) is invalid " + str('{:.6g}'.format(R1p)) + " !"
                    msgBox.critical (msgBox,"Error", msg)
                else:
                    LS = RS/w*m.sqrt(R1p/(RS-R1p))            
                    CS = 1/w/(w*L1p+m.sqrt(R1p*(RS-R1p)))
                
                    # Display results
                    self.o21.setText(str('{:.0f}'.format(Q1)))
                    self.o22.setText(str('{:.0f}'.format(Q2)))
                    self.o23.setText(str('{:.6g}'.format(LS)))
                    self.o24.setText(str('{:.6g}'.format(CS)))
                    self.o25.setText(str('{:.6g}'.format(LL)))
                    self.o26.setText(str('{:.6g}'.format(CL)))
                    self.o27.setText(str('{:.6g}'.format(L12)))
                    
                    self.e32.setText(str('{:.6g}'.format(LS)))
                    self.e33.setText(str('{:.6g}'.format(CS)))
                    self.e34.setText(str('{:.6g}'.format(LL)))
                    self.e35.setText(str('{:.6g}'.format(CL)))
            
        else:
            
            msgBox = QtW.QMessageBox()
            msgBox.setWindowTitle("Error !")
            msgBox.critical (msgBox,"Error", "Please enter all input values for Mathcing Components calculation !")

    def calcCoilEfficiency(self, text):  

        
        if self.e01.text() != '' and self.e21.text() != '' and self.e22.text() != ''and self.e23.text() != '' and self.e24.text() != '' and self.e25.text() != '' and self.e26.text() != '' and self.e27.text() != '' and self.e28.text() != '' and self.e31.text() != '' and self.e32.text() != '' and self.e33.text() != ''and self.e34.text() != '' and self.e35.text() != '' :

            # Get the inputs            
            freq = float (self.e01.text())            
            RS = float (self.e21.text())
            RL = float (self.e22.text())
            R1 = float (self.e23.text())
            L1 = float (self.e24.text())
            R2 = float (self.e25.text())
            L2 = float (self.e26.text())
            R12 = float (self.e27.text())
            L12 = float (self.e28.text())
            
            if RL <= R2:
                msgBox = QtW.QMessageBox()
                msgBox.setWindowTitle("Error !")
                msgBox.critical (msgBox,"Error", "RL must be greater than R2 !")
            else:
            
                w = 2 * m.pi * freq
                
                Z11 = R1 + 1j * w * L1
                Z22 = R2 + 1j * w * L2
                Z12 = Z21 = R12 + 1j * w * L12
                
                LL = float (self.e34.text())
                CL = float (self.e35.text())
                
                ZRLLL = RL * 1j * w * LL / (RL + 1j * w * LL)
                ZL = 1/(1j*w*CL) + ZRLLL
    
                Zin=Z11-(Z12*Z21)/(Z22+ZL)      
                
                R1p = Zin.real
#                L1p = Zin.imag / w
            
                if RS <= R1p or R1p < R1:
                    msgBox = QtW.QMessageBox()
                    msgBox.setWindowTitle("Error !")
                    msg = "Converted input resistance (R1 prime) is invalid " + str('{:.6g}'.format(R1p)) + " !"
                    msgBox.critical (msgBox,"Error", msg)
                else:
                    LS = float (self.e32.text())          
                    CS = float (self.e33.text()) 
                    
                    Vsrc = float (self.e31.text()) 
                    
                    Z1p = Zin
                    Z1pC = 1/(1j*w*CS) + Z1p
                    Z1 = 1j*w*LS*Z1pC/(Z1pC+1j*w*LS)
                    
                    ZS1 = RS + Z1
                    Isrc = Vsrc / ZS1
                    V1 = Isrc * Z1

                    It = V1 / Z1pC
                    Vt = It * Z1p
                    
                    Ir = ( Vt - Z11*It ) / Z12
                    Vr = Z21 * It + Z22 * Ir

                    Vload = Vr + Ir * 1 / (1j*w*CL)
                    Iload = Vload / RL
                    
                    Vin = V1
                    Iin = Isrc
                    Pin = abs(Vin * Iin)
                    Vout = Vload
                    Iout = Iload
                    Pout = abs(Vout*Iout)
                    Eff = Pout / Pin * 100
                
                    # Display results
                    self.o31.setText(str('{:.6g}'.format(abs(Vin))))
                    self.o32.setText(str('{:.6g}'.format(abs(Vout))))
                    self.o33.setText(str('{:.6g}'.format(abs(Iin))))
                    self.o34.setText(str('{:.6g}'.format(abs(Iout))))
                    self.o35.setText(str('{:.6g}'.format(Pin)))
                    self.o36.setText(str('{:.6g}'.format(Pout)))
                    self.o37.setText(str('{:.3f}'.format(Eff)))
                    
        else:
            msgBox = QtW.QMessageBox()
            msgBox.setWindowTitle("Error !")
            msgBox.critical (msgBox,"Error", "Please enter all input values for Coil Efficiency calculation !")


    
if __name__ == '__main__':
    
    app = QtW.QApplication(sys.argv)
    mw = MainWindow()
    app.exec_()

