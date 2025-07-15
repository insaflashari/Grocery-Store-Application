## ORDERS_DAO.PY
# Handles customer orders

from datetime import datetime             # To capture the current timestamp for orders
from sql_connection import get_sql_connection  # Import DB connection helper

# -------- INSERT A NEW ORDER ------------
def insert_order(connection, order):
    cursor = connection.cursor()          # Create cursor for executing queries

    # Insert the order-level info into the 'orders' table
    order_query = (
        "INSERT INTO orders "
        "(customer_name, total, datetime) "
        "VALUES (%s, %s, %s)"
    )
    # Data tuple includes customer name, grand total, and current datetime
    order_data = (order['customer_name'], order['grand_total'], datetime.now())

    cursor.execute(order_query, order_data)  # Execute the insert
    order_id = cursor.lastrowid               # Get the new order's ID (primary key)

    # Insert each product line item into 'order_details' table
    order_details_query = (
        "INSERT INTO order_details "
        "(order_id, product_id, quantity, total_price) "
        "VALUES (%s, %s, %s, %s)"
    )

    order_details_data = []

    # Loop through all items in the order to prepare bulk insert data
    for order_detail_record in order['order_details']:
        order_details_data.append([
            order_id,                                 # Foreign key to link order details
            int(order_detail_record['product_id']),  # Product ID (cast to int)
            float(order_detail_record['quantity']),  # Quantity ordered
            float(order_detail_record['total_price']) # Total price for that item
        ])

    cursor.executemany(order_details_query, order_details_data)  # Insert all order items at once

    connection.commit()  # Commit changes to DB

    return order_id      # Return the newly created order ID


# -------- GET DETAILS OF A SINGLE ORDER ------------
def get_order_details(connection, order_id):
    cursor = connection.cursor()

    # SQL query joining order_details and products to get product info for an order
    query = (
        "SELECT order_details.order_id, order_details.quantity, order_details.total_price, "
        "products.name, products.price_per_unit "
        "FROM order_details "
        "LEFT JOIN products ON order_details.product_id = products.product_id "
        "WHERE order_details.order_id = %s"
    )

    data = (order_id, )   # Tuple with order_id to safely pass to the query

    cursor.execute(query, data)

    records = []

    # Build list of dictionaries with order item info
    for (order_id, quantity, total_price, product_name, price_per_unit) in cursor:
        records.append({
            'order_id': order_id,
            'quantity': quantity,
            'total_price': total_price,
            'product_name': product_name,
            'price_per_unit': price_per_unit
        })

    cursor.close()  # Close cursor to free resources

    return records


# -------- GET ALL ORDERS WITH DETAILS ------------
def get_all_orders(connection):
    cursor = connection.cursor()

    # Select all orders from 'orders' table
    query = ("SELECT * FROM orders")
    cursor.execute(query)

    response = []

    # Convert each row into a dictionary
    for (order_id, customer_name, total, dt) in cursor:
        response.append({
            'order_id': order_id,
            'customer_name': customer_name,
            'total': total,
            'datetime': dt,
        })

    cursor.close()

    # For each order, fetch and append detailed items info
    for record in response:
        record['order_details'] = get_order_details(connection, record['order_id'])

    return response


# -------- TESTING BLOCK ------------
if __name__ == '__main__':
    connection = get_sql_connection()

    # Print all orders with details (test)
    print(get_all_orders(connection))

    # Example for fetching details of order with ID 4 (uncomment to test)
    # print(get_order_details(connection, 4))

    # Example for inserting a new order (uncomment to test)
    # print(insert_order(connection, {
    #     'customer_name': 'dhaval',
    #     'total': '500',
    #     'datetime': datetime.now(),
    #     'order_details': [
    #         {
    #             'product_id': 1,
    #             'quantity': 2,
    #             'total_price': 50
    #         },
    #         {
    #             'product_id': 3,
    #             'quantity': 1,
    #             'total_price': 30
    #         }
    #     ]
    # }))
