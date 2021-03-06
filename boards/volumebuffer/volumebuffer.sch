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
LIBS:volumebuffer-cache
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
L TL072 U2
U 1 1 58E6EA22
P 3150 2850
F 0 "U2" H 3150 3050 50  0000 L CNN
F 1 "TL072" H 3150 2650 50  0000 L CNN
F 2 "Housings_DIP:DIP-8_W7.62mm" H 3150 2850 50  0001 C CNN
F 3 "" H 3150 2850 50  0000 C CNN
F 4 "tl072cp" H 3150 2850 60  0001 C CNN "manf#"
	1    3150 2850
	1    0    0    -1  
$EndComp
$Comp
L TL072 U2
U 2 1 58E6EAB3
P 2600 3550
F 0 "U2" H 2600 3750 50  0000 L CNN
F 1 "TL072" H 2550 3400 50  0000 L CNN
F 2 "Housings_DIP:DIP-8_W7.62mm" H 2600 3550 50  0001 C CNN
F 3 "" H 2600 3550 50  0000 C CNN
	2    2600 3550
	1    0    0    -1  
$EndComp
$Comp
L POT_Dual RV1
U 1 1 58E6EC42
P 2000 3250
F 0 "RV1" H 2160 3560 50  0000 C CNN
F 1 "DUAL_POT" H 2000 3350 50  0000 C CNN
F 2 "Connectors_Molex:Molex_KK-6410-06_06x2.54mm_Straight" H 2000 3250 50  0001 C CNN
F 3 "http://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocNm=640456&DocType=Customer+Drawing&DocLang=English" H 2000 3250 50  0001 C CNN
F 4 "640456-6" H 2000 3250 60  0001 C CNN "manf#"
	1    2000 3250
	0    1    1    0   
$EndComp
$Comp
L GND #PWR01
U 1 1 58EE846A
P 1900 3650
F 0 "#PWR01" H 1900 3400 50  0001 C CNN
F 1 "GND" H 1900 3500 50  0000 C CNN
F 2 "" H 1900 3650 50  0000 C CNN
F 3 "" H 1900 3650 50  0000 C CNN
	1    1900 3650
	1    0    0    -1  
$EndComp
$Comp
L C_Small C8
U 1 1 58EE9F0E
P 2700 3950
F 0 "C8" H 2710 4020 50  0000 L CNN
F 1 "100n" H 2710 3870 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Disc_D3_P2.5" H 2700 3950 50  0001 C CNN
F 3 "" H 2700 3950 50  0000 C CNN
	1    2700 3950
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR02
U 1 1 58EE9F14
P 2700 4050
F 0 "#PWR02" H 2700 3800 50  0001 C CNN
F 1 "GND" H 2700 3900 50  0000 C CNN
F 2 "" H 2700 4050 50  0000 C CNN
F 3 "" H 2700 4050 50  0000 C CNN
	1    2700 4050
	1    0    0    -1  
$EndComp
$Comp
L C_Small C4
U 1 1 58EEA412
P 2700 3150
F 0 "C4" H 2710 3220 50  0000 L CNN
F 1 "100n" H 2710 3070 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Disc_D3_P2.5" H 2700 3150 50  0001 C CNN
F 3 "" H 2700 3150 50  0000 C CNN
	1    2700 3150
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR03
U 1 1 58EEA418
P 2700 3050
F 0 "#PWR03" H 2700 2800 50  0001 C CNN
F 1 "GND" H 2700 2900 50  0000 C CNN
F 2 "" H 2700 3050 50  0000 C CNN
F 3 "" H 2700 3050 50  0000 C CNN
	1    2700 3050
	-1   0    0    1   
$EndComp
Text Notes 1300 2150 0    60   ~ 0
Baffle Step:\nfeedback R1 || C, then R2 to ground\nf_bs = 1/(R1*C*2*pi)\nR2 = R1/(BS_gain-1)\nfor 6 dB:\nR2 = R1/(2-1)=R1\nfor 3 dB:\nR2 = R1/(\sqrt{2}-1)=R1*2.4142
$Comp
L GND #PWR04
U 1 1 58FA1433
P 1900 3150
F 0 "#PWR04" H 1900 2900 50  0001 C CNN
F 1 "GND" H 1900 3000 50  0000 C CNN
F 2 "" H 1900 3150 50  0000 C CNN
F 3 "" H 1900 3150 50  0000 C CNN
	1    1900 3150
	1    0    0    -1  
