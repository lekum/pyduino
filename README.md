pyduino
=======

Python library to interface with arduino via serial connection.

[![Build Status](https://travis-ci.org/lekum/pyduino.svg?branch=master)](https://travis-ci.org/lekum/pyduino)

Functionality implemented
-------------------------

The library implements a two-way communication over the serial connection with the Arduino, sending text strings that encode operations to be perfomed in the Arduino board and parsing the returned messages.

The functionalities of the Arduino library that are currently exposed via this API are:

- pinMode() 
- digitalRead()
- digitalWrite()
- analogRead()
- analogWrite()

Usage
-----

In order to use the library, you will need to install the python3 requirements described in ``requirements.txt`` and load the arduino sketch (``pyduino_sketch.ino``) in the board.

After creating an Arduino board, it is recommended to pause for some seconds in order to allow the serial connection to be established.

Usage example:

	import time
	from pyduino import Arduino

	a = Arduino()
	time.sleep(3)
	a.set_pin_mode(13,'O')
	a.set_pin_mode(12,'I')
	time.sleep(1)
	a.digital_write(13,1)
	a.analog_write(5,245)
	print(a.digital_read(12))
	print(a.analog_read(2))
	time.sleep(5)

Enjoy!
