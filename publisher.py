import os
import json
from typing import TextIO

from pprint import pprint
from google.cloud import pubsub_v1


def pub_msg(project_id='bee-bit-tech-2', topic='ana'):
    publisher = pubsub_v1.PublisherClient()
    topic_name = publisher.topic_path(project_id, topic)
    publisher.publish(topic_name, b'My test!', spam='eggs')

#envia para o marcio
def pub_conversa():
    publisher = pubsub_v1.PublisherClient()
    # topic_name = 'projects/{project_id}/topics/{topic}'.format(
    topic_name = 'projects/bee-bit-tech-2/topics/conversa'.format(
        project_id='bee-bit-tech-2',
        topic='conversa',
    )
    publisher.publish(topic_name, b'Hello bob?!', spam='eggs')


def pub_criar(project_id='bee-bit-tech-2', topic='ana'):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic)
    topic = publisher.create_topic(topic_path)

    print("Topic created: {}".format(topic))


def pub_listar():
    publisher = pubsub_v1.PublisherClient()
    project_path = publisher.project_path('bee-bit-tech-2')

    for topic in publisher.list_topics(project_path):
        print(topic)


def pub_msg_json(project_id='bee-bit-tech-2', topic='conversa'):
    publisher = pubsub_v1.PublisherClient()

    topic_name = publisher.topic_path(project_id, topic)
    data_json = {"nome": "Mike", "idade": 7}
    message = json.dumps(data_json)
    message = message.encode('utf-8')

    publisher.publish(topic_name, message)


def read_file_json(project_id='bee-bit-tech-2', topic='conversa'):
    publisher = pubsub_v1.PublisherClient()
    topic_name = publisher.topic_path(project_id, topic)

    with open('/home/ana/Downloads/events_navigation.jpg', 'r') as file:

        data = file.readlines()

    for line in data:
        aux = line.encode()
        future = publisher.publish(topic_name, data=aux)
        #print(future.result())


def texttopub(project_id='bee-bit-tech-2', topic='TextToPubSub-Ana'):
    publisher = pubsub_v1.PublisherClient()
    topic_name = publisher.topic_path(project_id, topic)

    publisher.publish(topic_name, b'Teste TextToPubSub!!!!', spam='eggs')