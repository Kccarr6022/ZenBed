from zenbedclass import ZenBed
class Motor(ZenBed):
    def __init__(self, motorx, motory):
        self.MotorLocationXmax = 10
        self.MotorLocationYmax = 10
        self.MotorLocationX = motorx #Location of x value (int)\character value 0=A
        self.MotorLocationY = motory #Location of y value (int)
        
        pass
    
        """
        The following algorithm is designed to turn on the specific motor in the array.
        """
        
    def MotorOn(self): # Error
        if 0 < self.MotorLocationX < 10: #Checks what PCI to call from
           if 0 < self.MotorLocationY < 10:
                MotorBoard.channels[MotorLocationX].duty_cycle = 0xfffe
                print("Works")
    
        pass 
    
    def MotorHalfOn(self):
        if 0 < self.MotorLocationX < 10: #Checks what PCI to call from
           if 0 < self.MotorLocationY < 10:
                MotorBoard.channels[self.MotorLocationX].duty_cycle = 0x7fff
    
        pass
    
    def MotorOff(self):
        if 0 < self.MotorLocationX < 10: #Checks what PCI to call from
           if 0 < self.MotorLocationY < 10:
                MotorBoard.channels[self.MotorLocationX].duty_cycle = 0
    
        pass
        
    def MotorOn(self, PercentPower):
        if 0 < self.MotorLocationX < 10: #Checks what PCI to call from
           if 0 < self.MotorLocationY < 10:
                MotorBoard.channels[MotorLocationX].duty_cycle = PercentPower * 0x7fff
                print("Works")
    
        pass 
