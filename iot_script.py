def on_log(clent, userdta, level, buf):
    print(buf)
def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True
        print("connected OK")
    else:
        print("Bad connection Returned code", rc)
        client.loop_stop()
def on_disconnect(client, userdta, rc):
    print("client disconnected ok")
def on_publish(client, userdata, mid):
    print("In on_pub callback mid= ", mid)

count=0
mqtt.Client.connected_flag=False
mqtt.CLient.suppress_puback_flag=False
client= mqtt.Client("python1")

client.on_connect=on_connect
client.on_disconnect= on_disconnect
client.on_publish=on_publish

broker="http://192.168.17.106"
port=1883
topic="v1/devices/me/telemetry"

username=""
password=""
if username !="":
    pass
client.username_pw_set(username, password)
client.connect(broker, port)
while not client.connected_flag:
    client.loop()
    time.sleep(1)
time.sleep(3)
data=dict()
for i in range(100):
    data["main-light"]="ON"
    data["main-Door"]="OPEN"
    data_out=json.dumps(data)
    print("publish topic",topic, "data out= ",data_out)
    ret=client.publish(topic, data_out, 0)
    time.sleep(5)
    client.loop()
    data["main-light"]="OFF"
    data["main-Door"]="CLOSED"
    data_out=json.dumps(data)
    print("publish topic",topic, "data out= ",data_out)
    ret=client.publish(topic, data_out, 0)
    time.sleep(5)
    client.loop()
client.disconnect()