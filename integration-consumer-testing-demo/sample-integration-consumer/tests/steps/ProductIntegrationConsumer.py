import json
import os
import sys
from threading import Thread

from behave import *

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

from helper.assertion import assert_equal
from util.connect_kafka import send_kafka_message, start_kafka_consumer_in_stretch


@given('I set "{doc_id}" kafka message document')
def step_impl(context, doc_id):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(current_dir, '../data/', f'{doc_id}.json')
    with open(data_file_path, 'r') as c:
        context.kafka_message = json.load(c)


@given('I start kafka consumer for topic "{topic}" with "{consumer_group}" group name')
def step_impl(context, topic, consumer_group):
    context.messages = {consumer_group: []}
    context.consumer_thread = Thread(target=start_kafka_consumer_in_stretch,
                                     args=(topic, context.kafka_message['id'], consumer_group,
                                           context.messages[consumer_group]))
    context.consumer_thread.start()


@when('I send message to kafka "{topic}" topic')
def step_impl(context, topic):
    send_kafka_message(topic, context.kafka_message, context.kafka_message['id'])


@then('I should see "{topic}" event on "{consumer_group}" group name in kafka')
def step_impl(context, topic, consumer_group):
    context.consumer_thread.join()

    assert len(context.messages[consumer_group]) > 0, "No messages were consumed"
    consumed_key, consumed_value = context.messages[consumer_group][0]
    assert_equal(consumed_key, context.kafka_message["id"])
    assert_equal(consumed_value["product_id"], context.kafka_message["id"])
    assert_equal(consumed_value["product_name"], context.kafka_message["name"])
    assert_equal(consumed_value["description"], context.kafka_message["description"])
    assert_equal(consumed_value["price"], context.kafka_message["price"])
    assert_equal(consumed_value["status"], "Processed")
