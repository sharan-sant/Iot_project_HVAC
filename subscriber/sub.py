import paho.mqtt.client as mqtt
import ssl

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("iot/sensors")

def on_message(client, userdata, msg):
    print(f"Received: {msg.payload.decode()} from topic: {msg.topic}")

client = mqtt.Client()

client.tls_set(
    ca_certs="mqtt-ec2.pem",
    cert_reqs=ssl.CERT_REQUIRED,
    tls_version=ssl.PROTOCOL_TLS,
)

client.tls_insecure_set(True)

client.connect("13.60.179.184", 443)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
