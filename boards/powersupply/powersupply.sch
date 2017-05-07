EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:w_connectors
LIBS:tda7292
LIBS:audio
LIBS:powersupply-cache
EELAYER 25 0
EELAYER END
$Descr USLetter 11000 8500
encoding utf-8
Sheet 1 1
Title "LR4 Active Crossover, Power Supply, and Amp"
Date "2017-04-26"
Rev "0"
Comp "Scott Howard"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L R R2
U 1 1 58E0977A
P 5800 3550
F 0 "R2" V 5880 3550 50  0000 C CNN
F 1 "1K 1W" V 5800 3550 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM15mm" V 5730 3550 50  0001 C CNN
F 3 "" H 5800 3550 50  0000 C CNN
F 4 "ROX1SJ1K0" V 5800 3550 60  0001 C CNN "manf#"
	1    5800 3550
	1    0    0    -1  
$EndComp
$Comp
L R R3
U 1 1 58E097EA
P 5800 3850
F 0 "R3" V 5880 3850 50  0000 C CNN
F 1 "1K 1W" V 5800 3850 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM15mm" V 5730 3850 50  0001 C CNN
F 3 "" H 5800 3850 50  0000 C CNN
	1    5800 3850
	1    0    0    -1  
$EndComp
$Comp
L CP1 C2
U 1 1 58E14E27
P 5450 3550
F 0 "C2" H 5475 3650 50  0000 L CNN
F 1 "6800u" H 5475 3450 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Radial_D22_L41_P10" H 5450 3550 50  0001 C CNN
F 3 "" H 5450 3550 50  0000 C CNN
F 4 "UVR1H682MRD" H 5450 3550 60  0001 C CNN "manf#"
	1    5450 3550
	1    0    0    -1  
$EndComp
$Comp
L CP1 C5
U 1 1 58E14EB6
P 5450 3850
F 0 "C5" H 5475 3950 50  0000 L CNN
F 1 "6800u" H 5475 3750 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Radial_D22_L41_P10" H 5450 3850 50  0001 C CNN
F 3 "" H 5450 3850 50  0000 C CNN
	1    5450 3850
	1    0    0    -1  
$EndComp
$Comp
L D_Bridge_-A+A D1
U 1 1 58E312D3
P 4700 3800
F 0 "D1" H 4450 4100 50  0000 C CNN
F 1 "Diode_Bridge" H 5050 3450 50  0000 C CNN
F 2 "Diodes_ThroughHole:Diode_Bridge_18.5x5.5" H 4700 3800 50  0001 C CNN
F 3 "" H 4700 3800 50  0000 C CNN
F 4 "GBU8J-BP" H 4700 3800 60  0001 C CNN "manf#"
	1    4700 3800
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X03 P1
U 1 1 58E31639
P 3450 3700
F 0 "P1" H 3450 3900 50  0000 C CNN
F 1 "CONN_01X03" V 3550 3700 50  0000 C CNN
F 2 "Terminal_Blocks:TerminalBlock_Pheonix_MKDS1.5-3pol" H 3450 3700 50  0001 C CNN
F 3 "" H 3450 3700 50  0000 C CNN
F 4 "1935174" H 3450 3700 60  0001 C CNN "manf#"
	1    3450 3700
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR2
U 1 1 58E57068
P 3800 3700
F 0 "#PWR2" H 3800 3450 50  0001 C CNN
F 1 "GND" H 3800 3550 50  0000 C CNN
F 2 "" H 3800 3700 50  0000 C CNN
F 3 "" H 3800 3700 50  0000 C CNN
	1    3800 3700
	1    0    0    -1  
$EndComp
$Comp
L C_Small C1
U 1 1 58E5D56E
P 5200 3550
F 0 "C1" H 5210 3620 50  0000 L CNN
F 1 "100n" H 5210 3470 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Disc_D3_P2.5" H 5200 3550 50  0001 C CNN
F 3 "" H 5200 3550 50  0000 C CNN
F 4 "K104K15X7RF53L2" H 5200 3550 60  0001 C CNN "manf#"
	1    5200 3550
	1    0    0    -1  
