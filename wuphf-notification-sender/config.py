import os

# Kafka Parameters
REQUEST_TOPIC = os.environ.get('REQUEST_TOPIC').replace('\'','')
GROUP_ID = os.environ.get('GROUP_ID').replace('\'','')
KAFKA_SERVER = os.environ.get('KAFKA_SERVER').replace('\'','')

# Email Parameters
SENDER_EMAIL = os.environ.get('SENDER_EMAIL').replace('\'','')
SENDER_PASSWORD = os.environ.get('SENDER_PASSWORD').replace('\'','')
RECEIVER_EMAIL = os.environ.get('RECEIVER_EMAIL').replace('\'','')