$EndComp
Text Label 1350 3350 0    60   ~ 0
left_in
Text Label 1350 2850 0    60   ~ 0
right_in
$Comp
L CONN_01X03 P2
U 1 1 58FBBFDF
P 1000 3150
F 0 "P2" H 1000 3350 50  0000 C CNN
F 1 "CONN_01X03" V 1100 3150 50  0000 C CNN
F 2 "Terminal_Blocks:TerminalBlock_Pheonix_MKDS1.5-3pol" H 1000 3150 50  0001 C CNN
F 3 "" H 1000 3150 50  0000 C CNN
F 4 "1935174" H 1000 3150 60  0001 C CNN "manf#"
	1    1000 3150
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR05
U 1 1 58FBD3A1
P 1450 3100
F 0 "#PWR05" H 1450 2850 50  0001 C CNN
F 1 "GND" H 1450 2950 50  0000 C CNN
F 2 "" H 1450 3100 50  0000 C CNN
F 3 "" H 1450 3100 50  0000 C CNN
	1    1450 3100
	1    0    0    -1  
$EndComp
Text Notes 600  2700 0    60   ~ 0
connect pin 2 to chassis as well
Wire Wire Line
	1200 3100 1450 3100
Wire Wire Line
	2850 2950 2850 3350
Wire Wire Line
	2850 3350 3600 3350
Wire Wire Line
	3450 2850 3550 2850
Wire Wire Line
	3550 2750 3550 3000
Wire Wire Line
	3550 2750 3900 2750
Wire Wire Line
	2300 3650 2300 4300
Wire Wire Line
	2900 3550 3400 3550
Wire Wire Line
	2350 2750 2850 2750
Wire Wire Line
	1200 3350 1900 3350
Wire Wire Line
	2100 3450 2300 3450
Wire Wire Line
	2500 3850 2500 4050
Wire Wire Line
	2500 3850 2700 3850
Wire Wire Line
	2500 3250 2500 3050
Wire Wire Line
	2700 3250 2500 3250
Wire Wire Line
	1200 3150 1200 3100
Wire Wire Line
	1200 2850 1200 3050
Wire Wire Line
	1200 3350 1200 3250
Wire Wire Line
	3550 3000 4350 3000
Connection ~ 3550 2850
Wire Wire Line
	3400 3450 3400 3650
Wire Wire Line
	3400 3450 4450 3450
Wire Wire Line
	3400 3650 3900 3650
Connection ~ 3400 3550
$Comp
L R R7
U 1 1 590237A2
P 3450 3200
F 0 "R7" V 3530 3200 50  0000 C CNN
F 1 "Rbs1" V 3450 3200 50  0000 C CNN
F 2 "scimpy_library:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal" V 3380 3200 50  0001 C CNN
F 3 "" H 3450 3200 50  0000 C CNN
	1    3450 3200
	-1   0    0    1   
$EndComp
Wire Wire Line
	3450 3050 3450 2850
Wire Wire Line
	3450 3050 3600 3050
Wire Wire Line
	3600 3350 3600 3250
Connection ~ 3450 3350
$Comp
L R R8
U 1 1 59024462
P 3750 3350
F 0 "R8" V 3830 3350 50  0000 C CNN
F 1 "Rbs2" V 3750 3350 50  0000 C CNN
F 2 "scimpy_library:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal" V 3680 3350 50  0001 C CNN
F 3 "" H 3750 3350 50  0000 C CNN
	1    3750 3350
	0    -1   -1   0   
$EndComp
$Comp
L GND #PWR06
U 1 1 59024750
P 3900 3350
F 0 "#PWR06" H 3900 3100 50  0001 C CNN
F 1 "GND" H 3900 3200 50  0000 C CNN
F 2 "" H 3900 3350 50  0000 C CNN
F 3 "" H 3900 3350 50  0000 C CNN
	1    3900 3350
	0    -1   -1   0   