$EndComp
$Comp
L C_Small C4
U 1 1 58E5D68C
P 5200 3850
F 0 "C4" H 5210 3920 50  0000 L CNN
F 1 "100n" H 5210 3770 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Disc_D3_P2.5" H 5200 3850 50  0001 C CNN
F 3 "" H 5200 3850 50  0000 C CNN
	1    5200 3850
	1    0    0    -1  
$EndComp
Text Label 3650 3400 0    60   ~ 0
+12VAC
Text Label 3650 4200 0    60   ~ 0
-12VAC
Connection ~ 5800 3700
Wire Wire Line
	5100 3400 6200 3400
Wire Wire Line
	5100 4000 6200 4000
Wire Wire Line
	3650 3400 4700 3400
Wire Wire Line
	4700 4200 3650 4200
Wire Wire Line
	3650 4200 3650 3800
Wire Wire Line
	3650 3600 3650 3400
Wire Wire Line
	3650 3700 3800 3700
Wire Wire Line
	5100 3800 5100 3400
Connection ~ 5450 3400
Wire Wire Line
	4300 3800 4300 4350
Wire Wire Line
	4300 4350 5100 4350
Wire Wire Line
	5100 4350 5100 4000
Connection ~ 5450 4000
Wire Wire Line
	5450 3400 5450 3350
Wire Wire Line
	5450 4050 5450 4000
Connection ~ 5200 3400
Wire Wire Line
	5200 3400 5200 3450
Wire Wire Line
	5200 3650 5200 3750
Wire Wire Line
	5200 3950 5200 4000
Connection ~ 5200 4000
Connection ~ 5200 3700
Connection ~ 5450 3700
Wire Wire Line
	5200 3700 6200 3700
$Comp
L Transformer_SP_2S novalue4
U 1 1 5908AD80
P 1600 3700
F 0 "novalue4" H 1600 4200 50  0000 C CNN
F 1 "TRANSFO_3" H 1600 3200 50  0000 C CNN
F 2 "" H 1600 3700 50  0001 C CNN
F 3 "" H 1600 3700 50  0000 C CNN
F 4 "VPS24-3300" H 1600 3700 60  0001 C CNN "manf#"
	1    1600 3700
	1    0    0    -1  
$EndComp
Text Notes 2450 3300 0    60   ~ 0
This is audio ground NOT protective ground
$Comp
L LM317_SOT223 novalue6
U 1 1 590C121C
P 2500 1350
F 0 "novalue6" H 2500 1650 50  0000 C CNN
F 1 "POWER OUTLET" H 2550 1100 50  0000 L CNN
F 2 "" H 2500 1350 50  0001 C CNN
F 3 "" H 2500 1350 50  0000 C CNN
F 4 "719W-00/03" H 2500 1350 60  0001 C CNN "manf#"
	1    2500 1350
	1    0    0    -1  
$EndComp
$Comp
L LM317_SOT223 novalue7
U 1 1 590C15D2
P 2500 2150
F 0 "novalue7" H 2500 2450 50  0000 C CNN
F 1 "fuse 1A, 250V rated" H 2550 1900 50  0000 L CNN
F 2 "" H 2500 2150 50  0001 C CNN
F 3 "" H 2500 2150 50  0000 C CNN
F 4 "0217001.HXP" H 2500 2150 60  0001 C CNN "manf#"
	1    2500 2150
	1    0    0    -1  
$EndComp
Wire Wire Line
	4700 4100 4700 4200
Wire Wire Line
	4400 3800 4300 3800
Wire Wire Line
	4700 3400 4700 3500
Wire Wire Line
	5000 3800 5100 3800
