import pymongo
from bson import ObjectId
from bson.json_util import dumps
from model.student import Student
import datetime
import calendar
from model.validation import Validate
from flask_caching import Cache

validate = Validate()


class DataLayer:

    def __init__(self, app):
        self.__client = pymongo.MongoClient('localhost', 27017)
        self.__db = self.__client["hogwarts"]
        self.__users = self.__client["hogwarts"]
        cache = Cache(config={'CACHE_TYPE': 'simple', 'CACHE_THRESHOLD': 1000})
        cache.init_app(app)
        self.__cache = cache

    def get_all_students(self):
        all_students = self.__cache.get("all_students")
        if all_students:
            return all_students
        else:
            students = dumps(self.__db.students.find())
            self.__cache.set("all_students", students, timeout=30)
            return students

    def add_student(self, student):
        new_student = Student(student)
        added_student = self.__db.students.insert_one(new_student.to_dict())
        result_student = self.__db.students.find_one({'first_name': new_student['first_name']})
        print(list(dict(result_student)))
        self.__cache.set(student['_id'], student, timeout=30)
        self.__cache.delete("all_students")
        return added_student

    def get_student_by_name(self, first_name):
        student = self.__db.students.find_one({"first_name": first_name})
        return student

    def get_student_by_id(self, student_id):
        cached_student = self.__cache.get(student_id)
        if cached_student:
            return cached_student
        else:
            student = self.__db.students.find_one({"_id": ObjectId(student_id)})
            if student:
                self.__cache.set(student_id, student, timeout=30)
            return student

    def remove_student(self, student_id):
        self.__cache.delete(student_id)
        student_to_remove = self.__db.students.delete_one({"_id": ObjectId(student_id)})
        return student_to_remove

    def clear_cache(self):
        self.__cache.clear()

    def update_student(self, student_id, data):
        self.__cache.delete(student_id)
        data.update({"last_update_time": datetime.date.today().isoformat()})
        dict_to_update = {'$set': data}
        student = self.__db.students.update_one({"_id": ObjectId(student_id)}, dict_to_update)
        self.__cache.delete("all_students")
        return student

    def get_students_by_day(self, date):
        student_by_date = self.__db.students.aggregate([{'$match': {"creation_time": date}}])
        count = (len(list(student_by_date)))
        return count

    def get_students_by_month(self, month, year):
        num_days_in_month = calendar.monthrange(year, month)[1]
        start_date = str(datetime.date(year, month, 1))
        end_date = str(datetime.date(year, month, num_days_in_month))
        students_matching_search = self.__db.students.aggregate(
            [{'$match': {"creation_time": {'$gte': start_date, '$lt': end_date}}}])
        students_created_in_date = []
        for student in students_matching_search:
            student['_id'] = str(student['_id'])
            students_created_in_date.append(student)
        return len(students_created_in_date)

    def students_want_skill(self, skill):
        res = self.__db.students.aggregate(
            [{'$match': {"desired_magic_skills": skill}}, {'$count': 'matching_students'}])
        result = []
        for i in res:
            result.append(i)
        return result

    def students_have_skill(self, skill):
        res = self.__db.students.aggregate(
            [{'$match': {"existing_magic_skills": skill}}, {'$count': 'matching_students'}])
        result = []
        for i in res:
            result.append(i)
        return result

    def find_most_desired_courses(self):
        res = self.__db.students.aggregate([
            {'$unwind': "$interested_in_course"},
            {'$group': {"_id": "$interested_in_course", "count": {'$sum': 1}}}
        ])
        return res
