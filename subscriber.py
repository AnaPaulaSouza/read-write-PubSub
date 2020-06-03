import os
import ipdb
import json
from google.cloud import pubsub_v1

def sub_msg():
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path('bee-bit-tech-2', 'mike')

    def callback(message):
        print(message.data)
        message.ack()

    future = subscriber.subscribe(subscription_path, callback=callback)

def sub_conversa():
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path('bee-bit-tech-2', 'conversa-ana')

    def callback(message):
        print(message.data)
        message.ack()

    future = subscriber.subscribe(subscription_path, callback=callback)

def sub_criar(project_id='bee-bit-tech-2', topic='conversa', sub_name='conversa-mike'):
    ipdb.set_trace()
    subscriber = pubsub_v1.SubscriberClient()
    topic_path = subscriber.topic_path(project_id, topic)
    subscription_path = subscriber.subscription_path(project_id, sub_name)

    subscription = subscriber.create_subscription(
        subscription_path, topic_path
    )

    print("Subscription created: {}".format(subscription))

def sub_msg_json(project_id='bee-bit-tech-2', topic='souza'):
    subscriber = pubsub_v1.SubscriberClient()
    topic_path = subscriber.topic_path(project_id, topic)
    subscription_path = subscriber.subscription_path(project_id, topic)

    def callback(message):
        print(message)
        message.ack()

        data = message.data.decode()
        json_data = json.loads(data)
        print(type(json_data))
        print(json_data)
    future = subscriber.subscribe(subscription_path, callback=callback)

def read_file_json(project_id='bee-bit-tech-2', topic='conversa-ana'):
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, topic)

    def callback(line):
        data = line.data.decode()
        json_data = json.loads(data)
        print(json_data)

    future = subscriber.subscribe(subscription_path, callback=callback)

def texttosub(project_id='bee-bit-tech-2', topic='texttosub-ana'):
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, topic)

    def callback(message):
        print(message.data)
        message.ack()

    future = subscriber.subscribe(subscription_path, callback=callback)






