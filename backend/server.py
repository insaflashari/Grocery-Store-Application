## SERVER
# Starts a Flask server on port 5000
# Exposes API endpoints like /getProducts, /insertProduct, /getAllOrders, etc.
# Accepts HTTP GET and POST requests
# Returns JSON responses
# Uses Access-Control-Allow-Origin: * so frontend (even from another port) can call it

from flask import Flask, request, jsonify         # Flask framework for creating the API
from sql_connection import get_sql_connection     # Import database connection helper
import mysql.connector                            # MySQL connector for Python (used internally)
import json                                       # Used to parse incoming JSON-formatted request data

# Importing Data Access Object modules for clean code separation
import products_dao
import orders_dao
import uom_dao

# Create a new Flask app instance
app = Flask(__name__)

# Establish a single database connection for reuse across all routes
connection = get_sql_connection()

# -------------------------- API ROUTES --------------------------

# Route to get all units of measurement (e.g., kg, pcs, L)
@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)      # Fetch UOMs using DAO
    response = jsonify(response)                 # Convert Python dict/list to JSON
    response.headers.add('Access-Control-Allow-Origin', '*')  # Enable CORS
    return response

# Route to get all products in the store
@app.route('/getProducts', methods=['GET'])
def get_products():
    response = products_dao.get_all_products(connection)       # Fetch product list
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Route to insert a new product (POST request)
@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])         # Parse incoming product data
    product_id = products_dao.insert_new_product(connection, request_payload)  # Insert product into DB
    response = jsonify({
        'product_id': product_id                               # Return the new product ID
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Route to fetch all orders and their itemized details
@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders_dao.get_all_orders(connection)          # Get all orders from DB
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Route to insert a new customer order
@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])        # Parse incoming order data
    order_id = orders_dao.insert_order(connection, request_payload)  # Save order to DB
    response = jsonify({
        'order_id': order_id                                  # Return the new order ID
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Route to delete a product by ID
@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])  # Delete product
    response = jsonify({
        'product_id': return_id                               # Return the deleted product ID
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# -------------------------- SERVER START --------------------------

# This block only runs if this file is executed directly (not imported)
if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)   # Start Flask server on http://localhost:5000
