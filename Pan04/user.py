
import csv
from logger import Logger


class User:

    @staticmethod
    def user_auth(name, password):
        try:
            with open("users.csv", "r") as f:
                creader = csv.DictReader(f, delimiter=",")
                for row in creader:
                    if name == row['first'] and password == row['password']:
                        print("name and password are correct")
                        if row['role']:
                            return row['role']
                        else:
                            return False
                print('wrong name or password')
        except Exception as e:
            print(e)
            Logger.add_to_log(e)


User.user_auth("Donald", "pass4")
User.user_auth(56, "pass4")
