from smbus2 import SMBus

class ArduinoInterface:

    adress = 69 #nice

    def __init__(self):
        self.bus = SMBus(1)

    def setColor(self, col):
        
        switch(col) {
            case 'red': bytes = [255, 0, 0]; break;
            case 'green': bytes = [0, 255, 0]; break;
            case 'blue': bytes = [0, 0, 255]; break;
        }
        
        bus.write_i2c_block_data(adress, 0, bytes);
            
        
    def buttonPressed(self):
         return (bus.read_byte_data(adress, 0) == 1);
