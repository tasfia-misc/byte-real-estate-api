from config import db
from uuid import uuid4
import json
import datetime

class Agents(db.Model):
    __tablename__ = 'agents'
    _id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    phone_number = db.Column(db.String(15))
    company = db.Column(db.String)
    token = db.Column(db.String)
    listings = db.relationship('Listings', backref='agents', lazy='dynamic')


    def __init__(self, first, last, eMail, phone, com):
        self.first_name = first
        self.last_name = last
        self.email = eMail
        self.phone_number = phone
        self.company = com
        self.token = uuid4().hex

class Listings(db.Model):
    __tablename__ = 'listings'
    _id = db.Column(db.Integer, primary_key=True)
    street_address = db.Column(db.String )
    city = db.Column(db.String)
    state = db.Column(db.String)
    zip_code = db.Column(db.String)
    price = db.Column(db.Integer)
    square_ft = db.Column(db.Integer)
    num_of_bedrooms = db.Column(db.Integer)
    num_of_bathrooms = db.Column(db.Integer)
    amenities = db.Column(db.String)
    description = db.Column(db.String)
    date_listed = db.Column(db.TIMESTAMP)
    last_update = db.Column(db.TIMESTAMP)
    rental_or_sale = db.Column(db.String)
    available_or_sold = db.Column(db.String)
    agent_token = db.Column(db.Integer, db.ForeignKey('agents.token'))

    def __init__(self, street, c, s, zip_, p, sq_ft, beds, baths, amn, des, date_created, date_modified, rOs, aOs, agent_token):
        self.street_address = street
        self.city = c
        self.state = s
        self.zip_code = zip_
        self.price = p
        self.square_ft = sq_ft
        self.num_of_bedrooms = beds
        self.num_of_bathrooms = baths
        self.amenities = amn
        self.description = des
        self.date_listed = date_created
        self.date_modified = date_modified
        self.rental_or_sale = rOs
        self.available_or_sold = aOs
        self.agent_token = agent_token

def filter_all_listings(token):
    all_listings = []
    results = Listings.query.filter_by(agent_token=token).all()

    for result in results:
        listing = {
            "Address": "{}, {}, {}, {}".format(result.street_address, result.city, result.state, result.zip_code),
            "Bedrooms": result.num_of_bedrooms,
            "Bath": result.num_of_bathrooms,
            "Availablity": result.available_or_sold,
            "Price": result.price,
            "Type": result.rental_or_sale,
            "Last_Modified" :result.last_update
        }
        all_listings.append(listing)

    return all_listings

def filter_city_listings(token,city):
    all_listings = []
    results = Listings.query.filter_by(city = city, agent_token = token)
    for result in results:
        listing = {
            "Address": "{}, {}, {}, {}".format(result.street_address, result.city, result.state, result.zip_code),
            "Bedrooms": result.num_of_bedrooms,
            "Bath": result.num_of_bathrooms,
            "Availablity": result.available_or_sold,
            "Price": result.price,
            "Type": result.rental_or_sale
        }
        all_listings.append(listing)

    return all_listings

def filter_state_listings(token,state):
    all_listings = []
    results = Listings.query.filter_by(state = state, agent_token = token)
    for result in results:
        listing = {
            "Address": "{}, {}, {}, {}".format(result.street_address, result.city, result.state, result.zip_code),
            "Bedrooms": result.num_of_bedrooms,
            "Bath": result.num_of_bathrooms,
            "Availablity": result.available_or_sold,
            "Price": result.price,
            "Type": result.rental_or_sale
        }
        all_listings.append(listing)

    return all_listings

def filter_bedroom_listings(token, bedroom_num):
    all_listings = []
    results = Listings.query.filter_by(num_of_bedrooms = bedroom_num, agent_token = token)
    for result in results:
        listing = {
            "Address": "{}, {}, {}, {}".format(result.street_address, result.city, result.state, result.zip_code),
            "Bedrooms": result.num_of_bedrooms,
            "Bath": result.num_of_bathrooms,
            "Availablity": result.available_or_sold,
            "Price": result.price,
            "Type": result.rental_or_sale
        }
        all_listings.append(listing)

    return all_listings

