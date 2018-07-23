from flask import Flask, g, request
from flask.json import jsonify
from pymongo import MongoClient
from flask_pymongo import PyMongo

app = Flask(__name__)

from service.mobile_service import MobileService

app.config["MONGO_URI"] = "mongodb://localhost:27017/rabans"
mongo = PyMongo(app)

# @app.before_request
# def init_mongo():
#     g.mongo = MongoClient(ConfigService.get_mongo_host(), 27017).rabans


@app.route('/mobile/questions', methods = ['GET'])
def getQuestions():
    return jsonify(MobileService.getQuestions())

@app.route('/mobile/questions', methods = ['POST'])
def postQuestions():
    pass

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)
