#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""ADT7410: ±0.5°C Accurate, 16-Bit Digital I2C Temperature Sensor"""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["Analog Devices"]
__license__    = "TBD"
__version__    = "0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

class REG:
	TEMPERATURE = 0
	Status = 2
	Configuration = 3
	THIGH = 4
	TLOW = 6
	TCRIT = 8
	THYST = 10
	ID = 11
	RESET = 47
