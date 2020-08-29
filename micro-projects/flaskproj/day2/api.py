import json
from flask import Flask, request, jsonify, flash, redirect, send_file, render_template, url_for
from model.DataObj import Instrument, User
import random
import string
import datetime
import time
from werkzeug.utils import secure_filename
import os.path
import io
from wtforms import Form, BooleanField, StringField, PasswordField, validators
import threading

app = Flask(__name__)
app.secret_key = os.urandom(24)

timer = None


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user_id = random_string()
        date = time_now()
        user = User(user_id, form.username.data, form.password.data, date, date)
        users.append(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


def time_now():
    return datetime.datetime.now().isoformat()


def random_string(string_length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


# music_instruments = [
#     {
#         'id': "a",
#         'type': 'percussion',
#         'name': 'drums',
#         'last_accessed': '',
#         'created_at': ''
#     },
#     {
#         'id': "b",
#         'type': 'strings',
#         'name': 'violin',
#         'last_accessed': '',
#         'created_at': '',
#         'image': ['1.jpg']
#     }
# ]

# users = [
#     {
#         'user_id': "a",
#         'user_name': 'Alex',
#         'instruments': ["a", "b"],
#         'last_accessed': '',
#         'created_at': ''
#     },
#     {
#         'user_id': "b",
#         'user_name': 'David',
#         'instruments': [],
#         'last_accessed': '',
#         'created_at': ''
#     }
# ]

users = []
music_instruments = []

# with open('data/users.json', 'w') as outfile:
#     json.dump(users, outfile)
# with open('data/instruments.json', 'w') as outfile:
#     json.dump(music_instruments, outfile)

with open('data/users.json') as file:
    users = json.load(file)
    print(users)

with open('data/instruments.json') as file:
    music_instruments = json.load(file)
    print(music_instruments)


def update():
    while True:
        with open('data/users.json', 'w') as outfile:
            json.dump(users, outfile)
        with open('data/instruments.json', 'w') as outfile:
            json.dump(music_instruments, outfile)
        time.sleep(10)


UPD_THREAD = threading.Thread(target=update)
UPD_THREAD.daemon = True  # main can exit while thread is still running
UPD_THREAD.start()


@app.route("/login")
def login():
    try:
        return jsonify({'users': users})
    except Exception as e:
        return e


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
        global users
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

# example: instruments?query=violin
@app.route("/instruments")
def search_instrument_by_name():
    try:
        t = time.process_time()
        instrument = request.args.get('query')
        result = {}
        instrument_to_find = []
        for i in music_instruments:
            if i['name'] == instrument:
                i['last_accessed'] = time_now()
                instrument_to_find.append(i)
        result['search_result'] = instrument_to_find
        elapsed_time = time.process_time() - t
        result['search_duration_time'] = elapsed_time
        print(result)
        return result
    except Exception as e:
        return e

# Key:  type data, and afterward choose in the right dropdown file
# Value: choose file


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# example: upload?instruments=drums
@app.route('/upload', methods=['POST'])
def upload_img():
    try:
        if 'data' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['data']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            instrument = request.args.get('instruments')
            print(instrument)
            count = 0
            for i in music_instruments:
                if i['name'] == instrument:
                    count += 1
                    i['last_accessed'] = time_now()
                    if 'image' in i:
                        if len(i['image']) > 1:
                            return "instrument can contain max 2 images"
                        else:
                            file.save('images/' + filename)
                            i['image'].append(filename)
                    else:
                        file.save('images/' + filename)
                        my_list = [filename]
                        i['image'] = my_list
        if count == 0:
            return "no such instrument"
        print(music_instruments)
        response = app.response_class(
            response=json.dumps({"status": "ok"}),
            status=200,
            mimetype='application/json'
        )
        return response
    except Exception as e:
        return e


# example: image?instruments=violin
@app.route("/image")
def show_instrument_image():
    try:
        instrument = request.args.get('instruments')
        count = 0
        for i in music_instruments:
            if i['name'] == instrument:
                count += 1
                i['last_accessed'] = time_now()
                if 'image' in i:
                    with open(os.path.join('images', i['image'][0]), "rb") as bites:
                        return send_file(
                            io.BytesIO(bites.read()),
                            attachment_filename='logo.jpeg',
                            mimetype='image/jpg'
                        )
                else:
                    return 'instrument ' + instrument + ' has no images'
        if count == 0:
            return 'no instrument with name ' + instrument + ' found'
    except Exception as e:
        return e


@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user_by_id(user_id):
    try:
        global users
        print(users)
        num_items = len(users)
        new_list = [i for i in users if not (i['user_id'] == user_id)]
        if num_items > len(new_list):
            users = new_list
            response = app.response_class(
                response=json.dumps({"status": "ok"}),
                status=200,
                mimetype='application/json'
            )
            return response
            # return jsonify({'users': users})
        else:
            return "user " + user_id + " doesn't exist"
    except Exception as e:
        return e


@app.route('/user/<user_id>/instrument/<instrument_id>', methods=['DELETE'])
def delete_instrument_from_user(user_id, instrument_id):
    try:
        count = 0
        for i in users:
            if i['user_id'] == user_id:
                count += 1
                if instrument_id in i['instruments']:
                    i['instruments'].remove(instrument_id)
                    return jsonify({'users': users})
                else:
                    return "instrument with  " + user_id + " not found"
        if count == 0:
            return "user " + user_id + " doesn't exist"
    except Exception as e:
        return e


if __name__ == "__main__":
    app.run()


