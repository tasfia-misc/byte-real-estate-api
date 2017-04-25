from flask import Flask, request, jsonify

app = Flask(__name__)

colors = [{'name':'red'},{'name':'green'},{'name':'blue'}]

@app.route('/test', methods = ['GET'])
def test():	
	return jsonify({
	'colors':colors
	})

@app.route('/test', methods = ['POST'])
def add():
	print(request.get_json(force=True)['name'])
	data=request.get_json(force=True)
	print(type(data))
	# print(data['name'])
	# new_color = {'name' : request.get_data['name']}
	# colors.append(new_color)	
	return jsonify({"colors" : colors})


if __name__ == "__main__":
    app.run(debug=True, port = 3000)

 