$EndComp
$Comp
L R R9
U 1 1 59025368
P 2900 3750
F 0 "R9" V 2980 3750 50  0000 C CNN
F 1 "Rbs1" V 2900 3750 50  0000 C CNN
F 2 "scimpy_library:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal" V 2830 3750 50  0001 C CNN
F 3 "" H 2900 3750 50  0000 C CNN
	1    2900 3750
	-1   0    0    1   
$EndComp
Wire Wire Line
	2900 3600 2900 3550
Wire Wire Line
	2900 3600 3050 3600
Wire Wire Line
	3050 3600 3050 3650
Wire Wire Line
	3050 3900 3050 3850
Wire Wire Line
	2900 4300 2900 3900
Wire Wire Line
	2900 3900 3050 3900
Wire Wire Line
	2300 4300 2900 4300
$Comp
L R R14
U 1 1 59026A5E
P 2150 4300
F 0 "R14" V 2230 4300 50  0000 C CNN
F 1 "Rbs2" V 2150 4300 50  0000 C CNN
F 2 "scimpy_library:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal" V 2080 4300 50  0001 C CNN
F 3 "" H 2150 4300 50  0000 C CNN
	1    2150 4300
	0    -1   -1   0   
$EndComp
$Comp
L C_Small C5
U 1 1 590A1DA3
P 3600 3150
F 0 "C5" H 3610 3220 50  0000 L CNN
F 1 "100n" H 3610 3070 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Disc_D6_P5" H 3600 3150 50  0001 C CNN
F 3 "" H 3600 3150 50  0000 C CNN
F 4 "FG26C0G1H104JNT06" H 3600 3150 60  0001 C CNN "manf#"
	1    3600 3150
	1    0    0    -1  
$EndComp
$Comp
L C_Small C7
U 1 1 590A1F6B
P 3050 3750
F 0 "C7" H 3060 3820 50  0000 L CNN
F 1 "100n" H 3060 3670 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Disc_D6_P5" H 3050 3750 50  0001 C CNN
F 3 "" H 3050 3750 50  0000 C CNN
	1    3050 3750
	1    0    0    -1  
$EndComp
Wire Wire Line
	1200 2850 1900 2850
Wire Wire Line
	2100 3500 2100 3450
Wire Wire Line
	2100 3000 2350 3000
Wire Wire Line
	2350 3000 2350 2750
$Comp
L TL074 U1
U 3 1 590D1545
P 5850 2750
F 0 "U1" H 5850 2950 50  0000 L CNN
F 1 "TL074" H 5850 2550 50  0000 L CNN
F 2 "Housings_DIP:DIP-14_W7.62mm" H 5800 2850 50  0001 C CNN
F 3 "" H 5900 2950 50  0000 C CNN
F 4 "tl074cn" H 5850 2750 60  0001 C CNN "manf#"
	3    5850 2750
	1    0    0    -1  
$EndComp
$Comp
L C_Small C6
U 1 1 590D1552
P 5950 3350
F 0 "C6" H 5960 3420 50  0000 L CNN
F 1 "100n" H 5960 3270 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Disc_D3_P2.5" H 5950 3350 50  0001 C CNN
F 3 "" H 5950 3350 50  0000 C CNN
	1    5950 3350
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR07
U 1 1 590D1559
P 5950 3450
F 0 "#PWR07" H 5950 3200 50  0001 C CNN
F 1 "GND" H 5950 3300 50  0000 C CNN
F 2 "" H 5950 3450 50  0000 C CNN
F 3 "" H 5950 3450 50  0000 C CNN
	1    5950 3450
	1    0    0    -1  
$EndComp
Wire Wire Line
	5750 3050 5750 3450
$Comp
L C_Small C1
U 1 1 590D1566
P 5950 2400
F 0 "C1" H 5960 2470 50  0000 L CNN
F 1 "100n" H 5960 2320 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Disc_D3_P2.5" H 5950 2400 50  0001 C CNN
F 3 "" H 5950 2400 50  0000 C CNN
F 4 "K104K15X7RF53L2" H 5950 2400 60  0001 C CNN "manf#"
	1    5950 2400
	1    0    0    -1  
