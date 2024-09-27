# Sample Integration Consumer

This project includes a Kafka consumer application that listens for events on an input topic, processes the data, and
produces a new message to an output topic. It also includes integration tests using `behave` to validate the consumer's
behavior.

## Table of Contents
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Environment Variables](#environment-variables)
- [Installation Guides](#installation-guides)
  - [Docker](#docker)
  - [Docker Compose](#docker-compose)
- [How to Run Consumer](#how-to-run-consumer)
- [How to Run Tests](#how-to-run-tests)
- [Explanation of the Test Steps](#explanation-of-the-test-steps)
- [Notes](#notes)

## Project Structure

- **`sample-integration-consumer/`**: The main directory for the consumer application.
    - **`consumer.py`**: The Kafka consumer implementation.
    - **`Dockerfile`**: Defines the Docker image for the consumer.
    - **`docker-compose.yml`**: Docker Compose file to set up Kafka, Zookeeper, the consumer, and other services.
    - **`requirements.txt`**: Lists dependencies for the consumer and tests.
    - **`tests/`**: Contains the integration tests and related data files.
        - **`data/`**: Holds JSON documents used in the tests (e.g., `ProductUpdatedEvent.json`).
        - **`features/`**: Contains the Gherkin feature files and step definitions for the tests.
            - **`steps/`**: Includes the step implementations (e.g., `kafka_steps.py`).

- **`util/`**: Utility functions and helper scripts (e.g., `connect_kafka.py`, `assertion.py`).

## Requirements

- Docker
- Docker Compose
- Python 3.x (for running tests)
- Virtual Environment (recommended for running tests)

## Environment Variables

- `KAFKA_BROKER`: Kafka broker address (default: `localhost:9092`)
- `INPUT_TOPIC`: Topic to consume messages from (default: `product-domain-topic`)
- `OUTPUT_TOPIC`: Topic to produce messages to (default: `product-integration-topic`)
- `GROUP_ID`: Consumer group ID (default: `product-consumer-group`)

These can be overridden in the `docker-compose.yml` file.

### Installation Guides

#### Docker

- **Windows**: Download and install Docker Desktop
  from [Docker for Windows](https://docs.docker.com/desktop/install/windows-install/). Make sure to enable WSL 2 (
  Windows Subsystem for Linux) for optimal performance.
- **Mac**: Download Docker Desktop for Mac from [Docker for Mac](https://docs.docker.com/desktop/install/mac-install/).
  Follow the installation steps in the link.
- **Linux**: Follow the official instructions to install Docker on Linux
  from [Docker's Get Docker](https://docs.docker.com/engine/install/) page. You can choose your specific Linux
  distribution (e.g., Ubuntu, CentOS) for detailed instructions.

#### Docker Compose

- **Windows and Mac**: Docker Compose is included with Docker Desktop, so no additional installation is needed.
- **Linux**: Install Docker Compose by following the instructions on
  the [Docker Compose installation page](https://docs.docker.com/compose/install/).

- The consumer is set to automatically listen to the `product-domain-topic` and send transformed messages to
  the `product-integration-topic`.

## How to Run Consumer

Inside the /sample-integration-consumer directory, run the following commands:

1. Build the Docker image:

   ```bash
   docker-compose build
   ```
   
2. Start the services (Zookeeper, Kafka broker, Kafka UI, and the consumer):
   ```bash
   docker-compose up -d
   ```
   This will automatically create the necessary Kafka topics (product-domain-topic and product-integration-topic) as
   part of
   the kafka-create-topics service.


3. To stop the services, should run:
   ```bash
   docker-compose down
   ```


4. Access Kafka UI:

    Once the services are running, access the Kafka UI at http://localhost:8080 to monitor topics and messages.


## How to Run Tests

**Warning:** You should run the consumer before running the tests!

1.	Set Up a Virtual Environment (Optional but Recommended):
       ```bash
        python3.11 -m venv .venv
        source .venv/bin/activate       
      ```
2.	Install Test Dependencies:

        Navigate to the sample-integration-consumer/ directory and install the required dependencies:
       ```bash
       pip install -r requirements.txt
       ```

3. Run the Tests:

    Inside the sample-integration-consumer/tests/ directory, run the tests using behave:
    ```bash
   cd tests
    export PYTHONPATH=$(pwd)
    behave $(pwd)/features
   ```
   This command will execute the BDD tests defined in the features directory.

### Explanation of the Test Steps

- **Given I set “ProductUpdatedEvent” kafka message document**: Loads the Kafka message document (e.g., `ProductUpdatedEvent.json`) from the `tests/data/` directory.
- **Given I start kafka consumer for topic “product-integration-topic” with “product-consumer-group-journey” group name**: Starts a Kafka consumer for the specified topic and consumer group.
- **When I send message to kafka “product-domain-topic” topic**: Sends a message to the specified Kafka topic.
- **Then I should see “product-integration-topic” event on “product-consumer-group-journey” group name in kafka**: Verifies that an event is received on the specified topic and consumer group.

## Notes

- Make sure Docker and Docker Compose are installed on your machine.
- The topics **product-domain-topic** and **product-integration-topic** are automatically created during startup by the
  kafka-create-topics service.
- The consumer is set to automatically listen to the **product-domain-topic** and send transformed messages to the
  **product-integration-topic**.