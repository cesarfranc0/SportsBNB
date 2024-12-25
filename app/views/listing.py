'''Listing Page'''

import flask #type: ignore
import app
from app import mongo

@app.a.route("/listing/<listing_id>/", methods=['GET'])
def listing(listing_id):
    '''Load a listing.'''
    client = mongo.connection()
    db = client['mydatabase'] #EDIT THIS
    listings = db['listings'] #EDIT THIS
    users = db['users'] #EDIT THIS

    query = {"_id": listing_id}
    listing = listings.find_one(query)

    cover = listing['cover_photo']
    title = listing['title']
    desc = listing['description']
    price = listing['price']
    location = listing['location']
    #TODO work on availability

    user_query = {"_id": listing['user_id']}
    user = users.find(user_query)


    content = {

    }
    
    return flask.render_template('listing.html', **content)