def filter_bathroom_listings(token, bathroom_num):
    all_listings = []
    results = Listings.query.filter_by(num_of_bathrooms = bathroom_num, agent_token = token)
    for result in results:
        listing = {
            "Address": "{}, {}, {}, {}".format(result.street_address, result.city, result.state, result.zip_code),
            "Bedrooms": result.num_of_bedrooms,
            "Bath": result.num_of_bathrooms,
            "Availablity": result.available_or_sold,
            "Price": result.price,
            "Type": result.rental_or_sale
        }
        all_listings.append(listing)

    return all_listings

def filter_type_listings(token, type_):
    all_listings = []
    results = Listings.query.filter_by(rental_or_sale = type_, agent_token = token)
    for result in results:
        listing = {
            "Address": "{}, {}, {}, {}".format(result.street_address, result.city, result.state, result.zip_code),
            "Bedrooms": result.num_of_bedrooms,
            "Bath": result.num_of_bathrooms,
            "Availablity": result.available_or_sold,
            "Price": result.price,
            "Type": result.rental_or_sale
        }
        all_listings.append(listing)

    return all_listings

def filter_availability_listings(token, availablity):
    all_listings = []
    results = Listings.query.filter_by(available_or_sold = availablity, agent_token = token)
    for result in results:
        listing = {
            "Address": "{}, {}, {}, {}".format(result.street_address, result.city, result.state, result.zip_code),
            "Bedrooms": result.num_of_bedrooms,
            "Bath": result.num_of_bathrooms,
            "Availablity": result.available_or_sold,
            "Price": result.price,
            "Type": result.rental_or_sale
        }
        all_listings.append(listing)

    return all_listings



def enter_new_listing(token, new_listing):
    print(new_listing)
    new_address = new_listing['street_address']
    new_city = new_listing['city']
    new_state = new_listing['state']
    new_zip = new_listing['zip']
    new_price = new_listing['price']
    new_sq_ft = new_listing['square_feet']
    new_bedroom_num = new_listing['num_of_bedrooms']
    new_bath_num = new_listing['num_of_bathrooms']
    new_amenities = new_listing['amenities']
    new_descript = new_listing['description']
    new_date_listed = datetime.datetime.now()
    new_last_modified = datetime.datetime.now()
    new_rent_sale = new_listing['rental_or_sale']
    new_avail = new_listing['available_or_sold']
   
    database_add = Listings(new_address,new_city,new_state,new_zip,new_price,new_sq_ft,new_bedroom_num,new_bath_num,new_amenities,new_descript,new_date_listed,datetime.datetime.now(),new_rent_sale,new_avail,token)
    db.session.add(database_add)
    db.session.commit()

def update_listing(token,updated_listing):
    address = updated_listing['street_address']
    updated_price = updated_listing['price']
    updated_amenities = updated_listing['amenities']
    updated_descript = updated_listing['description']
    # updated_last_modified = datetime.datetime.now()
    updated_rent_sale = updated_listing['rental_or_sale']
    updated_avail = updated_listing['available_or_sold']
 
    Listings.query.filter_by(street_address = address).update({
        'price': updated_price,
        'amenities':updated_amenities,
        'description':updated_descript,
        'rental_or_sale':updated_rent_sale,
        'available_or_sold':updated_avail
        })
    db.session.commit()

def remove_listing(token,unavailable_listing):
    address = unavailable_listing['street_address']

    Listings.query.filter_by(street_address = address).update({
        'price': "NONE",
        'amenities':"NONE",
        'description':"NONE",
        'rental_or_sale':"NONE",
        'available_or_sold':"NONE"
        })
    db.session.commit()    