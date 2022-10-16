from classes.patternclass import Pattern

# Imported pattern 1 -> rectangle
rectangle = Pattern()
rectangle.name = "rectangle"
rectangle.time = 0.3
rectangle.hold = 0; # Hold set to false
rectangle.rate_of_change = 3
rectangle.max_power = 18
rectangle.start_power = 6
rectangle.percent_power = 100
rectangle.sequence = """D4 E4, D5 E5, D6 E6, D7 E7, D8 E8, D9 E9, D10 E10, D11 E11, D12 E12, D13 E13,
D14 E14, D15 E15, D16 D17 E16 E17, F16 F17, G16 G17, H16 H17 I16 I17, H15 I15, H14 I14,
H13 I13, H12 I12, H11 I11, H10 I10, H9 I9, H8 I8, H7 I7, H6 I6, H5 I5, H4 I4, H3 I3 H2 I2,
G2 G3, F2 F3, D2 E2 D3 E3"""

# Imported pattern 2 -> expanding_circle
expanding_circle = Pattern()
expanding_circle.name = "expanding_circle"
expanding_circle.time = 0.3
expanding_circle.hold = 0; # hold set to false
expanding_circle.rate_of_change = 3
expanding_circle.max_power = 18
expanding_circle.start_power = 9
expanding_circle.percent_power = 100
expanding_circle.sequence = """F9 G9   ,  F8 G8 F10  G10  ,G7 F7 E7 E9 E8 H7 H8 H9 H10  E10  E11 F11 G11 H11 ,H6 G6 F6 E6 E12 F12 G12 H12 ,I5 H5 G5 F5 E5 D5 D6 D7 D8 D9 D10  D11 D12 D13 E13 F13 G13 H13 I13 I12 I11 I10  I9 I8 I7 I6 ,J12 J11 J10  J9 J8 J7 J6 J5 C5 C6 C7 C8 C9 C10  C11 C12 C13 J4 I4 H4 C4 D4 E4 F4 G4 C14 D14 E14 F14 G14 H14 I14 J14 J13 , B3 B4 B5 B6 B7 B8 B9 B11 B12 B13 B14 B15   C15   D15   E15   F15   G15   H15   I15   J15   K4 K5 K6 K7 K8 K9 K11 K12 K13 K14 K15 B10  K10   C3 D3 E3 F3 G3 H3 I3 J3 K3 ,K16 J16 I16 H16 G16 F16 E16 D16 C16 B16 B2 C2 D2 E2 F2 G2 H2 I2 J2 K2 ,A1 A2 A3 A4 A5 A6 A7 A8 A9 A11 A12 A13 A14 A15 A16 A17 A18 B1  B17 B18 C1  C17 C18 D1  D17 D18 E1  E17 E18 F1  F17 F18 G1  G17 G18 H1  H17 H18 I1  I17 I18 J1  J17 J18 K1  K17 K18 L1 L2 L3 L4 L5 L6 L7 L8 L9 L11 L12 L13 L14 L15 L16 L17 L10  A10    L18
"""
#F7 G7, F6 G6 F8 G8, E5 E6 E7 E8 E9 F5 F9 G5 G9 H5 H6 H7 H8 H9, D4 D5
#D6 D7 D8 D9 D10 D11 E4 E10 E11 F4 F10 F11 G4 G10 G11 H4 H10 H11 I4 I5 I6 I7 I8 I9 I10 I11, C3 C4
#C5 C6 C7 C8 C9 C10 C11 C12 C13 D3 D12 D13 E3 E12 E13 F3 F12 F13 G3 G12 G13 H3 H12 H13I3 I12 I13 J3
#J4 J5 J6 J7 J8 J9 J10 J11 J12 J13, B2 B3 B4 B5 B6 B7 B8 B9 B10 B11 B12 B13 B14 B15 C2 C14 C15 D2
#D14 D15 E2 E14 E15 F2 F14 F15 G2 G14 G15 H2 H14 H15 I2 I14 I15 J2 J14 J15 K2 K3 K4 K5 K6 K7 K8 K9
#K10 K11 K12 K13 K14 K15, A1 A2 A3 A4 A5 A6 A7 A8 A9 A10 A11 A12 A13 A14 A15 A16 A17 A18 B1 B16 B17
#B18 C1 C16 C17 C18 D1 D16 D17 D18 E1 E16 E17 E18 F1 F16 F17 F18 G1 G16 G17 G18 H1 H16 H17 H18 I1 I16
#I17 I18 J1 J16 J17 J18 K1 K16 K17 K18 L1 L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13 L14 L15 L16 L17 L18


