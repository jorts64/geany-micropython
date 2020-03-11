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
* Anar a Munta (Construeix a noves versions) -> Especifica Ordre de Muntatge (Ordres de construcció a noves versions)
* Afegir 2 noves opcions (veure imatge):
  * La Opció 2 de Compile: Executa al D1 mini, ampy -p /dev/ttyUSB0 run "%f" 
  * La Opció 2 de Execute: Consola D1 mini, picocom -b 115200 /dev/ttyUSB0 
* Canviar la opció 3 de Compile: Executa bucle infinit al D1 mini, ampy -p /dev/ttyUSB0 run "%f" -n

Ja podem treballar al nostre entorn micropython :blush:

![Captura de pantalla](/screenshot.png)

Potser no tingueu instal·lat al sistema el pip, caldrà fer 
sudo apt install python-pip

També és possible que us calgui sortir i entrar de sessió per activar tots els canvis
