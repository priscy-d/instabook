from app.controllers import app
from flask import request, jsonify
from db import user_list

@app.route("/users", methods=[ 'POST'])
def add_user():
    new_author = request.form['author']
    new_lang = request.form['language']
    new_title = request.form['title']
    id = len(user_list) + 1

    new_obj = {
        'id': id,
        'author': new_author,
        'language': new_lang,
        'title': new_title
    }

    user_list.append(new_obj)
    return jsonify(user_list), 201

@app.route("/users/all", methods=[ 'GET'])
def get_users():
    if len(user_list) > 0:
        return jsonify(user_list)
    else:
        'Nothing found', 404