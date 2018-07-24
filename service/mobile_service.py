from flask import g
from bson.json_util import dumps

class MobileService:
    def __init__(self):
        pass

    @staticmethod
    def login(email, password):
        user = g.mongo.user.find({"email":email,"password":password})
        # user["id"]  = user._id.inserted_id
        return user

    @staticmethod
    def registerUser(firstName, lastName, age, sex, pincode, college, email, password):
        user = {"firstName":firstName,"lastName":lastName, "age":age, "sex":sex, "pincode":pincode, "college":college, "email":email, "password":password}
        user_id = g.mongo.user.insert_one(user)
        user["id"] = str(user_id.inserted_id)
        return user

    @staticmethod
    def fetchSymptomsForPincode(pincode):
        userList = g.mongo.user.find({"pincode":pincode})
        return dumps(userList)

    @staticmethod
    def fetchSymptomsForUser(firstName, lastName):
        user = g.mongo.user.find({"firstName":firstName, "lastName":lastName})
        return dumps(user)

    @staticmethod
    def fetchSymptomsForCollege(college):
        userList = g.mongo.user.find({"college": college})
        return dumps(userList)


    @staticmethod
    def storeDoctorsVerdict(verdict,firstName, lastName):
        user = g.mongo.user.find({"firstName":firstName, "lastName":lastName})
        #adding additional field in the existing table
        g.mongo.user.update({"firstName":firstName}, {"lastName":lastName},{"$set":{"label":verdict}})
        return 1

    @staticmethod
    def getQuestions():
        return {
            "test":"yo"
        }
