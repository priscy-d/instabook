
from flask import render_template

from flask import Flask


app = Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return render_template("layout.html", title="instaboook")

