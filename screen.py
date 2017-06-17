import network
import time
from lcd import I2cLcd

class Screen:

	def __init__(self, i2c):
		self.display = I2cLcd(i2c, 63, 2, 16)
		sta_if = network.WLAN(network.STA_IF)
		self.ip = str(sta_if.ifconfig()[0])
		self.display.putstr('Booting...')
		time.sleep(2)
		self.stopped()


	def running(self, bank):
		self.display.clear()
		self.display.putstr("Bank: %s\nRUNNING" % bank)

	def stopped(self):
		self.display.clear()
		self.display.putstr("%s\nIDLE..." % self.ip)
