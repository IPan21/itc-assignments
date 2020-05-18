import json
from flask import Flask, request, jsonify
import requests
from model.DataObj import Instrument, User
import random
import string
import datetime

app = Flask(__name__)


def time_now():
    return datetime.datetime.now().isoformat()


def random_string(string_length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


music_instruments = [
    {
        'id': "a",
        'type': 'percussion',
        'name': 'drums',
        'last_accessed': '',
        'created_at': ''
    },
    {
        'id': "b",
        'type': 'strings',
        'name': 'violin',
        'last_accessed': '',
        'created_at': ''
    }
]

users = [
    {
        'user_id': "a",
        'user_name': 'Alex',
        'instruments': ["a", "b"],
        'last_accessed': '',
        'created_at': ''
    },
    {
        'user_id': "b",
        'user_name': 'David',
        'instruments': [],
        'last_accessed': '',
        'created_at': ''
    }
]





@app.route("/")
def get_all_instruments():
    try:
        return jsonify({'music_instruments': music_instruments})
    except Exception as e:
        return e


@app.route("/users/<user_id>")
def get_instruments_by_user_id(user_id):
    try:
        instruments_ids = []
        search_result = []
        for i in users:
            if i['user_id'] == user_id:
                instruments_ids = i['instruments']
        for instrument_id in instruments_ids:
            for item in music_instruments:
                if item['id'] == instrument_id:
                    item['last_accessed'] = time_now()
                    search_result.append(item)
        response = jsonify({'user_' + user_id + '_instruments': search_result})
        return response
    except Exception as e:
        return e


@app.route("/<instrument_id>")
def get_instrument_by_id(instrument_id):
    try:
        instrument_to_find = []
        for i in music_instruments:
            if i['id'] == instrument_id:
                i['last_accessed'] = time_now()
                instrument_to_find = i
        return jsonify({instrument_id: instrument_to_find})
    except Exception as e:
        return e


@app.route("/instruments/<new_instrument_name>", methods=['POST'])
def add_instrument(new_instrument_name):
    try:
        for i in music_instruments:
            if i['name'] == new_instrument_name:
                return 'instrument already exists'
        instrument_id = random_string()
        date = time_now()
        new_instrument = Instrument(instrument_id, new_instrument_name, date, date)
        music_instruments.append(new_instrument)
        return jsonify({'music_instruments': music_instruments})
    except Exception as e:
        return e


@app.route("/instruments/<instrument_id>/user/<user_id>", methods=['POST'])
def assign_instrument_to_user(instrument_id, user_id):
    try:
        instrument_id_exists = 0
        for item in music_instruments:
            if item['id'] == instrument_id:
                instrument_id_exists += 1
        if instrument_id_exists == 0:
            return "instrument with id " + instrument_id + " doesn't exist"
        for i in users:
            if i['user_id'] == user_id:
                if instrument_id not in i['instruments']:
                    date = time_now()
                    i['last_accessed'] = date
                    i['instruments'].append(instrument_id)
                    print(jsonify({'users': users}))
                    return jsonify({'users': users})
                else:
                    return 'instrument is already assigned'
        return 'something went wrong'
    except Exception as e:
        return e

# https://youtu.be/T0gl9LXq3LA


@app.route("/instruments/<instrument_id>/link/<youtube_link>", methods=['POST'])
def add_youtube_link_to_instrument(instrument_id, youtube_link):
    try:
        instrument_id_exists = 0
        for item in music_instruments:
            if item['id'] == instrument_id:
                date = time_now()
                item['last_accessed'] = date
                item['video'] = youtube_link
                return 'video added'
        if instrument_id_exists == 0:
            return "instrument with id " + instrument_id + " doesn't exist"
    except Exception as e:
        return e


# {
# 	"user":{
# 		"name": "Anna",
# 		"instruments": []
# 	}
# }

@app.route("/users", methods=['POST'])
def add_user():
    try:
        content = request.json
        user_name = content['user']["name"]
        user_instruments = content['user']["instruments"]
        user_id = random_string()
        date = time_now()
        new_user = User(user_id, user_name, user_instruments, date, date)
        users.append(new_user)
        return jsonify({'users': users})
    except Exception as e:
        return e


if __name__ == "__main__":
    app.run()

