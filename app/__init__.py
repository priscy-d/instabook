from flask import render_template
# from flask import request, jsonify, flash
# from app.application import db

from run import app

data = [
    {'title': "Location", 'subtitle': 'Search destinations', "icon": "bi bi-geo-alt-fill",
     'path': "M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10m0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6"},
    {'title': "Check-in", 'subtitle': 'Select date', "icon": "bi bi-calendar-event-fill",
     'path': "M4 .5a.5.5 0 0 0-1 0V1H2a2 2 0 0 0-2 2v1h16V3a2 2 0 0 0-2-2h-1V.5a.5.5 0 0 0-1 0V1H4zM16 14V5H0v9a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2m-3.5-7h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1a.5.5 0 0 1 .5-.5"},
    {'title': "Check-out", 'subtitle': 'Select date', "icon": "bi bi-calendar-event-fill",
     'path': "M4 .5a.5.5 0 0 0-1 0V1H2a2 2 0 0 0-2 2v1h16V3a2 2 0 0 0-2-2h-1V.5a.5.5 0 0 0-1 0V1H4zM16 14V5H0v9a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2m-3.5-7h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1a.5.5 0 0 1 .5-.5"},
    {'title': "Who", 'subtitle': '2 adults . 0 children . 1 room', "icon": "bi bi-person-fill",
     'path': "M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6"}
]

content = [
    {'title': "300+", 'subtitle': 'Happy customers', "icon": "bi bi-people-fill",
     'path': "M7 14s-1 0-1-1 1-4 5-4 5 3 5 4-1 1-1 1zm4-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6m-5.784 6A2.24 2.24 0 0 1 5 13c0-1.355.68-2.75 1.936-3.72A6.3 6.3 0 0 0 5 9c-4 0-5 3-5 4s1 1 1 1zM4.5 8a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5"},
    {'title': "1500+", 'subtitle': 'Properties', "icon": "bi bi-buildings-fill",
     'path': "M15 .5a.5.5 0 0 0-.724-.447l-8 4A.5.5 0 0 0 6 4.5v3.14L.342 9.526A.5.5 0 0 0 0 10v5.5a.5.5 0 0 0 .5.5h9a.5.5 0 0 0 .5-.5V14h1v1.5a.5.5 0 0 0 .5.5h3a.5.5 0 0 0 .5-.5zM2 11h1v1H2zm2 0h1v1H4zm-1 2v1H2v-1zm1 0h1v1H4zm9-10v1h-1V3zM8 5h1v1H8zm1 2v1H8V7zM8 9h1v1H8zm2 0h1v1h-1zm-1 2v1H8v-1zm1 0h1v1h-1zm3-2v1h-1V9zm-1 2h1v1h-1zm-2-4h1v1h-1zm3 0v1h-1V7zm-2-2v1h-1V5zm1 0h1v1h-1z"},
    {'title': "4.5", 'subtitle': 'Ratings', "icon": "bi bi-star-fill",
     'path': "M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"},
    {'title': "5+", 'subtitle': 'City', "icon": "bi bi-geo-alt-fill",
     'path': "M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10m0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6"}
]


@app.route('/')
def main():
    return render_template("landing.html", data=data, content=content)


@app.route('/signup')
def signup():
    return render_template("signup.html", title="Join us")

# @app.route("/users", methods=['POST'])
# def add_user():
#     email = request.form['email']
#     firstName = request.form['firstName']
#     lastName = request.form['lastName']
#     userName = request.form['userName']
#     password = request.form['password']
#     location = request.form['location']
#     country = request.form['country']
#
#     new_obj = {
#         "email": email,
#         "firstName": firstName,
#         "lastName": lastName,
#         "userName": userName,
#         "password": password,
#         "location": location,
#         "country": country,
#
#     }
#
#     db.user.insert_one(new_obj)
#     flash('user successfully added')
#     return "yeppi"



from app.controllers import user
