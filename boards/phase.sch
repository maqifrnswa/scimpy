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
LIBS:audio
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
LIBS:crossover-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 2 2
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L TL074 U6
U 1 1 59009CED
P 4000 2000
F 0 "U6" H 4000 2200 50  0000 L CNN
F 1 "TL074" H 4000 1800 50  0000 L CNN
F 2 "Housings_DIP:DIP-14_W7.62mm" H 3950 2100 50  0000 C CNN
F 3 "" H 4050 2200 50  0000 C CNN
	1    4000 2000
	1    0    0    -1  
$EndComp
$Comp
L +12V #PWR044
U 1 1 5900A021
P 3900 1450
F 0 "#PWR044" H 3900 1300 50  0001 C CNN
F 1 "+12V" H 3900 1590 50  0000 C CNN
F 2 "" H 3900 1450 50  0000 C CNN
F 3 "" H 3900 1450 50  0000 C CNN
	1    3900 1450
	1    0    0    -1  
$EndComp
$Comp
L C_Small C50
U 1 1 58FFF56B
P 4100 2600
F 0 "C50" H 4110 2670 50  0000 L CNN
F 1 "100n" H 4110 2520 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Disc_D3_P2.5" H 4100 2600 50  0001 C CNN
F 3 "" H 4100 2600 50  0000 C CNN
	1    4100 2600
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR045
U 1 1 58FFF572
P 4100 2700
F 0 "#PWR045" H 4100 2450 50  0001 C CNN
F 1 "GND" H 4100 2550 50  0000 C CNN
F 2 "" H 4100 2700 50  0000 C CNN
F 3 "" H 4100 2700 50  0000 C CNN
	1    4100 2700
	1    0    0    -1  
$EndComp
$Comp
L -12V #PWR53
U 1 1 58FFF578
P 3900 2700
F 0 "#PWR53" H 3900 2800 50  0001 C CNN
F 1 "-12V" H 3900 2850 50  0000 C CNN
F 2 "" H 3900 2700 50  0000 C CNN
F 3 "" H 3900 2700 50  0000 C CNN
	1    3900 2700
	-1   0    0    1   
$EndComp
Wire Wire Line
	3900 2300 3900 2700
$Comp
L C_Small C48
U 1 1 58FFF59A
P 4100 1650
F 0 "C48" H 4110 1720 50  0000 L CNN
F 1 "100n" H 4110 1570 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Disc_D3_P2.5" H 4100 1650 50  0001 C CNN
F 3 "" H 4100 1650 50  0000 C CNN
	1    4100 1650
	1    0    0    -1  
$EndComp
Wire Wire Line
	3900 1550 4100 1550
Connection ~ 3900 1550
Wire Wire Line
	3900 2500 4100 2500
Connection ~ 3900 2500
Text Notes 400  550  0    60   ~ 0
http://www.linkwitzlab.com/models.htm#E\n\nall pass filters gives delay = 2 RC\nfor f < f0 = 1/(2pi R C)\nNeed f0 > cross-over freq\ntypically need at least 2 stages to get\nf0 > cross-over freq and enough delay\n\ntg = 2RC/(1+(f*RC*2pi)^2)\ntg = 1/(pi*f_0)* 1/(1+(f/f_0)^2)
$Comp
L R R38
U 1 1 58FFFCDA
P 3550 2300
F 0 "R38" V 3630 2300 50  0000 C CNN
F 1 "Rph" V 3550 2300 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM7mm" V 3480 2300 50  0001 C CNN
F 3 "" H 3550 2300 50  0000 C CNN
	1    3550 2300
	-1   0    0    1   
$EndComp
$Comp
L C_Small C49
U 1 1 58FFFCE1
P 3300 2100
F 0 "C49" H 3310 2170 50  0000 L CNN
F 1 "100n" H 3310 2020 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Disc_D6_P5" H 3300 2100 50  0001 C CNN
F 3 "" H 3300 2100 50  0000 C CNN
	1    3300 2100
	0    -1   -1   0   
$EndComp
$Comp
L GND #PWR046
U 1 1 58FFFCE8
P 3550 2450
F 0 "#PWR046" H 3550 2200 50  0001 C CNN
F 1 "GND" H 3550 2300 50  0000 C CNN
F 2 "" H 3550 2450 50  0000 C CNN
F 3 "" H 3550 2450 50  0000 C CNN
	1    3550 2450
	1    0    0    -1  
