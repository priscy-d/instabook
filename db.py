from mongoengine import connect

connect(
    db='instabook_db',
    username='your_username',
    password='your_password',
    host='your_host',
    port=27017
)
