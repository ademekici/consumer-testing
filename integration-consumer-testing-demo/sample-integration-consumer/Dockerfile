FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the sample-integration-consumer script
COPY consumer.py .

# Set environment variables (can be overridden by Docker Compose)
ENV KAFKA_BROKER=kafka:9092
ENV INPUT_TOPIC=input_topic
ENV OUTPUT_TOPIC=output_topic
ENV GROUP_ID=my_consumer_group

# Run the sample-integration-consumer
CMD ["python", "consumer.py"]