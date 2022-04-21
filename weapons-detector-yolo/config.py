import os

# Flask Parameters
DEBUG = os.environ.get('DEBUG', False)
SECRET_KEY = os.environ.get('SECRET_KEY') or 'vikrantsecretkey'
STATIC_DIR = os.environ.get('STATIC_DIR') or os.path.join(os.path.dirname(__file__), 'static')
FLASK_HOST = os.environ.get('FLASK_HOST').replace('\'','')
FLASK_PORT = os.environ.get('FLASK_PORT').replace('\'','')

# Kafka Parameters
RESPONSE_TOPIC = os.environ.get('RESPONSE_TOPIC').replace('\'','')
GROUP_ID = os.environ.get('GROUP_ID').replace('\'','')
KAFKA_SERVER = os.environ.get('KAFKA_SERVER') .replace('\'','')