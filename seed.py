import config
from model import Agents, Listings
import datetime

config.db.drop_all()
config.db.create_all()

current_time = datetime.datetime.now()

first_user = Agents('john','smith','jsmith@gmail.com','2125559987','Nyc Realty',)

first_listing = Listings('295 Madison Ave 35th floor','New York City','New York', '$15,000/month', '10,000 sq ft',  '5','2','Door Man', 'None', current_time, 'Rental','Sold')

config.db.session.add(first_listing)
config.db.session.add(first_user)
config.db.session.commit()