$EndComp
Wire Wire Line
	5750 2300 5950 2300
Connection ~ 5750 2300
Wire Wire Line
	5750 3250 5950 3250
Connection ~ 5750 3250
Text Notes 1300 6350 0    60   ~ 0
http://www.linkwitzlab.com/models.htm#E\n\nall pass filters gives delay = 2 RC\nfor f < f0 = 1/(2pi R C)\nNeed f0 > cross-over freq\ntypically need at least 2 stages to get\nf0 > cross-over freq and enough delay\n\ntg = 2RC/(1+(f*RC*2pi)^2)\ntg = 1/(pi*f_0)* 1/(1+(f/f_0)^2)
$Comp
L R R5
U 1 1 590D1572
P 5400 3050
F 0 "R5" V 5480 3050 50  0000 C CNN
F 1 "Rph" V 5400 3050 50  0000 C CNN
F 2 "scimpy_library:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal" V 5330 3050 50  0001 C CNN
F 3 "" H 5400 3050 50  0000 C CNN
	1    5400 3050
	-1   0    0    1   
$EndComp
$Comp
L C_Small C3
U 1 1 590D1579
P 5150 2850
F 0 "C3" H 5160 2920 50  0000 L CNN
F 1 "100n" H 5160 2770 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Disc_D6_P5" H 5150 2850 50  0001 C CNN
F 3 "" H 5150 2850 50  0000 C CNN
	1    5150 2850
	0    -1   -1   0   
$EndComp
$Comp
L GND #PWR08
U 1 1 590D1580
P 5400 3200
F 0 "#PWR08" H 5400 2950 50  0001 C CNN
F 1 "GND" H 5400 3050 50  0000 C CNN
F 2 "" H 5400 3200 50  0000 C CNN
F 3 "" H 5400 3200 50  0000 C CNN
	1    5400 3200
	1    0    0    -1  
$EndComp
Wire Wire Line
	4350 2850 5050 2850
Wire Wire Line
	5400 2850 5400 2900
Wire Wire Line
	5250 2850 5550 2850
Connection ~ 5400 2850
Wire Wire Line
	5750 2200 5750 2450
$Comp
L R R1
U 1 1 590D158B
P 5200 2000
F 0 "R1" V 5280 2000 50  0000 C CNN
F 1 "2K2" V 5200 2000 50  0000 C CNN
F 2 "scimpy_library:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal" V 5130 2000 50  0001 C CNN
F 3 "" H 5200 2000 50  0000 C CNN
F 4 "MCMF0W4FF2201A50" V 5200 2000 60  0001 C CNN "manf#"
	1    5200 2000
	0    1    1    0   
$EndComp
Wire Wire Line
	4900 2850 4900 2000
Wire Wire Line
	4900 2000 5050 2000
Connection ~ 4900 2850
Wire Wire Line
	5350 2000 5900 2000
Wire Wire Line
	5550 2650 5400 2650
Wire Wire Line
	5400 2650 5400 2000
Connection ~ 5400 2000
Wire Wire Line
	6150 2750 6750 2750
Wire Wire Line
	6200 2000 6250 2000
Wire Wire Line
	6250 2000 6250 2750
Connection ~ 6250 2750
Text Notes 3550 6200 0    60   ~ 0
high pass b/c it's for tweeter\nthis way high freq see no phase shift\nBut you want a constant delay over cross-over region\nso maybe f0 > 2 fc?\nfc = 1 kHz crossover\nf0 = 2 khz\ndelay = 127 microsec
Text Notes 6400 6200 0    60   ~ 0
How much delay do you want?\nRC = \frac{ 1 \pm \sqrt{1-(tg*\omega_c)^2} }{t_g (\omega_c^2)}\ntake the smaller one so f0 is bigger!\nfor two stage, make each stage give you t_g/2 delay\nexample: 150 us delay desired, each stage gets 75 us\nRC = 6.36e-4, 3.99e-5\nassume C = 100 nF\nRph = 6.36 kOhm, 399 Ohm\nsmaller one will give flattest response over cross-over region, use that
$Comp
L TL074 U1
U 2 1 590D15A9
P 7550 2650
F 0 "U1" H 7550 2850 50  0000 L CNN
F 1 "TL074" H 7550 2450 50  0000 L CNN
F 2 "Housings_DIP:DIP-14_W7.62mm" H 7500 2750 50  0001 C CNN
F 3 "" H 7600 2850 50  0000 C CNN
	2    7550 2650
	1    0    0    -1  
