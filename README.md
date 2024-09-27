# Consumer Testing

This project is an example of implementing a Kafka consumer using Python. The primary objective is to consume messages from a Kafka topic, process the data, and produce a new message to another Kafka topic. The project follows an event-driven architecture and is suitable for scenarios like processing product updates.

## Purpose

The main goals of this project are to:
- **Consume Kafka Messages**: The consumer listens to a specified Kafka topic (e.g., product updates) to receive events.
- **Process and Transform Data**: Extract relevant information, apply transformations, or enrich the data.
- **Produce Processed Messages**: After processing, produce a new message to an output Kafka topic.
- **Integration Testing**: Validate the consumer's functionality using BDD (Behavior-Driven Development) with the `behave` framework.

## Structure

- **`helper/`**: Contains helper modules like assertions and aggregations.
- **`util/`**: Provides utility scripts for Kafka connections and message handling.
- **`integration-consumer-testing-demo/`**: Houses the main example (`sample-integration-consumer`) demonstrating the implementation.

## Examples 

1. `sample-integration-consumer`

    This repository includes an example implementation located in the [`integration-consumer-testing-demo/sample-integration-consumer`](integration-consumer-testing-demo/sample-integration-consumer) directory. The example demonstrates:
    
    - How to implement the Kafka consumer using Python.
     - Setting up a Dockerized environment with Kafka and Zookeeper.
     - Running integration tests using `behave`.