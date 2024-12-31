'''Listing Page'''

import flask #type: ignore
import app
from app import mongo
from bson import ObjectId

@app.a.route("/listing/<listing_id>/", methods=['GET']) 
def listing(listing_id):

    '''Load a listing.'''
    client = mongo.connection()
    db = client['db'] 
    listings = db['listings']
    users = db['users'] 

    query = {"_id": ObjectId(listing_id)}
    listing = listings.find_one(query)
    print(listing)
    cover = listing['cover_photo']
    title = listing['title']
    desc = listing['description']
    price = listing['price']
    location = listing['location']
    city = location['City']
    state = location['State']
    address = location['Address']
    all_avail = listing['availability']
    availability = []
    for x in all_avail:
        date = x['date']
        for time in x['time_slots']:
            start = time['start']
            end = time['end']
            availability.append({'date': date, 'start': start, 'end': end})
    
    user_query = {"_id": listing['user_id']}
    user = users.find_one(user_query)
    first_name = user['name']['first']
    last_name = user['name']['last']
    name = first_name + " " + last_name

    content = {
        'cover': cover,
        'title': title,
        'desc': desc,
        'price': price,
        'address': address,
        'city': city,
        'state': state,
        'availability': availability,
        'name': name
    }
    
    return flask.render_template('listing.html', **content)