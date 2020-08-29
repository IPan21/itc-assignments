import os
from db.dataLayer import DataLayer
from flask_cors import CORS, cross_origin
from model.student import Student
from model.student import skills
from db.customEncoder import CustomEncoder
from flask import Flask, request, make_response, json, jsonify
import datetime
from json import dumps
from flask_pymongo import PyMongo
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from model.validation import Validate

app = Flask(__name__)
CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'


validate = Validate()


app.config['MONGO_hogwarts'] = 'reactloginreg'
# app.config['MONGO_URI'] = 'mongodb://heroku...' # change it
app.config['MONGO_URI'] = 'mongodb://heroku...' # change it
app.config['JWT_SECRET_KEY'] = 'secret' # change it

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

data = DataLayer(app)


@app.route('/users/register', methods=["POST"])
@cross_origin()
def register():
    users = mongo.db.users
    first_name = request.get_json()['first_name']
    last_name = request.get_json()['last_name']
    email = request.get_json()['email']
    password = bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')
    created = datetime.utcnow()
    user_id = users.insert({
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,
        'created': created
    })
    new_user = users.find_one({'_id': user_id})
    result = {'email': new_user['email'] + ' registered'}
    return jsonify({'result': result})


@app.route('/users/login', methods=['POST'])
@cross_origin()
def login():
    users = mongo.db.users
    email = request.get_json()['email']
    password = request.get_json()['password']
    # result = ""
    response = users.find_one({'email': email})
    if response:
        if bcrypt.check_password_hash(response['password'], password):
            access_token = create_access_token(identity={
                'first_name': response['first_name'],
                'last_name': response['last_name'],
                'email': response['email']
            })
            result = jsonify({'token': access_token})
        else:
            result = jsonify({"error": "Invalid username and password"})
    else:
        result = jsonify({"result": "No results found"})
    return result


def from_db_to_json(status=200, indent=4, sort_keys=True, **kwargs):
    response = make_response(dumps(dict(**kwargs), indent=indent, sort_keys=sort_keys, cls=CustomEncoder))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['mimetype'] = 'application/json'
    response.status_code = status
    return response


@app.route("/students")
def get_all_students():
    students = data.get_all_students()
    resp = app.response_class(response=students,
                              status=200,
                              mimetype="application/json")
    return resp


@app.route("/student/<name>")
def get_student_by_name(name):
    student = data.get_student_by_name(name)
    return from_db_to_json(result=student)


@app.route("/student-by-id/<_id>")
def get_student_by_id(_id):
    print(_id)
    try:
        validate.validate_id(_id)
    except Exception as e:
        resp = app.response_class(response=json.dumps({'Error': str(e)}),
                                  status=400,
                                  mimetype="application/json")
        return resp
    student = data.get_student_by_id(_id)
    return from_db_to_json(result=student)


@app.route('/update-student/<student_id>', methods=['GET', 'POST'])
def update_student(student_id):
    try:
        validate.validate_id(student_id)
    except Exception as e:
        resp = app.response_class(response=json.dumps({'Error': str(e)}),
                                  status=400,
                                  mimetype="application/json")
        return resp
    try:
        new_student = dict(request.form)
        new_student = list(new_student)[0]
        new_student = json.loads(new_student)
        dict_to_update = {}
        for key in new_student:
            if new_student[key]:
                dict_to_update.update({key: new_student[key]})
        updated = data.update_student(student_id, dict_to_update)
        if updated.modified_count > 0:
            res = app.response_class(response=json.dumps({'Status': 'Student with id {} updated'.format(student_id)}),
                                     status=200,
                                     mimetype="application/json")
            data.clear_cache()
            return res
        else:
            res = app.response_class(response=json.dumps({'Error': 'no student with id {}'.format(student_id)}),
                                     status=400,
                                     mimetype="application/json")
            return res
    except Exception as e:
        return "Wrong form data format" + str(e) + ' . Accepted format: {{ key: "value", key: "value", etc. }}'


@app.route("/add-student", methods=['GET', 'POST'])
def add_student():
    try:
        d = request.form
        print(d)
        new_student = dict(request.form)
        new_student = list(new_student)[0]
        new_student = json.loads(new_student)
        new_student = Student(new_student)
        if validate.validate_student(new_student.to_dict()):
            data.add_student(new_student.to_dict())
            resp = app.response_class(response=new_student.to_json(),
                                      status=200,
                                      mimetype="application/json")
            data.clear_cache()
            return resp
        else:
            response = app.response_class(response=json.dumps({'Error': "wrong student format"}), status=400,
                                          mimetype="application/json")
            return response
    except Exception as e:
        return "Wrong form data format" + str(e) + ' . Accepted format: {{ key: "value", key: "value", etc. }}'


@app.route("/remove-student/<student_id>", methods=['DELETE'])
def remove_student_by_id(student_id):
    print(student_id)
    try:
        validate.validate_id(student_id)
    except Exception as e:
        resp = app.response_class(response=json.dumps({'Error': str(e)}),
                                  status=400,
                                  mimetype="application/json")
        return resp
    removed = data.remove_student(student_id)
    if removed.deleted_count > 0:
        print("here")
        res = app.response_class(response=json.dumps({'Status': 'Student with id {} removed'.format(student_id)}),
                                 status=200,
                                 mimetype="application/json")
        return res
    else:
        res = app.response_class(response=json.dumps({'Error': 'no student with id {}'.format(student_id)}),
                                 status=400,
                                 mimetype="application/json")
        return res


@app.route("/student-by-date/<date>")
def get_students_by_date(date):
    try:
        validate.validate_date(date)
    except Exception as e:
        resp = app.response_class(response=json.dumps({'Error': str(e)}),
                                  status=400,
                                  mimetype="application/json")
        return resp
    count = data.get_students_by_day(date)
    resp = app.response_class(response=json.dumps({'total': str(count)}),
                              status=200,
                              mimetype="application/json")
    return resp


@app.route("/student-by-month/<month>,<year>")
def get_students_by_month(month, year):
    try:
        validate.validate_month_year(month, year)
    except Exception as e:
        resp = app.response_class(response=json.dumps({'Error': str(e)}),
                                  status=400,
                                  mimetype="application/json")
        return resp
    count = data.get_students_by_month(int(month), int(year))
    resp = app.response_class(response=json.dumps({'total': str(count)}),
                              status=200,
                              mimetype="application/json")
    return resp


@app.route("/desired-skills-pie-data/<skill_type>")
def get_desired_skills_pie_data(skill_type):
    print(skill_type)
    try:
        validate.validate_skill_type(skill_type)
    except Exception as e:
        resp = app.response_class(response=json.dumps({'Error': str(e)}),
                                  status=400,
                                  mimetype="application/json")
        return resp
    labels = []
    pie_data = []
    for i in skills:
        if skill_type == "desired":
            result = data.students_want_skill(i)
            if result:
                pie_data.append((result[0]['matching_students']))
                labels.append(i)
        elif skill_type == "existing":
            result = data.students_have_skill(i)
            if result:
                pie_data.append((result[0]['matching_students']))
                labels.append(i)
        else:
            return 'something went wrong'
    return {"labels": labels, 'data': pie_data}


@app.route("/desired-courses-pie-data/")
def get_desired_courses_pie_data():
    labels = []
    pie_data = []
    result = data.find_most_desired_courses()
    res = (list(result))
    for i in res:
        labels.append(i['_id'])
        pie_data.append(i['count'])
    return {"labels": labels, 'data': pie_data}


if __name__ == "__main__":
    # port = int(os.environ.get('PORT', 5000))
    # app.run(host='0,0,0,0', port=port)
    app.run()
