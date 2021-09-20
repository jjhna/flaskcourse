from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Decorators - functions that take another function as an argument and returns another function. It allows the extension of an existing function
# @app.route('/') # http://www.google.com/ - we are just getting the homepage or root of the site when we use '/'
# def home():
#     return 'hello wrld' # whatever we do in this function we need to return a response

# JSON is essentially a dictionary, has a key and value pair
# HOWEVER JSON is not a dictionary but a text or long string, so the app needs to return a string and JS needs to turns it into suitable data
# flask uses jsonify which takes in the dictionary and converts it into JSON
# note that this is a list, and we want to return a dictionary of stores
stores = [
    {
        'name': 'my wrld',
        'items': [
            {
                'name': 'my item',
                'price': 69.69
            }
        ]
    }
]

# renders the html webpage called index
@app.route('/')
def home():
    return render_template('index.html')

# web servers work by handiling request such as:
# GET /login HTTP/1.1 - the first part is the Verb: GET, the 2nd is the path after the forward slash /login and the 3rd is the protocol http or https
# Host: https://twitter.com - Just the name of the website before the forward slash '/' or the root of the website

# GET     Retrieve something GET          /item/1
# POST    Receive data and use it         POST/item
# PUT     Make sure something is there    PUT/item
# DELETE  Remove something                DELETE /item/1

# Rest API - a way of thinking about how a web server responds to your requests.
# Rest APIs responds with both data and resources, such as get a resources, remove a resource, etc
# REST are stateless, meaning that one request cannot use another request, so the web server always needs to make a full check

# All of these below are endpoints: an endpoint is the location from which APIs can access the reosurces they need to carry out their function
# The place that APIs send requests and where the resources lives is called an endpoint

# POST /store data: {name}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json() # the request to get the name of the new store in question
    new_store = { # create a new store
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store) # we need to add our new store to the list of stores 
    return jsonify(new_store) # then return the new store as a string using jsonify

# GET /store/<string:name>
@app.route('/store/<string:name>') # http://127.0.0.1:5000/store/some_name we retrieve something from the some_name path url
def get_store(name):
    # Iterate over stores
    # If the store name matches, return it
    # If none match, return an error message
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'error: store name is not found in the list of stores'})

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores}) # we use a key and value pair to get the dictionary from the list of stores
# jsonify which takes in the dictionary and converts it into JSON

# POST /store/<string:name>/item {name, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    for store in stores: # we first need to iterate through the stores to see if the store actually exist if so then we can add the item to the store
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item) # we know which store we want so we just have to append the new items to that store['item'] category
            return jsonify(new_item)
    return jsonify({'error: store not found to add items to'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']}) # return the jsonify or strings of items in the store
    return jsonify({'error: store item is not found'})

app.run(port=5000)