# Imported pattern 3 -> goacross
goacross = Pattern()
goacross.name = "goacross"
goacross.time = 0.1
goacross.hold = 0; # hold set to false
goacross.rate_of_change = 5
goacross.max_power = 50
goacross.start_power = 15
goacross.percent_power = 100
goacross.sequence = """A1 A2, B1 B2, C1 C2, D1 D2, E1 E2, F1 F2, G1 G2, H1 H2, I1 I2, J1 J2, K1 K2,
L1 L2, L3 L4, K3 K4, J3 J4, I3 I4, H3 H4, G3 G4, F3 F4, E3 E4, D3 D4, C3 C4, B3 B4, A3 A4 A5 A6,
B5 B6, C5 C6, D5 D6, E5 E6, F5 F6, G5 G6, H5 H6, I5 I6, J5 J6, K5 K6, L5 L6 L7 L8, K7 K8, J7 J8,
I7 I8, H7 H8, G7 G8, F7 F8, E7 E8, D7 D8, C7 C8, B7 B8, A7 A8 A9 A10, B9 B10, C9 C10, D9 D10, E9
E10, F9 F10, G9 G10, H9 H10, I9 I10, J9 J10, K9 K10 L9 L10 L11 L12, K11 K12, J11 J12, I11 I12, H11
H12, G11 G12, F11 F12, E11 E12, D11 D12, C11 C12, B11 B12, A11 A12"""


# Imported pattern 4 -> flow
flow = Pattern()
flow.name = "flow"
flow.time = 0.3
flow.hold = 0; # hold set to false
flow.rate_of_change = 3
flow.max_power = 24
flow.start_power = 12
flow.percent_power = 100
flow.sequence = """A1 A2 A3 A4 A5 A6 A7 A8 A9 A10 A11 A12 A13 A14 A15 A16 A17 A18, B1 B2 B3 B4 B5 B6 B7 B8 B9 B10 B11 B12 B13 B14 B15 B16 B17 B18,
C1 C2 C3 C4 C5 C6 C7 C8 C9 C10 C11 C12 C13 C14 C15 C16 C17 C18, D1 D2 D3 D4 D5 D6 D7 D8 D9 D10 D11 D12 D13 D14 D15 D16 D17 D18,
E1 E2 E3 E4 E5 E6 E7 E8 E9 E10 E11 E12 E13 E14 E15 E16 E17 E18, F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 F12 F13 F14 F15 F16 F17 F18,
G1 G2 G3 G4 G5 G6 G7 G8 G9 G10 G11 G12 G13 G14 G15 G16 G17 G18, H1 H2 H3 H4 H5 H6 H7 H8 H9 H10 H11 H12 H13 H14 H15 H16 H17 H18,
I1 I2 I3 I4 I5 I6 I7 I8 I9 I10 I11 I12 I13 I14 I15 I16 I17 I18, J1 J2 J3 J4 J5 J6 J7 J8 J9 J10 J11 J12 J13 J14 J15 J16 J17 J18,
K1 K2 K3 K4 K5 K6 K7 K8 K9 K10 K11 K12 K13 K14 K15 K16 K17 K18, L1 L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13 L14 L15 L16 L17 L18"""

# K1 K2 K3 K4 K5 K6 K7 K8 K9 K10 K11 K12 K13 K14 K15 K16 K17 K18, J1 J2 J3 J4 J5 J6 J7 J8 J9 J10 J11 J12 J13 J14 J15 J16 J17 J18,
# I1 I2 I3 I4 I5 I6 I7 I8 I9 I10 I11 I12 I13 I14 I15 I16 I17 I18, H1 H2 H3 H4 H5 H6 H7 H8 H9 H10 H11 H12 H13 H14 H15 H16 H17 H18,
# G1 G2 G3 G4 G5 G6 G7 G8 G9 G10 G11 G12 G13 G14 G15 G16 G17 G18, F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 F12 F13 F14 F15 F16 F17 F18,
# E1 E2 E3 E4 E5 E6 E7 E8 E9 E10 E11 E12 E13 E14 E15 E16 E17 E18, D1 D2 D3 D4 D5 D6 D7 D8 D9 D10 D11 D12 D13 D14 D15 D16 D17 D18,
# C1 C2 C3 C4 C5 C6 C7 C8 C9 C10 C11 C12 C13 C14 C15 C16 C17 C18, B1 B2 B3 B4 B5 B6 B7 B8 B9 B10 B11 B12 B13 B14 B15 B16 B17 B18


