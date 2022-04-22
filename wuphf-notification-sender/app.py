import json
from utils.email_notifier import send_email
from utils.consumer import Consumer
from config import *

def parse_input_alert(message):
    """Sample message body: {"header":"WEAPON DETECTED", "label":["pistol","knife"]}

    Args:
        message (_type_): _description_
    """
    try:
        message_body = json.loads(message.value)
        #filename = 'some_file.csv'
        #SourcePathName  = 'C:/reports/' + filename 
        send_email(sender_email=SENDER_EMAIL, sender_password=SENDER_PASSWORD, receiver_email=RECEIVER_EMAIL, body=message_body.get('label'))
    except Exception as e:
        print(f'ERROR: Something went wrong while triggering an email...\n{e}')



if __name__=='__main__':
    print(KAFKA_SERVER, REQUEST_TOPIC)
    print(SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL)
    consumer = Consumer(topic_to_consume=REQUEST_TOPIC, kafka_server=KAFKA_SERVER)
    for message in consumer.consume():
        print(message.value)
        parse_input_alert(message)