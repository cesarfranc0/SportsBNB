'''Index Page'''

import flask #type: ignore
import app
from app import mongo

@app.a.route("/", methods=['GET'])
def index():
    '''Load the index page.'''
    state = flask.request.args.get('state')

    if not state:
        state = 'New York'

    client = mongo.connection()
    db = client['db']
    listings = db['listings']
    results = listings.find({'location.State': state})
    listing = []
    for x in results:
        temp = {
            'id': str(x['_id']),
            'title': x['title'],
            'cover': x['cover_photo'],
            'price': x['price'],
            'description': x['description'],
            'address': x['location']['Address'],
            'city': x['location']['City'],
            'state': x['location']['State'],
        }
        listing.append(temp)

    context = {
        'listings': listing
    }
    return flask.render_template('index.html', **context)