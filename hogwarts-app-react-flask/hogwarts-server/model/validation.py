import bson
from model.student import courses, skills
import datetime


class Validate:

    def __init__(self):
        self.courses = courses
        self.skills = skills

    @staticmethod
    def validate_id(object_id):
        if not bson.objectid.ObjectId.is_valid(object_id):
            raise ValueError("'{}' is an invalid id.".format(object_id))

    @staticmethod
    def validate_student(student):
        if (student['first_name'] and
                student['last_name'] and
                student['existing_magic_skills'] and
                student['desired_magic_skills'] and
                student['interested_in_course']):
            first_name = type(student['last_name']) is str
            first_name_l = len(student['last_name']) >= 1
            last_name = type(student['last_name']) is str
            last_name_l = len(student['last_name']) >= 1
            existing_magic_skills = type(student['existing_magic_skills']) is list
            existing_magic_skills_l = len(student['existing_magic_skills']) >= 1
            desired_magic_skills = type(student['existing_magic_skills']) is list
            desired_magic_skills_l = len(student['existing_magic_skills']) >= 1
            interested_in_course = type(student['existing_magic_skills']) is list
            interested_in_course_l = len(student['existing_magic_skills']) >= 1
            if (first_name and
                    first_name_l and
                    last_name and
                    last_name_l and
                    existing_magic_skills and
                    existing_magic_skills_l and
                    desired_magic_skills and
                    desired_magic_skills_l and
                    interested_in_course and
                    interested_in_course_l):
                return True
        return False

    @staticmethod
    def validate_skill_type(skill):
        if skill != 'desired':
            if skill != 'existing':
                raise ValueError("skill expected to be 'desired' or 'existing'")

    @staticmethod
    def validate_date(date):
        if not datetime.datetime.strptime(date, '%Y-%m-%d'):
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    @staticmethod
    def validate_month_year(month, year):
        if not int(month) < 13 or not int(year) < 3000:
            raise ValueError("Incorrect data format, month should be MM, year should be YYYY")
