FROM python:3.10-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY db_subscriber_service/sub_to_rds.py ./sub_to_rds.py
COPY mqtt.crt .
COPY mqtt.key .

CMD ["python", "sub_to_rds.py"]