import config
from model import Agents, Listings

config.db.drop_all()
config.db.create_all()

first_user = Agents('john','smith','jsmith@gmail.com','2125559987','Nyc Realty', '123456asdfg')

config.db.session.add(first_user)
config.db.session.commit()

first_listing = Listings('295 Madison Ave 35th floor','New York City','New York',  )