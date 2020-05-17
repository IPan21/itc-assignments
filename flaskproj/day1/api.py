import json
from os import abort
from flask import Flask
import requests
from model.DataObj import JsonablePost, Comment
app = Flask(__name__)


# @app.route("/")
# def get_posts():
#     posts = requests.get('https://jsonplaceholder.typicode.com/posts')
#     posts_in_json = posts.json()
#     response = app.response_class(response=json.dumps(posts_in_json), status=200, mimetype="application/json")
#     return response


def get_posts():
    posts_response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if posts_response.status_code != 200:
        abort(404)

    posts = posts_response.json()
    # print(posts)
    data = {}
    for index in range(len(posts)):
        post_args = []
        for key in posts[index]:
            post_args.append(posts[index][key])
        post_data = JsonablePost(post_args[0], post_args[1], post_args[2], post_args[3], JsonablePost.creation_date())
        if int(post_args[1]) < 10:
            response = requests.get('https://jsonplaceholder.typicode.com/posts/' + str(post_args[1]) + "/comments")
            response_json = response.json()
            comment_list = []
            for i in response_json:
                c_item=[]
                for key in i:
                    c_item.append(i[key])
                comment_data = Comment(c_item[0], c_item[1], c_item[2], c_item[3])
                comment_list.append(comment_data)
            post_comments = {post_args[1]: comment_list}
            post_data.update(post_comments)
        add_id_to_object = {post_args[1]: post_data}
        data.update(add_id_to_object)
    return data


@app.route("/")
def get_all_posts():
    data = get_posts()
    response = app.response_class(
        response=json.dumps(data, indent=4),
        status=200,
        mimetype='application/json')
    return response

# @app.route("/")
# def get_posts():
#     posts_response = requests.get('https://jsonplaceholder.typicode.com/posts')
#     if posts_response.status_code != 200:
#         abort(404)
#
#     posts = posts_response.json()
#     # print(posts)
#     data = {}
#     for index in range(len(posts)):
#         post_args = []
#         for key in posts[index]:
#             post_args.append(posts[index][key])
#         post_data = JsonablePost(post_args[0], post_args[1], post_args[2], post_args[3], JsonablePost.creation_date())
#         if int(post_args[1]) < 10:
#             response = requests.get('https://jsonplaceholder.typicode.com/posts/' + str(post_args[1]) + "/comments")
#             response_json = response.json()
#             comment_list = []
#             for i in response_json:
#                 c_item=[]
#                 for key in i:
#                     c_item.append(i[key])
#                 comment_data = Comment(c_item[0], c_item[1], c_item[2], c_item[3])
#                 comment_list.append(comment_data)
#             post_comments = {post_args[1]: comment_list}
#             post_data.update(post_comments)
#         add_id_to_object = {index: post_data}
#         data.update(add_id_to_object)
#     response = app.response_class(
#         response=json.dumps(data, indent=4),
#         status=200,
#         mimetype='application/json'
#     )
#     return response


@app.route("/<id>")
def get_post_by_id(id):
    data = get_posts()
    response = app.response_class(
        response=json.dumps(data[int(id)], indent=4),
        status=200,
        mimetype='application/json')
    return response

# @app.route("/<id>")
# def get_post_by_id(id):
#     post_response = requests.get('https://jsonplaceholder.typicode.com/posts/' + id)
#     post = post_response.json()
#     response = app.response_class(response=json.dumps(post), status=200, mimetype="application/json")
#     return response


@app.route("/users/<userId>")
def get_post_by_user_id (userId):
    data = get_posts()
    result_list = {}
    for i in data.values():
        if i['userId'] == int(userId):
            result_list.update(i)
            print(i)
    response = app.response_class(
        response=json.dumps(result_list, indent=4),
        status=200,
        mimetype='application/json')
    return response

# @app.route("/users/<userId>")
# def get_post_by_user_id (userId):
#     post_response = requests.get('https://jsonplaceholder.typicode.com/posts?userId=' + userId)
#     post = post_response.json()
#     response = app.response_class(response=json.dumps(post), status=200, mimetype="application/json")
#     return response

@app.route("/comments/<id>")
def get_nested_comments_by_post_id(id):
    data = get_posts()
    response = app.response_class(
        response=json.dumps(data[int(id)][int(id)], indent=4),
        status=200,
        mimetype='application/json')
    return response

# @app.route("/comments/<id>")
# def get_nested_comments_by_post_id(id):
#     post_response = requests.get('https://jsonplaceholder.typicode.com/posts/' + id + "/comments")
#     post = post_response.json()
#     response = app.response_class(response=json.dumps(post), status=200, mimetype="application/json")
#     return response


if __name__ == "__main__":
    app.run()

