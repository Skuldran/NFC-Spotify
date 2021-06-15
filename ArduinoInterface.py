from smbus2 import SMBus

class ArduinoInterface:

    address = 69 #nice

    def __init__(self):
        self.bus = SMBus(1)

    def setColor(self, col):
        
        if col == 'red':
            vals = [255, 0, 0]
        elif col == 'green':
            vals = [0, 255, 0]
        elif col=='blue':
            vals = [0, 0, 255]
        elif col=='yellow':
            vals = [220, 220, 60]
        else:
            vals = [50, 50, 50]
        
        self.bus.write_i2c_block_data(self.address, 0, vals);
            
        
    def buttonPressed(self):
         return (self.bus.read_byte_data(self.address, 0) == 1);
