# socat PTY,link=/tmp/ttyS0,raw,echo=0 PTY,link=/tmp/ttyS1,raw,echo=1

import serial, time, json
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected = True
        print("Connected succesfully")
    else: 
        print("Not connected, returned code: ", rc)
        client.loop_stop()
def on_disconnect(client, userdata, rc):
    if(rc == 0):
        print("Disconnection Successful")
    else:
        print("System disconnected via code: ", rc)
def on_publish(client, userdata, mid):
    print("Message: ", mid, " has left the client")



PuertoSerial = serial.Serial('/tmp/ttyS1 ',9600) 
print("Connected to serial port")
client = mqtt.Client("B76547")
client.connected = False
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

broker ="iot.eie.ucr.ac.cr"
port = 1883
topic = "v1/devices/me/telemetry"
device = "Jnna3Y5vNYCHEbEk3XlV"
#device = "8RLko5j9POK6dxmleE7J"
client.username_pw_set(device)
client.connect(broker, port)
dict = dict()
while client.connected != True:
    client.loop()
    time.sleep(2)
print("Program waits every 10 min to send data to dashboard")

while(1):
    if(PuertoSerial.in_waiting > 0):
        input = PuertoSerial.readline()
        decode = input.decode().replace('\r\n', '')
        split = decode.split('/')
        dict["Temperature"] = split[0]
        dict["Humidity"] = split[1]
        dict["Intensity of light(cd)"] = split[2]
        dict["Wind speed (m/s)"] = split[3]
        if(int(split [4]) == 0):
            dict["Active Rain (Yes/No)"] = "Yes"
        else:
            dict["Active Rain (Yes/No)"] = "No"
        
        if(split[5] == '0'):
            dict["Battery Level"] = "OK"
        else:
            dict["Battery Level"] = "Low battery"
        output = json.dumps(dict)
        print(output)
        client.publish(topic, output)

