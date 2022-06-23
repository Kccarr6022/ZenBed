
    """
    .percent() is redifined by range (0,100,0,pwrlvl)
        This makes things more universal and seemless when adjusting patterns
        Otherwise things like the width would be effected by adjusting the power
    """
def wave():
    for seq
        mtr[0](inc) #Starts the wave
        if mtr[x-1](inc) and mtr[x-1].percent()>=(width)
            mtr[x](inc)
        if mtr[x].percent()==pwrlvl
            mtr[x](dec)
            
#    set mtr[0-1] = max in seq range ie 35 in this example

def seq()
    for x in range (0,35)
#This is all of the motors that are being used in the pattern
#This assigns the motors a single motor number based on the order they will be called
#If motors are called together then they share the same motor number


"""Motor Functions"""
#cmtr = current mtr = mtr[x]
#i didnt know if i could use x twice

def inc():
    cmtr.percent(x+spd)
#     mtr[1](inc)
#     Motor 1 starts increasing in power

def dec():
    cmtr.percent(x-spd)
#     mtr[1](dec)
#     Motor 1 starts decreasing in power

    
def hld()
    Hold current power level
#     mtr[1](hld)
#     Motor 1 holds current power level
    
    
    
    """
    Adjustable Pattern Functions
    Speed/Width/Power
    """
    
def spd():
    roc()*(x)
#     x = 1 standard roc
#     x = .5 half standard roc
#     x = 2 double standard roc etc...
#     spd is just a multiplyer for roc
#     roc can be universal but speed is pattern specific
#     Adjusting this changes the speed that the pattern is exicuted
    
def width():
    ()
#     .percent(x)
#     x = amount of power previous mtr has to reach for cmtr to start inc

#     Adjusting this will change the amount of motors are on at the same time
#     Aka adjusting the width of the wave    
 
   
def pwrlvl():
    ()
#     .percent(x)
#     x = max amount of power motors go to
#     used by the rest of the code to decide


def roc(): #This will be master code and will not be adjusted per
    .percent(.5)/.1seconds
    #Rate of change
    #How fast a motor increases or decreases in power
    #Could be based on pca frequency instead of time





Basic conceptual example:

Set mtr0 to increasing by 10% per second
When mtr0 reaches 20%, set mtr1 to increasing by 10% per second
When mtr1 reaches 20%, set mtr2 to increasing by 10% per second
When mtr1 reaches 20%, set mtr2 to increasing by 10% per second
When mtr% = or > 90% 


When previous mtr reaches x%, then set current mtr to increasing
When current mtr reaches max power, then set to decreasing