'''User Profile Page.'''

import flask #type: ignore
import app
import mongo

@app.a.route("/user/",  methods=["GET"])
def my_user():
    '''Load a user's profile.'''
    if 'logname' not in flask.session:
        return flask.redirect(flask.url_for('login'))
    logname = flask.session["logname"]

    client = mongo.connection()
    db = client['mydatabase'] #EDIT THIS
    users = db['users'] #EDIT THIS

    #User Information
    query = {"email": logname}
    user = users.find(query)
    for u in user:
        first_name = u['name']['first']
        last_name = u['name']['last']
        month_joined = u['month']
        year_joined = u['year']
        location = u.get('location')
        pfp = u.get('pfp')
        uid = users['_id']

    #Owned Listings
    listings = db['listings']
    listing_query = {"user_id": uid}
    created_listings = listings.find(listing_query)
    created = []
    for x in created_listings:
        created.append({'title': x['title'], 'cover': x['cover_photo']})

    #Reserved Listings
    bookings = db['bookings']
    bookings_query = {"user_id": uid}
    reservations = bookings.find(bookings_query)
    reserve = []
    for x in reservations:
        lid = x['listing_id']
        query = {"_id": lid}
        listing = listings.find(query)
        for x in listing:
            title = x['title']
            cover = x['cover_photo']
        date = x['booking_date']
        start = x['time']['start']
        end = x['time']['end']
        price = x['price']
        reserve.append({'title': title, 'cover': cover, 'date': date,
                        'start_time': start, 'end_time': end, 'price': price})
        
    content = {
        'logname': logname,
        'first_name': first_name,
        'last_name': last_name,
        'month': month_joined,
        'year': year_joined,
        'location': location,
        'pfp': pfp,
        'created_listings': created,
        'reserved_listings': reserve
    }

    return flask.render_template('user.html', **content)

