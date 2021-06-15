from smbus2 import SMBus
import time

class ArduinoInterface:

    address = 69 #nice

    def __init__(self):
        self.bus = SMBus(1)
        time.sleep(1)
        print("Arduino communication initialized.")

    def setColor(self, col):
        if col == 'red':
            vals = [0xFF, 0x00, 0x00]
        elif col == 'green':
            vals = [0x00, 0xFF, 0x00]
        elif col=='blue':
            vals = [0x00, 0x00, 0xFF]
        elif col=='yellow':
            vals = [0xA0, 0x50, 0x10]
        else:
            vals = [0x80, 0x80, 0x80]
        
        self.bus.write_i2c_block_data(self.address, 0x00, vals);
        
    def buttonPressed(self):
        time.sleep(0.1);
        button = self.bus.read_byte(self.address);
        return (button == 1);
