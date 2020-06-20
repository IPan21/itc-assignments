import json
import datetime


class Student:

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def to_dict(self):
        return json.loads(json.dumps(self.__dict__))

    def __init__(self, student):
        self.first_name = student['first_name']
        self.last_name = student['last_name']
        self.existing_magic_skills = student['existing_magic_skills']
        self.desired_magic_skills = student['desired_magic_skills']
        self.interested_in_course = student['interested_in_course']
        self.creation_time = datetime.date.today().isoformat()
        self.last_update_time = datetime.date.today().isoformat()


courses = [
    'Muggle Studies',
    'Divination',
    'Ancient Runes',
    'Care of Magical Creatures',
    'Arithmancy',
    'Flying',
    'Defense Against the Dark Arts',
    'Herbology',
    'Astronomy',
    'History of Magic',
    'Potions',
    'Transfiguration',
    'Charms'
];

skills = [
    'Lycanthropy',
    'Veela Charm',
    'Magical Resistance',
    'Parseltongue',
    'Legilimency And Occlumency',
    'Seeing',
    'Wandless Magic',
    'Apparition',
    'Animagus',
    'Metamorphmagi'
];