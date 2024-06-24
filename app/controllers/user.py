# from run import app
from flask import request, jsonify, flash
# from app.application import db

from flask import Flask
# from run import app
# from flask_pymongo import PyMongo

app = Flask(__name__, template_folder='/home/priscilladunyoh/Personal/instabook/templates')

app.config['SECRET_KEY'] = '689727683effe5980db7ec9af471311b2ebf9c7f'
app.config[
    'MONGO_URI'] = "mongodb+srv://priscilladunyoh99:Q7OXtTY2z66B1vj3@cluster0.gsxghkt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# mongo_client = PyMongo(app)
# db = mongo_client.db

# users = db['instabook']
# if db is not None:
#     # Proceed with operations on the database
#     users = db['users']
#     # Now you can perform operations on the 'users' collection
# else:
#     print("Failed to connect to the database.")


@app.route("/users", methods=['POST'])
def add_user():
    email = request.form['email']
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    userName = request.form['userName']
    password = request.form['password']
    location = request.form['location']
    country = request.form['country']

    new_obj = {
        "email": email,
        "firstName": firstName,
        "lastName": lastName,
        "userName": userName,
        "password": password,
        "location": location,
        "country": country,

    }
    db.users.insert_one(new_obj)
    flash('user successfully added')
    return "yeppi"


@app.route("/users/all", methods=['GET'])
def get_users():
    # if len(user_list) > 0:
    #     return jsonify(user_list)
    # else:
    #     'Nothing found', 404
    pass
