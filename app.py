from flask import render_template, request, jsonify
from config import db, app
from model import *
import json

@app.route('/', methods = ['GET'])
def all_listings():
	all_listings = retreive_all_listings()
	return jsonify(
		listings = all_listings
	)

@app.route('/<token>', methods = ['GET'])
def agent_listings(token):
	agent_listings = filter_all_listings(token)
	return jsonify(
		listings = agent_listings
	)

@app.route('/<token>/state=<state>', methods = ['GET'])
def state_search(token, state):
	state_results = filter_state_listings(token, state)
	return jsonify(
		listings = state_results
	)
########################################
# holding off on price cux its annoying
# @app.route('/token/price')
# def price_search():
# 	price = request.args.get('price')
# 	return price

# @app.route('/sqft')
# def sqft_search():
# 	sqft = request.args.get('sqft')
# 	return sqft
#########################################

@app.route('/<token>/bed=<bedroom_num>', methods = ['GET'])
def bedroom_num_search(token,bedroom_num):
	bedroom_results = filter_bedroom_listings(token, bedroom_num)
	return jsonify(
		listing = bedroom_results
	)

@app.route('/<token>/bath=<bathroom_num>', methods = ['GET'])
def bathroom_num_search(token,bathroom_num):
	bathroom_results = filter_bathroom_listings(token, bathroom_num)
	return jsonify(
		listing = bathroom_results
	)

#this is to filter by whether the listing is for sale or rent
@app.route('/<token>/type=<type_>', methods = ['GET'])
def type_search(token, type_):
	type_results = filter_type_listings(token, type_)
	return jsonify(
		listing = type_results
	)

@app.route('/<token>/avail=<availablity>', methods = ['GET'])
def availablity(token, availablity):
	availablity_results = filter_availability_listings(token, availablity)
	return jsonify(
		listing = availablity_results
	)

@app.route('/<token>', methods = ['POST'])
def add_listing(token):
	new_listing = {
		'street_address': request.json['street_address'],
		'city': request.json['city'],
		'state': request.json['state'],
		'zip_code': request.json['zip_code'],
		'price': request.json['price'],
		'num_of_bedrooms': request.json['num_of_bedrooms'],
		'num_of_bathrooms': request.json['num_of_bathrooms'],
		'amenities': request.json['amenities'],
		'description': request.json['description'],
		'rental_or_sale': request.json['rental_or_sale'],
		'available_or_sold': request.json['available_or_sold'],
		'agent_token': token,
		'square_ft': request.json['square_ft']
	}
	enter_new_listing(token, new_listing)
	return 'listing successfully added. check all listing or filter by [].'

# @app.route('/<token>', methods = ['PUT'])
# def grab_info(token):
# 	updated_listing = {
# 		'street_address': request.json['street_address']
# 	}
#
# 	print(request.json['price'])
#
# 	if request.json['price'] != None:
# 		updated_listing['price']: request.json['price']
# 	if request.json['amenities']:
# 		updated_listing['amenities']: request.json['amenities']
# 	if request.json['description']:
# 		updated_listing['description']: request.json['description']
# 	if request.json['rental_or_sale']:
# 		updated_listing['rental_or_sale']: request.json['rental_or_sale']
# 	if request.json['available_or_sold']:
# 		updated_listing['available_or_sold']: request.json['available_or_sold']
#
# 	# updated_listing = {
# 	# 	'street_address': request.json['street_address'],
# 	# 	'price': request.json['price'],
# 	# 	'amenities': request.json['amenities'],
# 	# 	'description': request.json['description'],
# 	# 	'rental_or_sale': request.json['rental_or_sale'],
# 	# 	'available_or_sold': request.json['available_or_sold']
# 	# }
#
# 	update_listing(token,updated_listing)
# 	return 'listing successfully updated. check all listing or filter by [].'

@app.route('/<token>', methods = ['DELETE'])
def delete_listing(token):
	unvailable_listing = {
		'street_address': request.json['street_address']
	}
	remove_listing(token, unvailable_listing)
	return('listing successfully removed')

if __name__ == "__main__":
    app.run(debug=True)
