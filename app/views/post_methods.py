'''POST Methods.'''

import uuid
import hashlib
import flask
import app
from app import mongo
from datetime import datetime

@app.a.route('/accounts/', methods=['POST'])
def account_operations():
    '''Perform account operations.'''
    operation = flask.request.form["operation"]
    url = flask.request.args.get("target")

    if operation == "login":
        post_login()
    elif operation == "create":
        post_create()
    elif operation == "delete":
        post_delete()

    if url is None or url == "":
        url = flask.url_for("my_index")

    return flask.redirect(url)

def post_login():
    '''Log in a user.'''
    username = flask.request.form["username"]
    password = flask.request.form["password"]

    client = mongo.connection()
    db = client['db']
    users = db['users']
    query = {"email": username}
    user = users.find_one(query)

    password_arr = user["password"].split('$')
    salt = password_arr[1]
    correct_password_hash = password_arr[2]
    salted = salt + password
    entered_password_hash = hashlib.new(password_arr[0])
    entered_password_hash.update(salted.encode('utf-8'))
    password_hashed = entered_password_hash.hexdigest()
    if correct_password_hash == password_hashed:
        flask.session["logname"] = username
    else:
        print("wrong password")
        flask.abort(403)

def post_create():
    '''Create a new user.'''
    email = flask.request.form["email"]
    password = flask.request.form["password"]
    first_name = flask.request.form["firstname"]
    last_name = flask.request.form["lastname"]
    location = flask.request.form["location"]

    algorithm = 'sha512'
    salt = uuid.uuid4().hex
    hash_obj = hashlib.new(algorithm)
    password = str(password)
    salt = str(salt)
    password_salted = salt + password
    hash_obj.update(password_salted.encode('utf-8'))
    password_hash = hash_obj.hexdigest()
    password_db_string = "$".join([algorithm, salt, password_hash])

    today = datetime.today()
    month = today.strftime("%B")
    year = today.year

    client = mongo.connection()
    db = client['db']
    db.users.insert_one({
        "name": {
            "first": first_name,
            "last": last_name
        },
        "email": email,
        "password": password_db_string,
        "location": location,
        "month": month,
        "year": year
    })
    flask.session["logname"] = email
