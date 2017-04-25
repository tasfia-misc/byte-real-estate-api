import config
from model import Agents, Listings
import datetime

config.db.drop_all()
config.db.create_all()

first_agent = Agents('john','smith','jsmith@gmail.com','2125559987','NYC Realty')
second_agent = Agents('john', 'appleseed', 'derp@gmail.com', '4035664356', 'Byte Realty')

first_listing = Listings(
    '295 Madison Ave, Fl. 35',
    'New York City',
    'New York',
    '10017',
    '$15,000/month',
    '10,000 sq ft',
    '5',
    '2',
    'Doorman',
    'Description 1',
    'Rental',
    'Sold',
    first_agent.token
)

second_listing = Listings(
    '4514 Woodhaven Ave, Apt. 3A',
    'Astoria',
    'New York',
    '11102',
    '$4,000/month',
    '2,000 sq ft',
    '2',
    '2',
    'No amenities',
    'Description 2',
    'Rental',
    'Available',
    first_agent.token
)

third_listing = Listings(
    '324 Park Ave, Apt. 66B',
    'New York City',
    'New York',
    '10001',
    '$1,200,000',
    '5,000 sq ft',
    '1',
    '1',
    'No amenities',
    'Description 3',
    'Sale',
    'Available',
    second_agent.token
)

config.db.session.add(first_agent)
config.db.session.add(second_agent)

config.db.session.add(first_listing)
config.db.session.add(second_listing)
config.db.session.add(third_listing)

config.db.session.commit()
