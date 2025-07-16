Grocery Store App Manager
A simple web application backend and frontend for managing grocery store products and customer orders.

Overview
This project provides a system to manage grocery store operations including:

Adding, deleting, and listing products with unit pricing

Capturing customer orders with detailed order items

Retrieving order histories and details

Web interface for managing products and orders

Tech Stack
Backend: Python (Flask or similar framework assumed)

Database: SQL (MySQL or compatible, connection via sql_connection.py)

Frontend: HTML, CSS, JavaScript

File formats: Product images and other assets in /images folder

Features
Insert new orders with multiple products and quantities

View all orders with detailed line items

Insert, list, and delete products with unit of measure and price

Responsive web pages to interact with backend APIs

Simple SQL-based data persistence

File Structure
bash
Copy
Edit
/css/                # CSS stylesheets
/js/                 # JavaScript files
/images/             # Images used in the website (product photos, UI images)
/orders_dao.py       # Backend code handling orders database operations
/products_dao.py     # Backend code handling products database operations
/sql_connection.py   # Database connection helper
/manage-product.html # Product management web page
/order.html          # Order viewing and creation web page
/index.html          # Homepage / main entry point
/server.py           # Backend server (Flask or other framework) to connect frontend and backend
/uom_dao.py          # Unit of Measure data access object
Setup Instructions
Install dependencies

Python 3.x

Required Python packages (e.g., Flask, MySQL connector) — install via:

bash
Copy
Edit
pip install -r requirements.txt
(Create this file if not present with the packages you need)

Database setup

Create your SQL database with tables for orders, order_details, products, and uom as expected by the DAOs.

Update sql_connection.py with your database credentials.

Run the server
Start the backend server (example using Flask):

bash
Copy
Edit
python server.py
Access the frontend
Open index.html or the relevant HTML pages in a browser to interact with the app.

Usage
Use /manage-product.html to add or remove products.

Use /order.html to place new customer orders or view existing orders.

Backend handles storing and retrieving all data with SQL queries.

Notes
The backend functions use parameterized queries for security (except a noted place in delete_product which can be improved).

The app currently supports image files in the /images folder (ensure supported formats like .jpg, .png).

The frontend pages rely on JavaScript to interact with the backend API endpoints.

Future Improvements
Add user authentication and roles

Improve UI with better design and responsiveness

Add image upload and management for products

Support order updates and cancellations

Implement more robust error handling and input validation