$EndComp
Wire Wire Line
	2500 2100 3200 2100
Wire Wire Line
	3550 2100 3550 2150
Wire Wire Line
	3500 2100 3700 2100
Connection ~ 3550 2100
Wire Wire Line
	3900 1700 3900 1450
$Comp
L R R1
U 1 1 58FFFD5A
P 3350 1250
F 0 "R1" V 3430 1250 50  0000 C CNN
F 1 "2K2" V 3350 1250 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM7mm" V 3280 1250 50  0001 C CNN
F 3 "" H 3350 1250 50  0000 C CNN
	1    3350 1250
	0    1    1    0   
$EndComp
$Comp
L R R37
U 1 1 58FFFDB5
P 4200 1250
F 0 "R37" V 4280 1250 50  0000 C CNN
F 1 "2K2" V 4200 1250 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM7mm" V 4130 1250 50  0001 C CNN
F 3 "" H 4200 1250 50  0000 C CNN
	1    4200 1250
	0    1    1    0   
$EndComp
Wire Wire Line
	3050 2100 3050 1250
Wire Wire Line
	3050 1250 3200 1250
Connection ~ 3050 2100
Wire Wire Line
	3500 1250 4050 1250
Wire Wire Line
	3700 1900 3550 1900
Wire Wire Line
	3550 1900 3550 1250
Connection ~ 3550 1250
Wire Wire Line
	4300 2000 4900 2000
Wire Wire Line
	4350 1250 4400 1250
Wire Wire Line
	4400 1250 4400 2000
Connection ~ 4400 2000
Text HLabel 2500 2100 0    60   Input ~ 0
right_tweeter_in
Text HLabel 6600 1900 2    60   Input ~ 0
right_tweeter_out
Wire Wire Line
	3400 2100 3550 2100
Text Notes 3800 200  0    60   ~ 0
high pass b/c it's for tweeter\nthis way high freq see no phase shift\nBut you want a constant delay over cross-over region\nso maybe f0 > 2 fc?\nfc = 1 kHz crossover\nf0 = 2 khz\ndelay = 127 microsec
Text Notes 7150 350  0    60   ~ 0
How much delay do you want?\nRC = \frac{ 1 \pm \sqrt{1-(tg*\omega_c)^2} }{t_g (\omega_c^2)}\ntake the smaller one so f0 is bigger!\nfor two stage, make each stage give you t_g/2 delay\nexample: 150 us delay desired, each stage gets 75 us\nRC = 6.36e-4, 3.99e-5\nassume C = 100 nF\nRph = 6.36 kOhm, 399 Ohm\nsmaller one will give flattest response over cross-over region, use that
$Comp
L TL074 U6
U 2 1 59010294
P 5700 1900
F 0 "U6" H 5700 2100 50  0000 L CNN
F 1 "TL074" H 5700 1700 50  0000 L CNN
F 2 "" H 5650 2000 50  0000 C CNN
F 3 "" H 5750 2100 50  0000 C CNN
	2    5700 1900
	1    0    0    -1  
$EndComp
$Comp
L R R41
U 1 1 590102BD
P 5250 2200
F 0 "R41" V 5330 2200 50  0000 C CNN
F 1 "Rph" V 5250 2200 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM7mm" V 5180 2200 50  0001 C CNN
F 3 "" H 5250 2200 50  0000 C CNN
	1    5250 2200
	-1   0    0    1   
$EndComp
$Comp
L C_Small C51
U 1 1 590102C3
P 5000 2000
F 0 "C51" H 5010 2070 50  0000 L CNN
F 1 "100n" H 5010 1920 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Disc_D6_P5" H 5000 2000 50  0001 C CNN
F 3 "" H 5000 2000 50  0000 C CNN
	1    5000 2000
	0    -1   -1   0   
$EndComp
$Comp
L GND #PWR047
U 1 1 590102C9
P 5250 2350
F 0 "#PWR047" H 5250 2100 50  0001 C CNN
F 1 "GND" H 5250 2200 50  0000 C CNN
F 2 "" H 5250 2350 50  0000 C CNN
F 3 "" H 5250 2350 50  0000 C CNN
	1    5250 2350
	1    0    0    -1  