$EndComp
$Comp
L R R6
U 1 1 590D15B0
P 7100 3050
F 0 "R6" V 7180 3050 50  0000 C CNN
F 1 "Rph" V 7100 3050 50  0000 C CNN
F 2 "scimpy_library:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal" V 7030 3050 50  0001 C CNN
F 3 "" H 7100 3050 50  0000 C CNN
	1    7100 3050
	-1   0    0    1   
$EndComp
$Comp
L C_Small C2
U 1 1 590D15B7
P 6850 2750
F 0 "C2" H 6860 2820 50  0000 L CNN
F 1 "100n" H 6860 2670 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Disc_D6_P5" H 6850 2750 50  0001 C CNN
F 3 "" H 6850 2750 50  0000 C CNN
	1    6850 2750
	0    -1   -1   0   
$EndComp
$Comp
L GND #PWR09
U 1 1 590D15BE
P 7100 3200
F 0 "#PWR09" H 7100 2950 50  0001 C CNN
F 1 "GND" H 7100 3050 50  0000 C CNN
F 2 "" H 7100 3200 50  0000 C CNN
F 3 "" H 7100 3200 50  0000 C CNN
	1    7100 3200
	1    0    0    -1  
$EndComp
Wire Wire Line
	7100 2750 7100 2900
Wire Wire Line
	6950 2750 7250 2750
Connection ~ 7100 2750
$Comp
L R R3
U 1 1 590D15C7
P 6900 2000
F 0 "R3" V 6980 2000 50  0000 C CNN
F 1 "2K2" V 6900 2000 50  0000 C CNN
F 2 "scimpy_library:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal" V 6830 2000 50  0001 C CNN
F 3 "" H 6900 2000 50  0000 C CNN
	1    6900 2000
	0    1    1    0   
$EndComp
$Comp
L R R4
U 1 1 590D15CE
P 7750 2000
F 0 "R4" V 7830 2000 50  0000 C CNN
F 1 "2K2" V 7750 2000 50  0000 C CNN
F 2 "scimpy_library:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal" V 7680 2000 50  0001 C CNN
F 3 "" H 7750 2000 50  0000 C CNN
	1    7750 2000
	0    1    1    0   
$EndComp
Wire Wire Line
	6600 2750 6600 2000
Wire Wire Line
	6600 2000 6750 2000
Connection ~ 6600 2750
Wire Wire Line
	7050 2000 7600 2000
Wire Wire Line
	7250 2550 7100 2550
Wire Wire Line
	7100 2550 7100 2000
Connection ~ 7100 2000
Wire Wire Line
	7850 2650 8900 2650
Wire Wire Line
	7900 2000 7950 2000
Wire Wire Line
	7950 2000 7950 2650
Connection ~ 7950 2650
$Comp
L TL074 U1
U 4 1 590D15E1
P 5850 4650
F 0 "U1" H 5850 4850 50  0000 L CNN
F 1 "TL074" H 5850 4450 50  0000 L CNN
F 2 "Housings_DIP:DIP-14_W7.62mm" H 5800 4750 50  0001 C CNN
F 3 "" H 5900 4850 50  0000 C CNN
	4    5850 4650
	1    0    0    -1  
$EndComp
$Comp
L R R16
U 1 1 590D15E8
P 5400 4950
F 0 "R16" V 5480 4950 50  0000 C CNN
F 1 "Rph" V 5400 4950 50  0000 C CNN
F 2 "scimpy_library:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal" V 5330 4950 50  0001 C CNN
F 3 "" H 5400 4950 50  0000 C CNN
	1    5400 4950
	-1   0    0    1   
