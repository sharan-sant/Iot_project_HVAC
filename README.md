# HVAC MQTT Services

This project contains small services used to experiment with MQTT and AWS RDS.
It includes:

- **Publisher** (`publisher/pub.py`) – sends random temperature and humidity
  readings to an MQTT broker over TLS.
- **Subscriber** (`subscriber/sub.py`) – listens to the same topic and prints
  incoming messages.
- **RDS Subscriber** (`db_subscriber_service/sub_to_rds.py`) – subscribes to the
  MQTT topic and stores the payload in a PostgreSQL database.

## Environment variables

The RDS subscriber requires the following variables at runtime:

- `DB_HOST` – database host name
- `DB_PORT` – database port (default `5432`)
- `DB_NAME` – database name
- `DB_USER` – database user
- `DB_PASSWORD` – database password (required)

## Building Docker images

TLS certificates (`mqtt.crt` and `mqtt.key`) must be available in the build
context when creating images. The repository `.gitignore` excludes these files
so they need to be provided separately.

```bash
# Build the RDS subscriber using the default Dockerfile
docker build -t hvac-rds-subscriber .

# Build the publisher image
docker build -f dockerfile-pub -t hvac-publisher .

# Build the RDS subscriber using dockerfile-sub (same as Dockerfile)
docker build -f dockerfile-sub -t hvac-rds-subscriber-alt .
```