# Work in progress
# Imported pattern 5 -> strobe
strobe = Pattern()
strobe.name = "strobe"
strobe.time = 0.5
strobe.hold = 0; # hold set to false
strobe.rate_of_change = 15
strobe.max_power = 30
strobe.start_power = 15
strobe.percent_power = 100
strobe.sequence = """G18 H18 I18, G17 H17 I17, G16 H16 I16, G18 H18 I18, G15 H15 I15 G16 H16 I16 G17 H17 I17, G14 H14 I14 G15 H15 I15 G16 H16 I16, G13 H13 I13 G14 H14 I14 G15 H15 I15""" 
#G12 H12 I12, G11 H11 I11, G10 H10 I10, G9 H9 I9, G8 H8 I8, G7 H7 I7, G6 H6 I6, G5 H5 I5, G4 H4 I4, G3 H3 I3, G2 H2 I2, G1 H1 I1"""


# Imported pattern 7 -> circle
circle = Pattern()
circle.name = "circle"
circle.time = 0.3
circle.hold = 0; # hold set to false
circle.rate_of_change = 3
circle.max_power = 24
circle.start_power = 12
circle.percent_power = 100
circle.sequence = """F3, E3 F4, E4, D4 D5 E5, C6 D6, C7 D7 B7, B8 C8 D8, D9 C9 B9, 
B10 C10 D10, C11 D11, C12 D12, D13 E13, D14 E14, E15, F15 E16, F16, G15, G14 H14, 
G13 H13, H12 I12, H11 I11, H10 I10 J10, J9 I9 H9, H8 I8 J8, H7 J7 I7, I6 H6, H5 G6, G5 G4 H4"""

# Imported pattern 8 -> leaf1
leaf1 = Pattern()
leaf1.name = "leaf1"
leaf1.time = 0.2
leaf1.hold = 0; # Hold set to false
leaf1.rate_of_change = 3
leaf1.max_power = 24
leaf1.start_power = 12
leaf1.percent_power = 100
leaf1.sequence = """D3, D4 E4, E5 F5 E6, F6 F7 G7 H7, H6 I6 I5, I4 J4, J3 K3, K4, J5,
J6 J7 I7 H8, G8 F8 E8 E7, D7 C7 C6, C5, D6, D8, E9 F9 F10, G10 G11 H10 H9 I9, J9 I8
J8, K8 K7, L6, L7, K9, J10 I10 I11, H11 H12 G12 F12 F11, E12 E11 D11 D10, C10 C9 D9,
C8 B8, B7, A7, A8 A9 B9, B10 B11 C11, C12 D12 D13 E13 F13, G13 H13 I13 I12 J12, J11 K11 K12,
K10, L9, L10, L11 K13, J13 J14, I14 I15 H15 G15, F15 F16 E15 D15, D14 C14 C15, B14 C13, B13,
B12 A12, A13 A14, A15 B15, B16 C16 C17 D17 E17, F17 G17 H17 H16 I16, J16 J15 K15 K14, L14,
L15 K16, J17, I17, I18, H18, F1 G1 G2, G3 F3 F2 E2"""

# Imported pattern 9 -> leaf2
leaf2 = Pattern()
leaf2.name = "leaf2"
leaf2.time = 0.2
leaf2.hold = 0; # Hold set to false
leaf2.rate_of_change = 3
leaf2.max_power = 24
leaf2.start_power = 9
leaf2.percent_power = 100
leaf2.sequence = """C2, C3 D3, D4 E4 E5, E6 F6 F5 G6, G5 H5 H6, H4 I4, I3, J2, J3, J4, J5 I5 I6, I7 H7 G7 G8,
F8 E8 E7 D7, C7 C6, C5 B5, B4, A4 A5, A6 B6, B7 B7 B8 C8, D9 E9 F9 F10, G10 G9 H9 I8, J8 J7,
K6, K7, K8 J9, I9 I10 H10, H11 G11 F11 E11 E12, D12 D11 C11, C10 B10 B9, A8, A7, A9 A10,
B11 B12 C12, D13 E13 F13 F12, G12 H12 I11, J11 J10 K10, K9, L8, L9 L10, K11 K12 J12,
I12 I13 H13 G14, G15 F15 F14 E14, D15 D14 C14, C13 B13, A12, A13, B14 B15, C15 C16 D16,
E16 E15 F16 G16, H16 H15 I15, I14 J14, K13, L12, L13 L14, K15 K16 J16, I17 H18 G18, G1 G2, F2, F3"""

# Imported pattern 10 -> duelrectangle
duelrectangle = Pattern()
duelrectangle.name = "duelrectangle"
duelrectangle.time = 0.2
duelrectangle.hold = 0; # Hold set to false
duelrectangle.rate_of_change = 3
duelrectangle.max_power = 21
duelrectangle.start_power = 9
duelrectangle.percent_power = 100
duelrectangle.sequence = """F3 G3, E3 H3, E4 H4, E5 H5, E6 H6, E7 H7, E8 H8, E9 H9, E10 H10,
E11 H11, E12 H12, E13 H13, E14 H14, E15 H15, E16 H16, F16 G16, F17 G17, F18 G18, F1 G1, F2 G2"""