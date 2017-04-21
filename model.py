from config import db
from uuid import uuid4
import json

class Agents(db.Model):
    __tablename__ = 'agents'
    _id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    phone_number = db.Column(db.String(11))
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
    rental_or_sale = db.Column(db.String)
    available_or_sold = db.Column(db.String)
    agent_token = db.Column(db.Integer, db.ForeignKey('agents.token'))

    def __init__(self, street, c, s, zip_, p, sq_ft, beds, baths, amn, des, date, rOs, aOs, agent_token):
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
        self.date_listed = date
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
            "Type": result.rental_or_sale
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
    print('================')
    print(new_listing)
    print('+++++++++++++++++++')
    print(token)
    pass
    
# def enter_new_listing(token, new_listing):
#     print(new_listing)


    # listing_to_add = b.decode(new_listing)
    # listing_to_add = json.load(listing_to_add)
    # print(listing_to_add)