Text Notes 7350 5500 0    60   ~ 0
http://www.signaltransfer.freeuk.com/powerout.htm\ntl07x max V is +/15V\nVp after rectifier = 15V\nVp before rectifier = 17 V (two diode drop off)\nVrms before rectifier = 12 V <- use this transformer\n\nFor one 8 ohm driver:\n15 Vs = ~~8 W per driver for 1% THD (10W for 10%)\nsqrt(10 W * 8 omh) = 8.9 Vrms over driver\n8.9 V rms = 12.6 Vp\nIpk = 12.6/8 = 1.6 A peak <-5 less than Imax = 5A\nEach rail (capacitor) only supplies 1/2 of the time\nso average per time per capacitor:\nI avg = 1.6 A peak/pi = 0.5 A\n(should we just be talking about power instead? 4*10W+2*20W=80W,\n80W/2 = 40W on each rail, 40W/15V DC = 2.6 A DC per rail)\n\n0.1% noise = .0089 V rms at output\nsupply side rejection = 75 dB,gain =30 dB, net rejection 45 dB\n0.0089 V rms out = 1.59 V noise on supply side\nneed to calc capacitance and ripple)\n\nV rms ripple = ripple factor * V_avg_DC\nripple factor = 1/(4*sqrt(3)*f*C*R)\nf = 60 Hz\n\nsawtooth wave:\nvrms = I_avg /(4*sqrt(3)*freq*cap)\nassume avg is approx the dc value\n\nvdc =15, i_avg = 2.6\n3900 uF gets 1.59 V rms\n\nthen use current = C dV/dt (with V=Vrms cos(omega t))\nI rms =  I_avg*pi /(2*sqrt(3)) = 0.9 * I_avg = 2.34 A rms\n
Text Notes 2950 5250 0    60   ~ 0
-put a small, better behaved cap in parallel to decouple since big caps have bad esr\n-put a resistor that discharges cap when power is off over 6.8 seconds (1k)
$Comp
L CONN_01X03 P2
U 1 1 590CB8B6
P 6400 3700
F 0 "P2" H 6400 3900 50  0000 C CNN
F 1 "CONN_01X03" V 6500 3700 50  0000 C CNN
F 2 "Terminal_Blocks:TerminalBlock_Pheonix_MKDS1.5-3pol" H 6400 3700 50  0001 C CNN
F 3 "" H 6400 3700 50  0000 C CNN
F 4 "1935174" H 6400 3700 60  0001 C CNN "manf#"
	1    6400 3700
	1    0    0    -1  
$EndComp
Wire Wire Line
	6200 3400 6200 3600
Connection ~ 5800 3400
Wire Wire Line
	6200 4000 6200 3800
Connection ~ 5800 4000
$Comp
L +15V #PWR1
U 1 1 590CBACD
P 5450 3350
F 0 "#PWR1" H 5450 3200 50  0001 C CNN
F 1 "+15V" H 5450 3490 50  0000 C CNN
F 2 "" H 5450 3350 50  0000 C CNN
F 3 "" H 5450 3350 50  0000 C CNN
	1    5450 3350
	1    0    0    -1  
$EndComp
$Comp
L -15V #PWR4
U 1 1 590CBBAE
P 5450 4050
F 0 "#PWR4" H 5450 4150 50  0001 C CNN
F 1 "-15V" H 5450 4200 50  0000 C CNN
F 2 "" H 5450 4050 50  0000 C CNN
F 3 "" H 5450 4050 50  0000 C CNN
	1    5450 4050
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR3
U 1 1 590CBEA0
P 6050 3700
F 0 "#PWR3" H 6050 3450 50  0001 C CNN
F 1 "GND" H 6050 3550 50  0000 C CNN
F 2 "" H 6050 3700 50  0000 C CNN
F 3 "" H 6050 3700 50  0000 C CNN
	1    6050 3700
	1    0    0    -1  
$EndComp
Connection ~ 6050 3700
Text Notes 1000 3150 0    60   ~ 0
trans. chasis to proected earth
$EndSCHEMATC
