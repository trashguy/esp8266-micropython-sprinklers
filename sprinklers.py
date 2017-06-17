import time

class Sprinklers:

	def __init__(self, i2c, screen):
		self.i2c = i2c
		self.i2c_addr = 32
		self.screen = screen
		self.running = False
		self.runningBank = 0
		self.startTime = 0

		if self.i2c_addr in self.i2c.scan():
			self.i2c.writeto_mem(self.i2c_addr, 0, b'\x00')
			self.i2c.writeto_mem(self.i2c_addr, 20, b'\x00')
		else:
			print('Sprinklers not detected')			

	def bank_hex(self, bank):
		if bank is 1:
			return b'\x01'
		elif bank is 2:
			return b'\x02'
		elif bank is 3:
			return b'\x04'
		elif bank is 4:
			return b'\x08'
		elif bank is 5:
			return b'\x10'
		else:
			pass
			
	def start_bank(self, bank):
		if self.i2c_addr in self.i2c.scan():
			self.i2c.writeto_mem(self.i2c_addr, 20, self.bank_hex(bank))
			self.running = True
			self.runningBank = bank
			self.startTime = time.time()
			self.screen.running(bank)
		else:
			print('Sprinklers not detected')

	def stop_bank(self):
		if self.i2c_addr in self.i2c.scan():
			self.i2c.writeto_mem(self.i2c_addr, 20, b'\x00')
			self.running = False
			self.runningBank = 0
			self.time = 0
			self.screen.stopped()
		else:
			print('Sprinklers not detected')

	def isRunning(self):
		return self.running

	def getRunningBank(self):
		return self.runningBank

	def getStartTime(self):
		return self.startTime
