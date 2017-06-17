import uhttpd
import http_api_handler
import machine

from api_sprinklers import DefaultHandler
from sprinklers import Sprinklers
from screen import Screen

# Connect to i2c bus. Pin 5 and 4 on on NodeMCU boards or 0 and 2 on the little esp8266
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))

sc = Screen(i2c)

sp = Sprinklers(i2c, sc)

# UHTTPD config
api_handler = http_api_handler.Handler([(['sprinklers'], DefaultHandler(sp))])
server = uhttpd.Server([('/api', api_handler)])
server.run()