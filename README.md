**AMBIENTE VIRTUAL**

- **Criar**
$ python3 -m venv venv

- **Carregar**
$ source venv/bin/activate

**INSTALAR DEPENDÊNCIAS**:

- **OpenCV**
$ git clone https://github.com/jayrambhia/Install-OpenCV
$ cd Install-OpenCV/Ubuntu
$ chmod +x * 
$ ./opencv_latest.sh
$ pip install opencv-python

- **Outras dependências**
$ pip install imutils
$ pip install paho-mqtt

**CARREGANDO O MÓDULO E CONFIGURANDO**

- **Clone o código fonte**
$ cd ~
$ git clone https://github.com/Smart-AniMon/module

- **Credenciais mqtt**
$ cd module
$ nano credentials.txt
[separar um por linha na ordem: user, password, host, topic] 

- **Diretório para imagens**
$ mkdir images

**SENSOR DE TEMPERATURA E UMIDADE**

https://blog.fazedores.com/temperatura-com-dht11-e-raspberry-pi/#:~:text=Sensor%20de%20umidade%20e%20temperatura,%E2%80%93%20Umidade%20%3A%2020%20%C3%A0%2080%25

$ sudo apt-get install git build-essential python-dev
$ git clone https://github.com/adafruit/Adafruit_Python_DHT.git
$ cd Adafruit_Python_DHT
$ python3 setup.py install
$ sudo apt-get install python3-setuptools
$ pip install RPi.GPIO