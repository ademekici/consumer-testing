from confluent_kafka import Consumer, Producer
import json
import os
import uuid

# Kafka settings from environment variables
KAFKA_BROKER = os.getenv('KAFKA_BROKER', 'kafka:9092')
INPUT_TOPIC = os.getenv('INPUT_TOPIC', 'product-domain-topic')
OUTPUT_TOPIC = os.getenv('OUTPUT_TOPIC', 'product-integration-topic')
GROUP_ID = os.getenv('GROUP_ID', 'product-consumer-group')

# Kafka Consumer configuration
consumer_conf = {
    'bootstrap.servers': KAFKA_BROKER,
    'group.id': GROUP_ID,
    'auto.offset.reset': 'earliest'
}

# Kafka Producer configuration
producer_conf = {
    'bootstrap.servers': KAFKA_BROKER
}


class Product:
    def __init__(self, id: str, name: str, price: float, description: str):
        self.id = id
        self.name = name
        self.price = price
        self.description = description

    @staticmethod
    def from_json(data: str):
        product_data = json.loads(data)
        return Product(
            id=product_data.get('id', str(uuid.uuid4())),
            name=product_data.get('name', 'Unknown Product'),
            price=product_data.get('price', 0.0),
            description=product_data.get('description', '')
        )

    def to_integration_event(self):
        return ProductIntegrationEvent(
            product_id=self.id,
            product_name=self.name,
            description=self.description,
            price=self.price,
            status="Processed"
        )


class ProductIntegrationEvent:
    def __init__(self, product_id: str, product_name: str, description: str, price: float, status: str):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price
        self.status = status

    def to_json(self):
        return json.dumps({
            'product_id': self.product_id,
            'product_name': self.product_name,
            'description': self.description,
            'price': self.price,
            'status': self.status
        })


class KafkaProductProcessor:
    def __init__(self):
        self.consumer = Consumer(consumer_conf)
        self.producer = Producer(producer_conf)
        self.input_topic = INPUT_TOPIC
        self.output_topic = OUTPUT_TOPIC

    def consume_and_process(self):
        self.consumer.subscribe([self.input_topic])

        try:
            while True:
                msg = self.consumer.poll(1.0)  # Poll for new messages

                if msg is None:
                    continue
                if msg.error():
                    print(f"Consumer error: {msg.error()}")
                    continue

                # Process the received message into a Product
                product = Product.from_json(msg.value().decode('utf-8'))
                print(f"Received product: {product.name}, Price: {product.price}")

                # Transform and send to the output topic
                integration_event = product.to_integration_event()
                self.producer.produce(self.output_topic, integration_event.to_json().encode('utf-8'),
                                      key=integration_event.product_id)
                self.producer.flush()

                print(f"Produced integration event to {self.output_topic}: {integration_event.to_json()}")

        except KeyboardInterrupt:
            pass
        finally:
            self.consumer.close()


if __name__ == "__main__":
    processor = KafkaProductProcessor()
    processor.consume_and_process()
