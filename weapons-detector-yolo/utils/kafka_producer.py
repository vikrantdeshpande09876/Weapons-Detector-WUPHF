from kafka import KafkaProducer

class Producer():
    """Simple wrapper class for producing a response asynchronously over a topic.
    """
    
    def __init__(self, kafka_server='localhost:9092'):
        """Initialize the Kafka-producer object.
        Args:
            kafka_server ([str]): Defaults to 'localhost:9092'
        """
        print(kafka_server)
        self.producer = KafkaProducer(
            bootstrap_servers = kafka_server,
            api_version = (0, 11, 15),
            #value_serializer=lambda m: pickle.dumps(m).encode('ascii')
            )
        
    
    def publish(self, topic, message):
        """Sends a message over a Kafka-topic.
        Args:
            topic ([str]): Kafka-Topic name.
            message ([str]): Message to send over the Kafka-topic.
        """
        self.producer.send(topic, message)
        self.producer.flush()


    def send_alert_if_weapon(self, predictions, topic, message, verbose=False):
        final_labels = set([pred.split()[0] for pred in predictions])
        if 'knife' in final_labels or 'pistol' in final_labels:
            print(f'Final Labels: {final_labels}. Sending out a Kafka message over topic {topic}...')
            if verbose:  print(f'Message={message}')
            self.publish(topic=topic, message=message)