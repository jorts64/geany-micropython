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

## Important

Tots els fitxser s'executen al D1 mini, però no es desen a la seva memòria flash

Si volem actualitzar el fitxer *main.py* (que s'autoexecuta després del *boot.py* després de donar alimentació al D1 mini) haurem de fer al terminal
~~~
ampy -p /dev/ttyUSB0 put "main.py"
~~~
El mateix passa si volem actualitzar el fitxer "boot.py" o qualsevol llibreria

Per tenir un llistat del les ordres disponibles només cal fer en un terminal
~~~
ampy
~~~

Si voleu podeu ampliar el nom d'opcions de *Geany* a *Compile* i afegir una nova opció per actualitzar *main.py* podeu anar
a *Edita -> Preferències -> Diversos*  i canviar el valor de *number_ft_menu_items*. Us caldrà reiniciar *Geany* per que els canvis tinguin efecte. 
