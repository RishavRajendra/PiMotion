from .i2c import I2C
import time

addr = 0x60
regH = 0x02
regL = 0x03 

mag = I2C()
def readAngle():
    angleH = hex(mag._readRegister(addr,regH))
    angleL = hex(mag._readRegister(addr,regL))
    bearing = int(angleH,16)*0x100+int(angleL,16)
    print("Current bearing is ", bearing/10)
    return bearing/10