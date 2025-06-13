import paho.mqtt.client as mqtt
import ssl
import time
import json
import random

# MQTT Broker details
broker_url = "13.60.179.184"  # AWS EC2 public IP
port = 443
topic = "iot/sensors"

# TLS certificate path
ca_cert_path = "mqtt-ec2.pem"  # Use the bundled certificate provided with the repo

# Create client
client = mqtt.Client(client_id="mqtt_simulator1")

# TLS configuration
client.tls_set(
    ca_certs=ca_cert_path,
    certfile=None,
    keyfile=None,
    cert_reqs=ssl.CERT_NONE,
    tls_version=ssl.PROTOCOL_TLS,
    ciphers=None
)
client.tls_insecure_set(True)

# Connect callback
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to broker")
    else:
        print(f"❌ Connection failed with code {rc}")

client.on_connect = on_connect

# Connect and loop
client.connect(broker_url, port)
client.loop_start()

# Publish simulated data every 3 sec
try:
    while True:
        payload = {
            "temperature": round(random.uniform(20.0, 35.0), 2),
            "humidity": round(random.uniform(30.0, 60.0), 2),
            "unit": "C/%"
        }
        client.publish(topic, json.dumps(payload))
        print(f"📤 Published: {payload}")
        time.sleep(3)
except KeyboardInterrupt:
    print("❌ Disconnected")
    client.loop_stop()
    client.disconnect()
