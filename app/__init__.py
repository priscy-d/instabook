from flask import render_template

from flask import Flask

app = Flask(__name__, template_folder='templates')

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



@app.route('/')
def main():
    return render_template("landing.html", data=data)


@app.route('/signup')
def signup():
    return render_template("signup.html", title="Join us")