$EndComp
$Comp
L C_Small C10
U 1 1 590D15EF
P 5150 4750
F 0 "C10" H 5160 4820 50  0000 L CNN
F 1 "100n" H 5160 4670 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Disc_D6_P5" H 5150 4750 50  0001 C CNN
F 3 "" H 5150 4750 50  0000 C CNN
	1    5150 4750
	0    -1   -1   0   
$EndComp
$Comp
L GND #PWR010
U 1 1 590D15F6
P 5400 5100
F 0 "#PWR010" H 5400 4850 50  0001 C CNN
F 1 "GND" H 5400 4950 50  0000 C CNN
F 2 "" H 5400 5100 50  0000 C CNN
F 3 "" H 5400 5100 50  0000 C CNN
	1    5400 5100
	1    0    0    -1  
$EndComp
Wire Wire Line
	3900 4750 5050 4750
Wire Wire Line
	5400 4750 5400 4800
Wire Wire Line
	5250 4750 5550 4750
Connection ~ 5400 4750
$Comp
L R R10
U 1 1 590D1600
P 5200 4200
F 0 "R10" V 5280 4200 50  0000 C CNN
F 1 "2K2" V 5200 4200 50  0000 C CNN
F 2 "scimpy_library:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal" V 5130 4200 50  0001 C CNN
F 3 "" H 5200 4200 50  0000 C CNN
	1    5200 4200
	0    1    1    0   
$EndComp
$Comp
L R R11
U 1 1 590D1607
P 6050 4200
F 0 "R11" V 6130 4200 50  0000 C CNN
F 1 "2K2" V 6050 4200 50  0000 C CNN
F 2 "scimpy_library:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal" V 5980 4200 50  0001 C CNN
F 3 "" H 6050 4200 50  0000 C CNN
	1    6050 4200
	0    1    1    0   
$EndComp
Wire Wire Line
	4900 4750 4900 4200
Wire Wire Line
	4900 4200 5050 4200
Connection ~ 4900 4750
Wire Wire Line
	5350 4200 5900 4200
Wire Wire Line
	5550 4550 5400 4550
Wire Wire Line
	5400 4550 5400 4200
Connection ~ 5400 4200
Wire Wire Line
	6150 4650 6750 4650
Wire Wire Line
	6200 4200 6250 4200
Wire Wire Line
	6250 4200 6250 4650
Connection ~ 6250 4650
$Comp
L TL074 U1
U 1 1 590D161C
P 7550 4550
F 0 "U1" H 7550 4750 50  0000 L CNN
F 1 "TL074" H 7550 4350 50  0000 L CNN
F 2 "Housings_DIP:DIP-14_W7.62mm" H 7500 4650 50  0001 C CNN
F 3 "" H 7600 4750 50  0000 C CNN
	1    7550 4550
	1    0    0    -1  
$EndComp
$Comp
L R R15
U 1 1 590D1623
P 7100 4900
F 0 "R15" V 7180 4900 50  0000 C CNN
F 1 "Rph" V 7100 4900 50  0000 C CNN
F 2 "scimpy_library:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal" V 7030 4900 50  0001 C CNN
F 3 "" H 7100 4900 50  0000 C CNN
	1    7100 4900
	-1   0    0    1   
$EndComp
$Comp
L C_Small C9
U 1 1 590D162A
P 6850 4650
F 0 "C9" H 6860 4720 50  0000 L CNN
F 1 "100n" H 6860 4570 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Disc_D6_P5" H 6850 4650 50  0001 C CNN
F 3 "" H 6850 4650 50  0000 C CNN
	1    6850 4650
	0    -1   -1   0   
$EndComp
$Comp
L GND #PWR011
U 1 1 590D1631
P 7100 5050
F 0 "#PWR011" H 7100 4800 50  0001 C CNN
F 1 "GND" H 7100 4900 50  0000 C CNN
F 2 "" H 7100 5050 50  0000 C CNN
F 3 "" H 7100 5050 50  0000 C CNN
	1    7100 5050
	1    0    0    -1  
$EndComp
Wire Wire Line
	7100 4650 7100 4750
