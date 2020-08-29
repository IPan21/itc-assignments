
from model.student import Student
import mysql.connector


class MySQLDataLayer:

    def __init__(self):
        self.db = mysql.connector.connect(host='localhost', database="hogwarts", user='root', password='Arte2109')

    def add_student(self, student):
        new_student = Student(student)
        new_student = new_student.to_dict()
        vals = list(new_student.values())
        mysql_insert_query = """INSERT INTO students (first_name, 
                                        last_name, 
                                        existing_magic_skills, 
                                        desired_magic_skills, 
                                        interested_in_course, 
                                        creation_time) 
                               VALUES 
                               (%s, %s, %s, %s, %s, %s)"""
        cursor = self.db.cursor()
        cursor.execute(mysql_insert_query, vals)
        self.db.commit()
        print(cursor.rowcount, "Record inserted successfully into hogwarts table")
        cursor.close()


    # def add_student(self, student):
    #     new_student = Student(student)
    #     added_student = self.__db.students.insert_one(new_student.to_dict())
    #     result_student = self.__db.students.find_one({'first_name': new_student['first_name']})
    #     print(list(dict(result_student)))
    #     self.__cache.set(student['_id'], student, timeout=30)
    #     self.__cache.delete("all_students")
    #     return added_student




