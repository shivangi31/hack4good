class MobileService:
    def __init__(self,db):
        self.mongo=db
        pass

    @staticmethod
    def registerUser(firstName, lastName, age, sex, pincode, college, email, password):
        user = {"firstName":firstName,"lastName":lastName, "age":age, "sex":sex, "pincode":pincode, "colege":college, "email":email, "password":password}
        user_id = self.mongo.user.insert_one(user)
        user["id"] = str(recipe_id.inserted_id)
        return user



    @staticmethod
    def getQuestions():
        return {
            "test":"yo"
        }
