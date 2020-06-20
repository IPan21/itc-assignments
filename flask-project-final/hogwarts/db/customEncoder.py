from json import JSONEncoder
from bson.objectid import ObjectId


class CustomEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        elif set(['first_name',
                  'last_name',
                  'existing_magic_skills',
                  'desired_magic_skills',
                  'interested_in_course',
                  'creation_time',
                  'last_update_time']).intersection(dir(obj)):
            return str(obj)
        elif hasattr(obj, 'next'):
            return list(obj)
        return JSONEncoder.default(self, obj)