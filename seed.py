import config
from model import Agents, Listings
import datetime

config.db.drop_all()
config.db.create_all()

current_time = datetime.datetime.now()

first_user = Agents('john','smith','jsmith@gmail.com','2125559987','Nyc Realty')

first_listing = Listings('295 Madison Ave 35th floor','New York City','New York', '10017', '$15,000/month', '10,000 sq ft', '5','2','Door Man', 'None', current_time, 'Rental','Sold', first_user.token)
second_listing =  Listings('493 Madison Ave 39th floor','New York City','New York', '10017', '$309,000/month', '5,000 sq ft','1','2','Door Man, Swimming Pool', 'None', current_time, 'Rental', 'Available', first_user.token)

config.db.session.add(first_user)
config.db.session.add(first_listing)
config.db.session.add(second_listing)
config.db.session.commit()
