# Instal·lació micropython al D1 mini
Per instal·lar micropython al vostre D1 mini cal    

    sudo pip3 install esptool
    cd firmware
    esptool.py --port /dev/ttyUSB0 erase_flash
    esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20200911-v1.13.bin 
    cd ..
    ampy -p /dev/ttyUSB0 mkdir lib
    cd lib
    ampy -p /dev/ttyUSB0  put dht12.py /lib/dht12.py
    ampy -p /dev/ttyUSB0  put ssd1306.py /lib/ssd1306.py
    ampy -p /dev/ttyUSB0  put umqttsimple.py /lib/umqttsimple.py 
    cd ..
    ampy -p /dev/ttyUSB0  put D1mini.py
