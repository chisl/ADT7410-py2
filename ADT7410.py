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

from ADT7410_constants import *

# name:        ADT7410
# description: ±0.5°C Accurate, 16-Bit Digital I2C Temperature Sensor
# manuf:       Analog Devices
# version:     0.1
# url:         http://www.analog.com/media/en/technical-documentation/data-sheets/ADT7410.pdf
# date:        2017-12-28


# Derive from this class and implement read and write
class ADT7410_Base:
	"""±0.5°C Accurate, 16-Bit Digital I2C Temperature Sensor"""
	# Register TEMPERATURE
	
	
	def setTEMPERATURE(self, val):
		"""Set register TEMPERATURE"""
		self.write(REG.TEMPERATURE, val, 16)
	
	def getTEMPERATURE(self):
		"""Get register TEMPERATURE"""
		return self.read(REG.TEMPERATURE, 16)
	
	# Bits TLOWFLAG_LSB0
	# Flags a TLOW event if the configuration register, Register Address 0x03[7] = 0 (13-bit resolution),
	#           and if comparator mode is selected through the configuration register, Register Address
	#           0x03[4]. When the temperature value is below TLOW, this bit it set to 1.
	#           Contains the Least Significant Bit 0 of the 15-bit temperature value if the configuration
	#           register, Register Address 0x03[7] = 1 (16-bit resolution). 
	
	# Bits THIGHFLAG_LSB1
	# Flags a THIGH event if the configuration register, Register Address 0x03[7] = 0 (13-bit resolution),
	#           and if comparator mode is selected through the configuration register, Register Address
	#           0x03[4]. When the temperature value is above THIGH, this bit it set to 1.
	#           Contains the Least Significant Bit 1 of the 15-bit temperature value if the configuration
	#           register, Register Address 0x03[7] = 1 (16-bit resolution). 
	
	# Bits TCRITFLAG_LSB2
	# Flags a TCRIT event if the configuration register, Register Address 0x03[7] = 0 (13-bit resolution),
	#           and if comparator mode is selected through the configuration register, Register Address
	#           0x03[4]. When the temperature value exceeds TCRIT, this bit it set to 1.
	#           Contains the Least Significant Bit 2 of the 15-bit temperature value if the configuration
	#           register, Register Address 0x03[7] = 1 (16-bit resolution). 
	
	# Bits TEMPERATURE
	# Temperature value in twos complement format
	# Bits SIGN
	# indicates if the temperature value is negative or positive
	# Register Status
	# This 8-bit read-only register reflects the status of the overtemperature
	#       and undertemperature interrupts that can cause the CT and
	#       INT pins to go active. It also reflects the status of a temperature
	#       conversion operation. The interrupt flags in this register are
	#       reset by a read operation to the status register and/or when
	#       the temperature value returns within the temperature limits,
	#       including hysteresis. The RDY bit is reset after a read from the
	#       temperature value register. In one-shot and 1 SPS modes, the
	#       RDY bit is reset after a write to the one-shot bits. 
	
	
	def setStatus(self, val):
		"""Set register Status"""
		self.write(REG.Status, val, 8)
	
	def getStatus(self):
		"""Get register Status"""
		return self.read(REG.Status, 8)
	
	# Bits unused_0
	# Bits THIGH
	# Set this bit to 1 when the temperature goes below the TLOW temperature limit, and if comparator
	#           mode is selected through the configuration register, Register Address 0x03[4]. The bit clears
	#           to 0 when the status register is read and/or when the temperature measured goes back above
	#           the limit set in the setpoint TLOW + THYST registers. 
	
	# Bits TLOW
	# Set this bit to 1 when the temperature goes above the THIGH temperature limit, and if comparator
	#          mode is selected through the configuration register, Register Address 0x03[4]. The bit clears
	#          to 0 when the status register is read and/or when the temperature measured goes back
	#          below the limit set in the setpoint THIGH − THYST registers. 
	
	# Bits TCRIT
	# Set this bit to 1 when the temperature goes above the TCRIT temperature limit, and if comparator
	#           mode is selected through the configuration register, Register Address 0x03[4]. This bit clears
	#           to 0 when the status register is read and/or when the temperature measured goes back
	#           below the limit set in the setpoint TCRIT − THYST registers. 
	
	# Bits nRDY
	# This bit goes low when the temperature conversion result is written into the temperature
	#           value register. It is reset to 1 when the temperature value register is read. In one-shot and 1
	#           SPS modes, this bit is reset after a write to the one-shot bits. 
	
	# Register Configuration
	# This 8-bit read/write register stores various configuration modes
	#       for the ADT7410, including shutdown, overtemperature and
	#       undertemperature interrupts, one-shot, continuous conversion,
	#       interrupt pins polarity, and overtemperature fault queues. 
	
	
	def setConfiguration(self, val):
		"""Set register Configuration"""
		self.write(REG.Configuration, val, 8)
	
	def getConfiguration(self):
		"""Get register Configuration"""
		return self.read(REG.Configuration, 8)
	
	# Bits FAULT_QUEUE
	# These two bits set the number of undertemperature/overtemperature faults that can
	#           occur before setting the INT and CT pins. This helps to avoid false triggering due
	#           to temperature noise. 
	
	# Bits CT_PIN_POLARITY
	# This bit selects the output polarity of the CT pin. 
	# Bits INT_PIN_POLARITY
	# This bit selects the output polarity of the INT pin. 
	# Bits INT_CT_MODE
	# This bit selects between comparator mode and interrupt mode. 
	# Bits OPMODE
	# These two bits set the operational mode for the ADT7410. 
	# Bits RESOLUTION
	# This bit sets up the resolution of the ADC when converting. 
	# Register THIGH
	# The THIGH setpoint MSB and THIGH setpoint LSB registers store
	#       the overtemperature limit value. An overtemperature event
	#       occurs when the temperature value stored in the temperature
	#       value register exceeds the value stored in this register. The INT pin
	#       is activated if an overtemperature event occurs. The temperature
	#       is stored in twos complement format with the MSB being the
	#       temperature sign bit. 
	#       The default setting for the THIGH setpoint is 64°C. 
	
	
	def setTHIGH(self, val):
		"""Set register THIGH"""
		self.write(REG.THIGH, val, 16)
	
	def getTHIGH(self):
		"""Get register THIGH"""
		return self.read(REG.THIGH, 16)
	
	# Bits THIGH
	# Register TLOW
	# The TLOW setpoint MSB and TLOW setpoint LSB registers store
	#       the undertemperature limit value. An undertemperature event
	#       occurs when the temperature value stored in the temperature
	#       value register is less than the value stored in this register. The
	#       INT pin is activated if an undertemperature event occurs. The
	#       temperature is stored in twos complement format with the MSB
	#       being the temperature sign bit. 
	#       The default setting for the TLOW setpoint is 10°C. 
	
	
	def setTLOW(self, val):
		"""Set register TLOW"""
		self.write(REG.TLOW, val, 16)
	
	def getTLOW(self):
		"""Get register TLOW"""
		return self.read(REG.TLOW, 16)
	
	# Bits TLOW
	# Register TCRIT
	# The TCRIT setpoint MSB and TCRIT setpoint LSB registers store
	#       the critical overtemperature limit value. A critical overtemperature
	#       event occurs when the temperature value stored in the
	#       temperature value register exceeds the value stored in this
	#       register. The CT pin is activated if a critical overtemperature
	#       event occurs. The temperature is stored in twos complement
	#       format with the MSB being the temperature sign bit. 
	#       The default setting for the TCRIT limit is 147°C. 
	
	
	def setTCRIT(self, val):
		"""Set register TCRIT"""
		self.write(REG.TCRIT, val, 16)
	
	def getTCRIT(self):
		"""Get register TCRIT"""
		return self.read(REG.TCRIT, 16)
	
	# Bits TCRIT
	# Register THYST
	# This 8-bit read/write register stores the temperature hysteresis
	#       value for the THIGH, TLOW, and TCRIT temperature limits. The
	#       temperature hysteresis value is stored in straight binary format
	#       using four LSBs. Increments are possible in steps of 1°C from
	#       0°C to 15°C. The value in this register is subtracted from the
	#       THIGH and TCRIT values and added to the TLOW value to implement
	#       hysteresis.
	#       Default is 5°C. 
	
	
	def setTHYST(self, val):
		"""Set register THYST"""
		self.write(REG.THYST, val, 8)
	
	def getTHYST(self):
		"""Get register THYST"""
		return self.read(REG.THYST, 8)
	
	# Bits HYSTERESIS
	# Hysteresis value, from 0°C to 15°C. Stored in straight binary format. 
	#           The default setting is 5°C. 
	
	# Bits unused_0
	# Register ID
	
	
	def setID(self, val):
		"""Set register ID"""
		self.write(REG.ID, val, 8)
	
	def getID(self):
		"""Get register ID"""
		return self.read(REG.ID, 8)
	
	# Bits REVISION_ID
	# Revision ID Contains the silicon revision identification number 
	# Bits MANUFACTURER_ID
	# Manufacture ID Contains the manufacturer identification number 
	# Register RESET
	# Software reset: Address pointer word as a command word to reset the part and
	#       upload all default settings. The ADT7410 does not respond to the I2
	#       C bus commands (do not acknowledge) during the default
	#       values upload for approximately 200 µs.
	
	
	def setRESET(self, val):
		"""Set register RESET"""
		self.write(REG.RESET, val, 0)
	
	def getRESET(self):
		"""Get register RESET"""
		return self.read(REG.RESET, 0)
	
	# Bits RESET
