'''Login/Create Accounts'''

import app
import flask #type: ignore

@app.a.route('/accounts/login/', methods=['GET'])
def login():
    if 'logname' in flask.session:
        return flask.redirect(flask.url_for("index"))
    return flask.render_template("login.html")

@app.a.route('/accounts/create/', method=['GET'])
def create():
    if 'logname' in flask.session:
        return flask.redirect(flask.url_for("index"))
    return flask.render_template("create.html")