

import machine
i2c = machine.i2C(machine.Pin('SCL'). machine.Pin('SDA'))
i2c.int()


import (servo)
servo = (servo.Servos(i2c))

#pca = pca9685.PCA9685(i2c)

