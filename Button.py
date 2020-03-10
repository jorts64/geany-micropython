
import time 
 
while True:
   if polsador():
	 led[1] = color['apagat']
	 led[4] = color['verd']
	 led.write()
   else:
	 led[1] = color['vermell']
	 led[4] = color['apagat']
	 led.write()
   time.sleep(1)



