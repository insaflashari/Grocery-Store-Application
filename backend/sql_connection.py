#SQL_CONNECTION.PY

import datetime                    # Imported but not used here — can be removed if unnecessary
import mysql.connector             # MySQL library to connect Python to a MySQL database

# Initialize a private module-level variable to store the database connection
__cnx = None

# Function to establish (or reuse) a connection to the MySQL database
def get_sql_connection():
    print("Opening mysql connection")  # Log to show when the connection is first made
    global __cnx                      # Declare we're using the global __cnx variable

    # Only create a new connection if one doesn't already exist
    if __cnx is None:
        __cnx = mysql.connector.connect(
            user='root',              # Your MySQL username (change as needed)
            password='root',          # Your MySQL password (change as needed)
            database='grocery_store'  # Name of your database
        )

    return __cnx                      # Return the existing or new connection
