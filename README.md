# INSTRUÇÕES PARA INSTALAÇÃO DO MÓDULO

Por conveniência vamos supor que deseja fazer a instalação no seu diretório pessoal (indicado pelo símbolo ~ ).

**CRIE UM AMBIENTE VIRTUAL**

- **Criar**
~~~
$ cd ~
$ python3 -m venv venv
~~~
- **Carregar**
~~~
$ source venv/bin/activate
~~~

**INSTALE AS DEPENDÊNCIAS DO PROJETO**:

- **OpenCV**
~~~
$ cd ~
$ git clone https://github.com/jayrambhia/Install-OpenCV
$ cd Install-OpenCV/Ubuntu
$ chmod +x *
$ ./opencv_latest.sh
$ pip install opencv-python
~~~

- **Adafruit_Python_DHT**
~~~
$ cd ~
$ sudo apt-get install git build-essential python-dev
$ git clone https://github.com/adafruit/Adafruit_Python_DHT.git
$ cd Adafruit_Python_DHT
$ python3 setup.py install
$ sudo apt-get install python3-setuptools
$ pip install RPi.GPIO
~~~

- **Outras dependências**
~~~
$ cd ~
$ pip install imutils
$ pip install paho-mqtt
~~~

**CARREGUE O CÓDIGO DO MÓDULO E CONFIGURE**

- **Clone o código fonte**
~~~
$ cd ~
$ git clone https://github.com/Smart-AniMon/module
~~~

- **Adicione as credenciais mqtt**
~~~
$ cd module
$ nano credentials.txt
~~~
>IMPORTANTE: As credenciais inseridas no arquivo _credentials.txt_ devem seguir o formato:
~~~
user
password
host
topic
~~~

- **Crie o diretório de imagens**
~~~
$ mkdir images
~~~

# MONTAGEM DOS COMPONENTES

Realize a montagem dos componentes conforme o diagrama abaixo:

<img src="https://github.com/Smart-AniMon/docs/blob/main/images/module-connection-diagram.png" alt="drawing" width="600"/>

**CONFIGURE O SENSOR DE MOVIMENTO PIR HC-SR501**

- Posicione a lente do sensor para cima e os dois trimpots virados para você.
- Tempo (esquerdo): Gire o trimpot completamente no sentido anti horário para diminuir o tempo de saída alta após a detecção.
- Sensibilidade (direito): Gire o trimpot completamente no sentido anti horário para diminuir o nível de sensibilidade (opcional).

# INICIANDO O MÓDULO

O módulo deve ser executado com _python3_. Para acompanhar a atividade do módulo execute no modo depuração adicionando o argumento _-D_ ou _--debug_:
~~~
$ python3 ~/module/controller.py -D
~~~
A mensagem **Run** indica que o módulo está operando. 
