##UOM_DAO.PY

# Function to fetch all units of measurement from the 'uom' table
def get_uoms(connection):
    cursor = connection.cursor()            # Create a cursor to execute SQL queries
    query = ("select * from uom")           # SQL query to get all rows from the 'uom' table
    cursor.execute(query)                   # Run the query

    response = []                           # This will store the final list of UOMs

    # Loop through each row returned by the query
    for (uom_id, uom_name) in cursor:
        response.append({
            'uom_id': uom_id,               # ID of the unit (e.g., 1)
            'uom_name': uom_name            # Name of the unit (e.g., "kg", "pcs")
        })

    return response                         # Return the list of UOMs as dictionaries


# This block runs only if the file is executed directly (used for testing/debugging)
if __name__ == '__main__':
    from sql_connection import get_sql_connection  # Import the database connection function

    connection = get_sql_connection()              # Open DB connection

    # Print all UOMs to the console
    print(get_uoms(connection))
