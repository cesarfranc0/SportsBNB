"""sportsBNB package intializer."""
import flask #type: ignore

a = flask.Flask(__name__)

a.config.from_object('app.config')

import app.views
import app.api

