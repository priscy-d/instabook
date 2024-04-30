from run import app
from flask_pymongo import PyMongo

app.config['SECRET_KEY'] = '689727683effe5980db7ec9af471311b2ebf9c7f'
app.config[
    'MONGO_URI'] = "mongodb+srv://priscilladunyoh99:Q7OXtTY2z66B1vj3@cluster0.gsxghkt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

mongo_client = PyMongo(app)
db = mongo_client.db

from pymongo.mongo_client import MongoClient
#
# uri = "mongodb+srv://priscilladunyoh99:Q7OXtTY2z66B1vj3@cluster0.gsxghkt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
#
# # Create a new client and connect to the server
# client = MongoClient(uri)
#
# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