Wire Wire Line
	6950 4650 7250 4650
Connection ~ 7100 4650
$Comp
L R R12
U 1 1 590D163A
P 6900 4200
F 0 "R12" V 6980 4200 50  0000 C CNN
F 1 "2K2" V 6900 4200 50  0000 C CNN
F 2 "scimpy_library:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal" V 6830 4200 50  0001 C CNN
F 3 "" H 6900 4200 50  0000 C CNN
	1    6900 4200
	0    1    1    0   
$EndComp
$Comp
L R R13
U 1 1 590D1641
P 7750 4200
F 0 "R13" V 7830 4200 50  0000 C CNN
F 1 "2K2" V 7750 4200 50  0000 C CNN
F 2 "scimpy_library:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal" V 7680 4200 50  0001 C CNN
F 3 "" H 7750 4200 50  0000 C CNN
	1    7750 4200
	0    1    1    0   
$EndComp
Wire Wire Line
	6600 4650 6600 4200
Wire Wire Line
	6600 4200 6750 4200
Connection ~ 6600 4650
Wire Wire Line
	7050 4200 7600 4200
Wire Wire Line
	7250 4450 7100 4450
Wire Wire Line
	7100 4450 7100 4200
Connection ~ 7100 4200
Wire Wire Line
	7850 4550 9000 4550
Wire Wire Line
	7900 4200 7950 4200
Wire Wire Line
	7950 4200 7950 4550
Connection ~ 7950 4550
$Comp
L GND #PWR012
U 1 1 590D1654
P 5950 2500
F 0 "#PWR012" H 5950 2250 50  0001 C CNN
F 1 "GND" H 5950 2350 50  0000 C CNN
F 2 "" H 5950 2500 50  0000 C CNN
F 3 "" H 5950 2500 50  0000 C CNN
	1    5950 2500
	1    0    0    -1  
$EndComp
Wire Wire Line
	3900 3650 3900 4750
Wire Wire Line
	4450 3450 4450 3900
Wire Wire Line
	4450 3900 8900 3900
Wire Wire Line
	4350 3000 4350 2850
Wire Wire Line
	3900 2750 3900 1650
Wire Wire Line
	3900 1650 9000 1650
Text Label 8100 4550 0    60   ~ 0
right_tweet
Text Label 8100 1650 0    60   ~ 0
left_bass
Text Label 8100 2650 0    60   ~ 0
left_tweet
Text Label 8100 3900 0    60   ~ 0
right_bass
$Comp
L GND #PWR013
U 1 1 590D52C7
P 2000 4300
F 0 "#PWR013" H 2000 4050 50  0001 C CNN
F 1 "GND" H 2000 4150 50  0000 C CNN
F 2 "" H 2000 4300 50  0000 C CNN
F 3 "" H 2000 4300 50  0000 C CNN
	1    2000 4300
	1    0    0    -1  
$EndComp
$Comp
L +15V #PWR014
U 1 1 590D6603
P 2500 3050
F 0 "#PWR014" H 2500 2900 50  0001 C CNN
F 1 "+15V" H 2500 3190 50  0000 C CNN
F 2 "" H 2500 3050 50  0000 C CNN
F 3 "" H 2500 3050 50  0000 C CNN
	1    2500 3050
	1    0    0    -1  
$EndComp
$Comp
L -15V #PWR16
U 1 1 590D6717
P 2500 4050
F 0 "#PWR16" H 2500 4150 50  0001 C CNN
F 1 "-15V" H 2500 4200 50  0000 C CNN
F 2 "" H 2500 4050 50  0000 C CNN
F 3 "" H 2500 4050 50  0000 C CNN
	1    2500 4050
	-1   0    0    1   
$EndComp
$Comp
L +15V #PWR015
U 1 1 590D680B
P 5750 2200
F 0 "#PWR015" H 5750 2050 50  0001 C CNN
F 1 "+15V" H 5750 2340 50  0000 C CNN
F 2 "" H 5750 2200 50  0000 C CNN
F 3 "" H 5750 2200 50  0000 C CNN
	1    5750 2200
	1    0    0    -1  
