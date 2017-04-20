from flask import render_template, request, jsonify
from config import db, app
from model import *

@app.route('/<token>')
def agent_listings(token):
	agent_listings = filter_all_listings(token)
	return jsonify(
		listings = agent_listings
	)

@app.route('/<token>/city=<city>')
def city_search(token, city):
	city_results = filter_city_listings(token, city)
	return jsonify(
		listings = city_results
	)

@app.route('/<token>/state=<state>')
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

@app.route('/<token>/bed=<bedroom_num>')
def bedroom_num_search(token,bedroom_num):
	bedroom_results = filter_bedroom_listings(token, bedroom_num)
	return jsonify(
		listing = bedroom_results
	)

@app.route('/<token>/bath=<bathroom_num>')
def bathroom_num_search(token,bathroom_num):
	bathroom_results = filter_bathroom_listings(token, bathroom_num)
	return jsonify(
		listing = bathroom_results
	)

########################################
# don't think a search for this is necessary
# @app.route('/amenities')
# def amenities_num_search():
# 	amenities_search = request.args.get('amenities')
# 	return amenities_search
#########################################

#this is to filter by whether the listing is for sale or rent
@app.route('/<token>/type=<type_>')
def type_search(token, type_):
	type_results = filter_type_listings(token, type_)
	return jsonify(
		listing = type_results
	)

@app.route('/<token>/avail=<availablity>')
def availablity(token, availablity):
	availablity_results = filter_availability_listings(token, availablity)
	return jsonify(
		listing = availablity_results
	)

@app.route('/<token>/add-listing')
def add_listing():
	pass

if __name__ == "__main__":
    app.run(debug=True)