$EndComp
Wire Wire Line
	5250 2000 5250 2050
Wire Wire Line
	5200 2000 5400 2000
Connection ~ 5250 2000
$Comp
L R R39
U 1 1 590102D4
P 5050 1150
F 0 "R39" V 5130 1150 50  0000 C CNN
F 1 "2K2" V 5050 1150 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM7mm" V 4980 1150 50  0001 C CNN
F 3 "" H 5050 1150 50  0000 C CNN
	1    5050 1150
	0    1    1    0   
$EndComp
$Comp
L R R40
U 1 1 590102DA
P 5900 1150
F 0 "R40" V 5980 1150 50  0000 C CNN
F 1 "2K2" V 5900 1150 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM7mm" V 5830 1150 50  0001 C CNN
F 3 "" H 5900 1150 50  0000 C CNN
	1    5900 1150
	0    1    1    0   
$EndComp
Wire Wire Line
	4750 2000 4750 1150
Wire Wire Line
	4750 1150 4900 1150
Connection ~ 4750 2000
Wire Wire Line
	5200 1150 5750 1150
Wire Wire Line
	5400 1800 5250 1800
Wire Wire Line
	5250 1800 5250 1150
Connection ~ 5250 1150
Wire Wire Line
	6000 1900 6600 1900
Wire Wire Line
	6050 1150 6100 1150
Wire Wire Line
	6100 1150 6100 1900
Connection ~ 6100 1900
Wire Wire Line
	5100 2000 5250 2000
$Comp
L TL074 U6
U 3 1 59011051
P 4000 3900
F 0 "U6" H 4000 4100 50  0000 L CNN
F 1 "TL074" H 4000 3700 50  0000 L CNN
F 2 "" H 3950 4000 50  0000 C CNN
F 3 "" H 4050 4100 50  0000 C CNN
	3    4000 3900
	1    0    0    -1  
$EndComp
$Comp
L R R47
U 1 1 5901107A
P 3550 4200
F 0 "R47" V 3630 4200 50  0000 C CNN
F 1 "Rph" V 3550 4200 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM7mm" V 3480 4200 50  0001 C CNN
F 3 "" H 3550 4200 50  0000 C CNN
	1    3550 4200
	-1   0    0    1   
$EndComp
$Comp
L C_Small C53
U 1 1 59011080
P 3300 4000
F 0 "C53" H 3310 4070 50  0000 L CNN
F 1 "100n" H 3310 3920 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Disc_D6_P5" H 3300 4000 50  0001 C CNN
F 3 "" H 3300 4000 50  0000 C CNN
	1    3300 4000
	0    -1   -1   0   
$EndComp
$Comp
L GND #PWR048
U 1 1 59011086
P 3550 4350
F 0 "#PWR048" H 3550 4100 50  0001 C CNN
F 1 "GND" H 3550 4200 50  0000 C CNN
F 2 "" H 3550 4350 50  0000 C CNN
F 3 "" H 3550 4350 50  0000 C CNN
	1    3550 4350
	1    0    0    -1  
$EndComp
Wire Wire Line
	2500 4000 3200 4000
Wire Wire Line
	3550 4000 3550 4050
Wire Wire Line
	3500 4000 3700 4000
Connection ~ 3550 4000
$Comp
L R R44
U 1 1 59011091
P 3350 3150
F 0 "R44" V 3430 3150 50  0000 C CNN
F 1 "2K2" V 3350 3150 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM7mm" V 3280 3150 50  0001 C CNN
F 3 "" H 3350 3150 50  0000 C CNN
	1    3350 3150
	0    1    1    0   
$EndComp
$Comp
L R R45
U 1 1 59011097
P 4200 3150
F 0 "R45" V 4280 3150 50  0000 C CNN
F 1 "2K2" V 4200 3150 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM7mm" V 4130 3150 50  0001 C CNN
F 3 "" H 4200 3150 50  0000 C CNN
	1    4200 3150
	0    1    1    0   
$EndComp
Wire Wire Line
	3050 4000 3050 3150
Wire Wire Line
	3050 3150 3200 3150
