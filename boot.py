# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
import gc
import network
from antptime import settime

gc.collect()

def do_connect():
    
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.ifconfig(('192.168.0.250', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('krankenwagen', 'greentea')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

    if sta_if.isconnected() and settime():
    	print('Time synced')

do_connect()
