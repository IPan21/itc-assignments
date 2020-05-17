import json
import datetime


class BasePost(dict):
    def __init__(self, userId, id, title, body, createdAt):
        dict.__init__(self, userId=userId, id=id, title=title, body=body, createdAt=createdAt)
        self.userId = userId
        self.id = id
        self.title = title
        self.body = body
        self.createdAt = createdAt


class ExtendedPost(BasePost):

    def __init__(self, userId, id, title, body, createdAt):
        super().__init__(userId, id, title, body, createdAt)

    def creation_date():
        # return datetime.datetime.now().isoformat()
        return datetime.datetime.now().strftime("%d-%m-%Y")


class JsonablePost(ExtendedPost):
    def to_json(self):
        return json.dumps(self, lambda o: o.__dict__)

    def __init__(self, userId, id, title, body, createdAt):
        super().__init__(userId, id, title, body, createdAt)


class Comment(dict):
    def __init__(self, comment_id, name, email, body):
        dict.__init__(self, id=comment_id, name=name, email=email, body=body)
        self.id = comment_id
        self.name = name
        self.email = email
        self.body = body