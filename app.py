import json
from http import HTTPStatus
from flask import Flask
from flask import request

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


@app.route('/api/logs', methods=['POST'])
def create_player_event():
    req = json.loads(request.data)
    player_event = from_request(req)
    return '', HTTPStatus.NO_CONTENT
