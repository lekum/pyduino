import unittest
import random
from pyduino import Arduino

class Arduino_Mock(Arduino):
    """
    Mocks the Arduino object
    Proxies the write() and readline() calls to an Arduino_Connection_Mock
    """

    def __init__(self):
        self.conn = Arduino_Connection_Mock()

class Arduino_Connection_Mock():
    """
    Mock of the Arduino connection
    
    Simulates the serial interface  to the arduino_sketch
    """

    def __init__(self):
        self.last_written = None

    def write(self, value_to_write):
        """
        Simulates writing to the Arduino via the USB connection
        """
        self.last_written = value_to_write
    
    def readline(self):
        """
        Simulates reading the value returned from Arduino via the USB connection
        The output depends on the previous last_written value
        The values of the pins are static 
        """
        if self.last_written == b'RD0':
            return b'D0:0'
        elif self.last_written == b'RD1':
            return b'D1:1'
        elif self.last_written == b'RD2':
            return b'D2:0'
        elif self.last_written == b'RD3':
            return b'D3:1'
        elif self.last_written == b'RD4':
            return b'D4:0'
        elif self.last_written == b'RD5':
            return b'D5:1'
        elif self.last_written == b'RD6':
            return b'D6:0'
        elif self.last_written == b'RD7':
            return b'D7:1'
        elif self.last_written == b'RD8':
            return b'D8:0'
        elif self.last_written == b'RD9':
            return b'D9:1'
        elif self.last_written == b'RD10':
            return b'D10:0'
        elif self.last_written == b'RD11':
            return b'D11:1'
        elif self.last_written == b'RD12':
            return b'D12:0'
        elif self.last_written == b'RD13':
            return b'D13:1'
        elif self.last_written == b'RA0':
            return b'A0:122'
        elif self.last_written == b'RA1':
            return b'A1:384'
        elif self.last_written == b'RA2':
            return b'A2:276'
        elif self.last_written == b'RA3':
            return b'A3:768'
        elif self.last_written == b'RA4':
            return b'A4:1022'
        elif self.last_written == b'RA5':
            return b'A5:512'
        else:
            return b''

class TestArduinoMethods(unittest.TestCase):

    def setUp(self):
        self.ar = Arduino_Mock()
        self.digital_pins = range(0,14)
        self.pwm_pins = [3,5,6,9,10,11]
        self.analog_in_pins = range(0,6)
        self.analog_in_values = [122, 384, 276, 768, 1022, 512]
        self.pin_modes = ['I', 'O', 'P']

    def test_digital_write(self):
        """
        Tests writing 1 and 0 in the 13 digital pins
        """

        for pin in self.digital_pins:
            self.ar.digital_write(pin, 1)
            self.assertEqual(self.ar.conn.last_written, 
                    'WD{}:1'.format(pin).encode())
            self.ar.digital_write(pin, 0)
            self.assertEqual(self.ar.conn.last_written, 
                    'WD{}:0'.format(pin).encode())
    
    def test_analog_write(self):
        """
        Tests writing values to the pwm pins
        """

        for pin in self.pwm_pins:
            pwm_value = random.randrange(0,256)
            self.ar.analog_write(pin, pwm_value)
            self.assertEqual(self.ar.conn.last_written, 
                    'WA{}:{}'.format(pin,pwm_value).encode())
    
    def test_digital_read(self):
        """
        Tests reading from the 13 digital pins
        """

        res = self.ar.digital_read(0)
        self.assertEqual(self.ar.conn.last_written, b'RD0')
        self.assertEqual(res, 0)

        res = self.ar.digital_read(1)
        self.assertEqual(self.ar.conn.last_written, b'RD1')
        self.assertEqual(res, 1)
        
        res = self.ar.digital_read(2)
        self.assertEqual(self.ar.conn.last_written, b'RD2')
        self.assertEqual(res, 0)
    
        res = self.ar.digital_read(3)
        self.assertEqual(self.ar.conn.last_written, b'RD3')
        self.assertEqual(res, 1)
        
        res = self.ar.digital_read(4)
        self.assertEqual(self.ar.conn.last_written, b'RD4')
        self.assertEqual(res, 0)
    
        res = self.ar.digital_read(5)
        self.assertEqual(self.ar.conn.last_written, b'RD5')
        self.assertEqual(res, 1)
        
        res = self.ar.digital_read(6)
        self.assertEqual(self.ar.conn.last_written, b'RD6')
        self.assertEqual(res, 0)
    
        res = self.ar.digital_read(7)
        self.assertEqual(self.ar.conn.last_written, b'RD7')
        self.assertEqual(res, 1)
        
        res = self.ar.digital_read(8)
        self.assertEqual(self.ar.conn.last_written, b'RD8')
        self.assertEqual(res, 0)
    
        res = self.ar.digital_read(9)
        self.assertEqual(self.ar.conn.last_written, b'RD9')
        self.assertEqual(res, 1)
        
        res = self.ar.digital_read(10)
        self.assertEqual(self.ar.conn.last_written, b'RD10')
        self.assertEqual(res, 0)
    
        res = self.ar.digital_read(11)
        self.assertEqual(self.ar.conn.last_written, b'RD11')
        self.assertEqual(res, 1)
        
        res = self.ar.digital_read(12)
        self.assertEqual(self.ar.conn.last_written, b'RD12')
        self.assertEqual(res, 0)
    
        res = self.ar.digital_read(13)
        self.assertEqual(self.ar.conn.last_written, b'RD13')
        self.assertEqual(res, 1)
    
    def test_analog_read(self):
        """
        Tests reading from the analog in ports 
        """

        for pin,value in zip(self.analog_in_pins, self.analog_in_values):
            res = self.ar.analog_read(pin)
            self.assertEqual(self.ar.conn.last_written, 'RA{}'.format(pin).encode())
            self.assertEqual(res, value)
    
    def test_set_pin_mode(self):
        """
        Tests setting the pin mode for the digital pins
        """
        for pin in self.digital_pins:
                for mode in self.pin_modes:
                    self.ar.set_pin_mode(pin, mode)
                    self.assertEqual(self.ar.conn.last_written,
                            'M{}{}'.format(mode, pin).encode())

if __name__ =='__main__':
    unittest.main()
