import paho.mqtt.client as mqtt
import ssl
import psycopg2
import json

# 🔐 PostgreSQL RDS config
db_conn = psycopg2.connect(
    host="iot-database.c10s2mo025fv.eu-north-1.rds.amazonaws.com",
    port=5432,
    database="postgres",
    user="postgres",
    password="g7[Eq~<Ai>*3wt7#~uZ5SDI:2]v2"  # 🛑 Use your actual password
)

cursor = db_conn.cursor()

# 🔗 MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    print("✅ MQTT Connected with result code " + str(rc))
    client.subscribe("iot/sensors")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print(f"📥 Received: {payload}")

    try:
        data = json.loads(payload)
        temperature = data.get("temperature")
        humidity = data.get("humidity")
        unit = data.get("unit", "C/%")

        cursor.execute("""
            INSERT INTO sensor_data (temperature, humidity, unit)
            VALUES (%s, %s, %s)
        """, (temperature, humidity, unit))
        db_conn.commit()
        print("📤 Saved to RDS!")
    except Exception as e:
        print(f"❌ Error: {e}")

# 🔧 MQTT TLS Secure Connection
client = mqtt.Client()
client.tls_set(
    ca_certs="mqtt.crt",
    cert_reqs=ssl.CERT_REQUIRED,
    tls_version=ssl.PROTOCOL_TLS,
)
client.tls_insecure_set(True)

client.connect("13.60.179.184", 443)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
