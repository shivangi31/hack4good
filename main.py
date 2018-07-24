from flask import Flask, g, request
from flask.json import jsonify
from pymongo import MongoClient
from flask_pymongo import PyMongo

app = Flask(__name__)

from service.mobile_service import MobileService
from util.util_service import UtilService

app.config["MONGO_URI"] = "mongodb://localhost:27017/rabans"
mongo = MongoClient("localhost", 27017).rabans
PinCodePath = "./resources/IN.txt"
pincode = {}

def required_param(key):
    if not g.json_body:
        raise Exception("Missing request body")

    if key not in g.json_body:
        raise Exception("Missing required parameter '" + key + "'")

    return g.json_body[key]


@app.before_request
def unwind_json():
    g.json_body = request.get_json(force=True, silent=True)

@app.before_request
def init_mongo():
    g.mongo = mongo


# @app.before_request
# def init_mongo():
#     g.mongo = MongoClient(ConfigService.get_mongo_host(), 27017).rabans

# @app.route('/test')


def initPinCode():
    pincode =  UtilService.pinCodeParser(PinCodePath)

@app.route('/signup', methods = ['POST'])
def signup():
    return jsonify( MobileService.registerUser(required_param("firstName"),required_param("lastName"),required_param("age"),required_param("sex"),required_param("pincode"),required_param("college"),required_param("email"),required_param("password") ))

@app.route('/login', methods = ['POST'])
def login():
    return jsonify(MobileService.login(required_param("email"),required_param("password")))

@app.route('/mobile/questions', methods = ['GET'])
def getQuestions():
    return jsonify(MobileService.getQuestions())

@app.route('/mobile/questions', methods = ['POST'])
def postQuestions():
    pass

@app.route('/mobile/fetch_symptoms_Pincode',methods = ['POST'])
def fetchSymptomsForPincode():
    return jsonify(MobileService.fetchSymptomsForPincode(required_param("Pincode")))

@app.route('/mobile/fetch_symptoms_User',methods = ['POST'])
def fetchSymptomsForUser():
    return jsonify(MobileService.fetchSymptomsForUser(required_param("firstName"),required_param("lastName")))

@app.route('/mobile/fetch_symptoms_College',methods = ['POST'])
def fetchSymptomsForCollege():
    return jsonify(MobileService.fetchSymptomsForCollege(required_param("college")))

@app.route('/mobile/fetch_symptoms_College',methods = ['POST'])
def storeDoctorsVerdict():
    return jsonify(MobileService.storeDoctorsVerdict(required_param("label"),required_param("firstName"),required_param("lastName")))

def dump(obj):
  for attr in dir(obj):
    print("obj.%s = %r" % (attr, getattr(obj, attr)))

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == "__main__":
    initPinCode()
    app.run(debug=True)
