from classes.patternclass import Pattern

# Imported pattern 1 -> rectangle
rectangle = Pattern()
rectangle.time = 0.1
rectangle.rate_of_change = 1
rectangle.max_power = 50
rectangle.start_power = 10
rectangle.percent_power = 100
rectangle.sequence = """D4 E4, D5 E5, D6 E6, D7 E7, D8 E8, D9 E9, D10 E10, D11 E11, D12 E12, D13 E13,
            D14 E14, D15 E15, D16 D17 E16 E17, F16 F17, G16 G17, H16 H17 I16 I17, H15 I15,
            H14 I14, H13 I13, H12 I12, H11 I11, H10 I10, H9 I9, H8 I8, H7 I7, H6 I6, H5 I5,
            H4 I4, H3 I3 H2 I2, G2 G3, F2 F3, D2 E2 D3 E3"""

# Imported pattern 2 -> expanding_circle
expanding_circle = Pattern()
expanding_circle.time = 0.1
expanding_circle.rate_of_change = 5
expanding_circle.max_power = 50
expanding_circle.start_power = 10
expanding_circle.percent_power = 100
expanding_circle.sequence = """F7 G7, F6 G6 F8 G8, E5 E6 E7 E8 E9 F5 F9 G5 G9 H5 H6 H7 H8 H9, D4 D5 D6 D7 D8 D9 D10 D11
E4 E10 E11 F4 F10 F11 G4 G10 G11 H4 H10 H11 I4 I5 I6 I7 I8 I9 I10 I11, B2 B3 B4 B5 B6 B7
B8 B9 B10 B11 B12 B13 C3 C12 C13 D3 D12 D13 E3 E12 E13 F3 F12 F13 G3 G12 G13 H3 H12 H13
I3 I12 I13 J3 J4 J5 J6 J7 J8 J9 J10 J11 J12 J13, B2 B3 B4 B5 B6 B7 B8 B9 B10 B11 B12 B13
B14 B15 C2 C14 C15 D2 D14 D15 E2 E14 E15 F2 F14 F15 G2 G14 G15 H2 H14 H15 I2 I14 I15 J2
J14 J15 K2 K3 K4 K5 K6 K7 K8 K9 K10 K11 K12 K13 K14 K15
"""
