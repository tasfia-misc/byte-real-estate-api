from config import db

class Agents(db.Model):
    __tablename__ = 'agents'
    _id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    phone_number = db.Column(db.String(11))
    company = db.Column(db.String)
    api_token = db.Column(db.String)
    listings = db.relationship('Listings', backref='agents',
                                lazy='dynamic')


    def __init__(self, first, last, eMail, phone, com, token):
        self.first_name = first
        self.last_name = last
        self.email = eMail
        self.phone_number = phone
        self.company = com
        self.api_token = token

class Listings(db.Model):
    __tablename__ = 'listings'
    _id = db.Column(db.Integer, primary_key=True)
    street_address = db.Column(db.String )
    city = db.Column(db.String)
    state = db.Column(db.String)
    price = db.Column(db.Integer)
    square_ft = db.Column(db.Integer)
    num_of_bedrooms = db.Column(db.Integer)
    num_of_bathrooms = db.Column(db.Integer)
    amenities = db.Column(db.String)
    description = db.Column(db.String)
    date_listed = db.Column(db.TIMESTAMP)
    rental_or_sale = db.Column(db.String)
    available_or_sold = db.Column(db.String)
    agent_token = db.Column(db.Integer, db.ForeignKey('agents.api_token'))

    def __init__(self, street, c, s, p, sq_ft, beds, baths, amn, des, date, rOs, aOs,agent_token):
        self.street_address = street
        self.city = c
        self.state = s
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

