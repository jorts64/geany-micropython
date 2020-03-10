# geany-micropython
Integració editor geany amb micropython ESP8266 D1 mini

## Programari:

* ampy
* picocom
* geany

## Instal·lació:

* pip install adafruit-ampy
* sudo apt install picocom
* sudo apt install geany

## Integració:

* Obrir geany i carregar un fitxer python (.py)
* Anar a Munta -> Especifica Ordre de Muntatge
* Afegir 2 noves opcions (veure imatge):
  * La Opció 2 de Compile: Executa al D1 mini, ampy -p /dev/ttyUSB0 run "%f" -n
  * La Opció 2 de Execute: Consola D1 mini, picocom -b 115200 /dev/ttyUSB0 
* Canviar la opció 3 de Compile: Executa bucle infinit al D1 mini, ampy -p /dev/ttyUSB0 run "%f" -n
![Captura de pantalla](/screenshot.png)
