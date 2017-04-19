# from flask import Flask,  render_template, request
# from flask_sqlalchemy import SQLAlchemy


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////realty_api.db'

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

from config import db, app
from model import *

token = ""

@app.route('/')
def agent_listings(token):
	token = request.args.get('token')
	return token

@app.route('/city')
def city_search():
	city = request.args.get('city')
	return city

@app.route('/state')
def state_search():
	state = request.args.get('state')
	return state

@app.route('/price')
def price_search():
	price = request.args.get('price')
	return price

@app.route('/sqft')
def sqft_search():
	sqft = request.args.get('sqft')
	return sqft	

@app.route('/bedroom_num')
def bedroom_num_search():
	bedroom = request.args.get('bedroom_num')
	return bedroom_num	

@app.route('/bathroom_num')
def bathroom_num_search():
	bathroom = request.args.get('bathroom_num')
	return bathroom_num	

@app.route('/amenities')
def amenities_num_search():
	amenities_search = request.args.get('amenities')
	return amenities_search	

#this is to filter by whether the listing is for sale or rent
@app.route('/type') 
def type_search():
	type = request.args.get('type')
	return type 

@app.route('/availablity')
def availablity():
	availablity = request.args.get('availablity')
	return availablity	


if __name__ == "__main__":
    app.run(debug=True)