$EndComp
$Comp
L -15V #PWR13
U 1 1 590D6882
P 5750 3450
F 0 "#PWR13" H 5750 3550 50  0001 C CNN
F 1 "-15V" H 5750 3600 50  0000 C CNN
F 2 "" H 5750 3450 50  0000 C CNN
F 3 "" H 5750 3450 50  0000 C CNN
	1    5750 3450
	-1   0    0    1   
$EndComp
$Comp
L CONN_01X07 P1
U 1 1 590D272F
P 9600 2700
F 0 "P1" H 9600 3100 50  0000 C CNN
F 1 "CONN_01X07" V 9700 2700 50  0000 C CNN
F 2 "Socket_Strips:Socket_Strip_Angled_1x07" H 9600 2700 50  0001 C CNN
F 3 "" H 9600 2700 50  0000 C CNN
F 4 "22-16-2070" H 9600 2700 60  0001 C CNN "manf#"
	1    9600 2700
	1    0    0    -1  
$EndComp
Wire Wire Line
	9400 3000 9000 3000
Wire Wire Line
	9000 3000 9000 4550
Wire Wire Line
	8900 3900 8900 2900
Wire Wire Line
	8900 2900 9400 2900
Wire Wire Line
	9400 2800 8900 2800
Wire Wire Line
	8900 2800 8900 2650
Wire Wire Line
	9000 1650 9000 2700
Wire Wire Line
	9000 2700 9400 2700
$Comp
L +15V #PWR016
U 1 1 590D2B76
P 9100 2200
F 0 "#PWR016" H 9100 2050 50  0001 C CNN
F 1 "+15V" H 9100 2340 50  0000 C CNN
F 2 "" H 9100 2200 50  0000 C CNN
F 3 "" H 9100 2200 50  0000 C CNN
	1    9100 2200
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR017
U 1 1 590D2BED
P 9100 2450
F 0 "#PWR017" H 9100 2200 50  0001 C CNN
F 1 "GND" H 9100 2300 50  0000 C CNN
F 2 "" H 9100 2450 50  0000 C CNN
F 3 "" H 9100 2450 50  0000 C CNN
	1    9100 2450
	1    0    0    -1  
$EndComp
$Comp
L -15V #PWR3
U 1 1 590D2CDA
P 9100 2250
F 0 "#PWR3" H 9100 2350 50  0001 C CNN
F 1 "-15V" H 9100 2400 50  0000 C CNN
F 2 "" H 9100 2250 50  0000 C CNN
F 3 "" H 9100 2250 50  0000 C CNN
	1    9100 2250
	-1   0    0    1   
$EndComp
Wire Wire Line
	9100 2450 9250 2450
Wire Wire Line
	9250 2450 9250 2600
Wire Wire Line
	9250 2600 9400 2600
Wire Wire Line
	9400 2500 9300 2500
Wire Wire Line
	9300 2500 9300 2250
Wire Wire Line
	9300 2250 9100 2250
Wire Wire Line
	9100 2200 9350 2200
Wire Wire Line
	9350 2200 9350 2400
Wire Wire Line
	9350 2400 9400 2400
$Comp
L POT_Dual no_value1
U 1 1 59125A0A
P 1250 4150
F 0 "no_value1" H 1410 4460 50  0000 C CNN
F 1 "connector_dual_pot" H 1250 4250 50  0000 C CNN
F 2 "" H 1250 4150 50  0001 C CNN
F 3 "http://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocNm=640456&DocType=Customer+Drawing&DocLang=English" H 1250 4150 50  0001 C CNN
F 4 "3-643815-6" H 1250 4150 60  0001 C CNN "manf#"
	1    1250 4150
	0    1    1    0   
$EndComp
$Comp
L R R2
U 1 1 590D1592
P 6050 2000
F 0 "R2" V 6130 2000 50  0000 C CNN
F 1 "2K2" V 6050 2000 50  0000 C CNN
F 2 "scimpy_library:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal" V 5980 2000 50  0001 C CNN
F 3 "" H 6050 2000 50  0000 C CNN
	1    6050 2000
	0    1    1    0   
$EndComp
$EndSCHEMATC
