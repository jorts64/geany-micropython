from D1mini import *

while True:
	sensor.measure()
	display.fill(0)
	display.text(str(sensor.temperature()), 0, 0)
	display.text(str(sensor.humidity()), 0, 8)
	display.show()
	time.sleep_ms(4000)