Connection ~ 3050 4000
Wire Wire Line
	3500 3150 4050 3150
Wire Wire Line
	3700 3800 3550 3800
Wire Wire Line
	3550 3800 3550 3150
Connection ~ 3550 3150
Wire Wire Line
	4300 3900 4900 3900
Wire Wire Line
	4350 3150 4400 3150
Wire Wire Line
	4400 3150 4400 3900
Connection ~ 4400 3900
Text HLabel 2500 4000 0    60   Input ~ 0
left_tweeter_in
Text HLabel 6600 3800 2    60   Input ~ 0
left_tweeter_out
Wire Wire Line
	3400 4000 3550 4000
$Comp
L TL074 U6
U 4 1 590110AB
P 5700 3800
F 0 "U6" H 5700 4000 50  0000 L CNN
F 1 "TL074" H 5700 3600 50  0000 L CNN
F 2 "" H 5650 3900 50  0000 C CNN
F 3 "" H 5750 4000 50  0000 C CNN
	4    5700 3800
	1    0    0    -1  
$EndComp
$Comp
L R R46
U 1 1 590110D4
P 5250 4100
F 0 "R46" V 5330 4100 50  0000 C CNN
F 1 "Rph" V 5250 4100 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM7mm" V 5180 4100 50  0001 C CNN
F 3 "" H 5250 4100 50  0000 C CNN
	1    5250 4100
	-1   0    0    1   
$EndComp
$Comp
L C_Small C52
U 1 1 590110DA
P 5000 3900
F 0 "C52" H 5010 3970 50  0000 L CNN
F 1 "100n" H 5010 3820 50  0000 L CNN
F 2 "Capacitors_ThroughHole:C_Disc_D6_P5" H 5000 3900 50  0001 C CNN
F 3 "" H 5000 3900 50  0000 C CNN
	1    5000 3900
	0    -1   -1   0   
$EndComp
$Comp
L GND #PWR049
U 1 1 590110E0
P 5250 4250
F 0 "#PWR049" H 5250 4000 50  0001 C CNN
F 1 "GND" H 5250 4100 50  0000 C CNN
F 2 "" H 5250 4250 50  0000 C CNN
F 3 "" H 5250 4250 50  0000 C CNN
	1    5250 4250
	1    0    0    -1  
$EndComp
Wire Wire Line
	5250 3900 5250 3950
Wire Wire Line
	5200 3900 5400 3900
Connection ~ 5250 3900
$Comp
L R R42
U 1 1 590110EA
P 5050 3050
F 0 "R42" V 5130 3050 50  0000 C CNN
F 1 "2K2" V 5050 3050 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM7mm" V 4980 3050 50  0001 C CNN
F 3 "" H 5050 3050 50  0000 C CNN
	1    5050 3050
	0    1    1    0   
$EndComp
$Comp
L R R43
U 1 1 590110F0
P 5900 3050
F 0 "R43" V 5980 3050 50  0000 C CNN
F 1 "2K2" V 5900 3050 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM7mm" V 5830 3050 50  0001 C CNN
F 3 "" H 5900 3050 50  0000 C CNN
	1    5900 3050
	0    1    1    0   
$EndComp
Wire Wire Line
	4750 3900 4750 3050
Wire Wire Line
	4750 3050 4900 3050
Connection ~ 4750 3900
Wire Wire Line
	5200 3050 5750 3050
Wire Wire Line
	5400 3700 5250 3700
Wire Wire Line
	5250 3700 5250 3050
Connection ~ 5250 3050
Wire Wire Line
	6000 3800 6600 3800
Wire Wire Line
	6050 3050 6100 3050
Wire Wire Line
	6100 3050 6100 3800
Connection ~ 6100 3800
Wire Wire Line
	5100 3900 5250 3900
$Comp
L GND #PWR050
U 1 1 590200E6
P 4100 1750
F 0 "#PWR050" H 4100 1500 50  0001 C CNN
F 1 "GND" H 4100 1600 50  0000 C CNN
F 2 "" H 4100 1750 50  0000 C CNN
F 3 "" H 4100 1750 50  0000 C CNN
	1    4100 1750
	1    0    0    -1  
$EndComp
$EndSCHEMATC
