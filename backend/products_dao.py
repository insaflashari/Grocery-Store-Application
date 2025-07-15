## PRODUCTS_DAO.PY
# Handles all product-related database operations

from sql_connection import get_sql_connection   # Import DB connection function

# ---------------- GET ALL PRODUCTS ----------------
def get_all_products(connection):
    cursor = connection.cursor()   # Create a cursor for executing SQL
    # SQL query to fetch all product details with unit name (JOIN with uom table)
    query = (
        "SELECT products.product_id, products.name, products.uom_id, "
        "products.price_per_unit, uom.uom_name "
        "FROM products "
        "INNER JOIN uom ON products.uom_id = uom.uom_id"
    )
    cursor.execute(query)          # Execute the query

    response = []                  # List to store results

    # Loop through results and build a dictionary for each row
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })

    return response                # Return the product list


# ---------------- INSERT A NEW PRODUCT ----------------
def insert_new_product(connection, product):
    cursor = connection.cursor()
    # SQL query to insert a new product into the table
    query = (
        "INSERT INTO products "
        "(name, uom_id, price_per_unit) "
        "VALUES (%s, %s, %s)"
    )
    # Extract data from the product dictionary
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])

    cursor.execute(query, data)    # Execute the insert
    connection.commit()            # Save changes to the DB

    return cursor.lastrowid        # Return the ID of the newly added product


# ---------------- DELETE A PRODUCT BY ID ----------------
def delete_product(connection, product_id):
    cursor = connection.cursor()
    # WARNING: Direct string formatting can cause SQL injection — use parameterized queries instead
    query = ("DELETE FROM products WHERE product_id = " + str(product_id))
    cursor.execute(query)          # Delete the product by ID
    connection.commit()

    return cursor.lastrowid        # Return the deleted product's ID


# ---------------- TESTING BLOCK ----------------
# This runs only when the file is executed directly (not imported)
if __name__ == '__main__':
    connection = get_sql_connection()  # Get a DB connection

    # Example: Insert a new product named "potatoes"
    print(insert_new_product(connection, {
        'product_name': 'potatoes',
        'uom_id': '1',              # ID of the unit (e.g., 1 = "kg")
        'price_per_unit': 10        # Price per unit
    }))
