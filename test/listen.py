# PARA OUVIR UM TÓPICO

# Para instalar o paho-mqtt use o comando pip install paho-mqtt
import string
import paho.mqtt.client as mqtt

def get_credentials():
    ref_arquivo = open("../credentials.txt","r") 
    return ref_arquivo.readlines()
    
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
  
    # O subscribe fica no on_connect pois, caso perca a conexão ele a renova
    # Lembrando que quando usado o #, você está falando que tudo que chegar após a barra do topico, será recebido
    client.subscribe("animon/identification")
    
# Callback responável por receber uma mensagem publicada no tópico acima
def on_message(client, userdata, msg):
    print(msg.topic+" -  "+str(msg.payload))
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

credentials = get_credentials()

# Seta um usuário e senha para o Broker, se não tem, não use esta linha
client.username_pw_set(credentials[0].rstrip('\n'), password=credentials[1].rstrip('\n'))

# Conecta no MQTT Broker, no meu caso, o Mosquitto
client.connect(credentials[2].rstrip('\n'), 1883, 60)

# Inicia o loop
client.loop_forever()