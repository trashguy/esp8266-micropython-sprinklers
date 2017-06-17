# esp8266-micropython-sprinklers

Simple sprinkler controller using micropython running on esp8266 board.
 
Utilizing an MCP23017 to expand io ports over i2c since the little ESP8266 boards only have 2 io ports. There is also an LCD screen and DS321 RTC running on the i2c bus. Right now I removed the RTC as I have found that scheduling within micropython is difficult.  For now I am handling all the control form a Pi and just using over REST.

```
curl -H "Content-Type: application/json" -X POST -d '{"bank": 1, "running": true}' http://192.168.0.250/api/sprinklers
```