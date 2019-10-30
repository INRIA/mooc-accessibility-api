import json
import os
from http import HTTPStatus
from flask import Flask
from flask import request
from elasticsearch import Elasticsearch


app = Flask(__name__)


def from_request(req):
    return {
        'user_id': req['userId'],
        'event_name': req['eventName'],
        'player': req['player'],
        'preferences': req['preferences'],
        'media_id': req['mediaId'],
        'created_at': req['createdAt']
    }


def save_event(player_event):
    es = Elasticsearch([os.getenv('ELASTICSEARCH_HOST')])
    es_index = os.getenv('ELASTICSEARCH_EVENTS_INDEX')

    return es.index(
        index=f'events_{es_index}',
        doc_type='_doc',
        body=player_event
    )


@app.route('/api/logs', methods=['POST'])
def create_player_event():
    req = json.loads(request.data)
    player_event = from_request(req)
    es_response = save_event(player_event)
    if es_response['result']:
        return '', HTTPStatus.CREATED
    else:
        return '', HTTPStatus.NO_CONTENT
