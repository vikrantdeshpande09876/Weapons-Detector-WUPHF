import json
from kafka import KafkaConsumer

class Consumer:
    """Simple wrapper class for consuming a request asynchronously over a topic.
    """

    def __init__(self, topic_to_consume, kafka_server='localhost:9092'):
        """Initialize the Kafka-consumer object.
        Args:
            topic_to_consume ([str]): The topic to monitor.
            kafka_server ([str]): Defaults to 'localhost:9092'
        """
        self.TOPIC_TO_CONSUME = topic_to_consume
        self.CONSUMER = KafkaConsumer(
            self.TOPIC_TO_CONSUME,
            bootstrap_servers = [kafka_server],
            #api_version = (0, 11, 15),
        )


    def consume(self):
        """Loops over the consumer objects received over a Kafka-topic.
        Returns:
            [KafkaConsumer data]: Returns the response received from Producer.
        """
        print(self.CONSUMER.bootstrap_connected())
        if self.CONSUMER.bootstrap_connected():
            print('Connected to Kafka-server successfully...')
            while True:
                try:
                    yield next(self.CONSUMER)
                except StopIteration:
                    print('Stopping consumer...')


    def get_last_offset(self):
        """Returns the last index of message in specific Kafka-topic
        Returns:
            [int]: The Last offset position.
        """
        last_offset = 0
        while not self.consumer._client.poll():
            last_offset += 1
            continue
        self.consumer.seek_to_beginning()
        return last_offset



    def close(self):
        """Close the consumer, waiting indefinitely for any needed cleanup.
        """
        self.consumer.close()