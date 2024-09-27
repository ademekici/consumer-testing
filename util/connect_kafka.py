import time

from confluent_kafka import Producer, Consumer, KafkaError, KafkaException
import json
import os

# Use the correct port for external access to the Kafka broker
KAFKA_BROKER = os.getenv('KAFKA_BROKER', 'localhost:29092')

# Create a Kafka producer
producer_config = {
    'bootstrap.servers': KAFKA_BROKER
}


def send_kafka_message(topic, message, key):
    producer = Producer(producer_config)
    producer.produce(topic, json.dumps(message).encode('utf-8'), key=key)
    producer.flush()


def print_assignment(consumer, partitions):  # if assignment empty, reconnect !
    print('Assignment: %s', partitions)


def start_kafka_consumer_in_stretch(topic, key, consumer_group, messages, timeout=60):
    consumer_conf = {
        'bootstrap.servers': KAFKA_BROKER,
        'group.id': consumer_group,
        'auto.offset.reset': 'earliest'
    }
    consumer = Consumer(consumer_conf)
    consumer.subscribe([topic], on_assign=print_assignment)
    start_time = time.time()

    while True:
        try:
            msg = consumer.poll(1.0)  # timeout in seconds
            current_time = time.time()
            if current_time - start_time > timeout:
                raise TimeoutError()
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    raise KafkaException(msg.error())
            if msg.key().decode('utf-8') == key:
                consumer.close()
                messages.append((msg.key().decode('utf-8').strip(), json.loads(msg.value().decode('utf-8'))))
                return
        except Exception as e:
            consumer.close()
            print(f"Exception: {e}")
            break

    consumer.close()
    return
