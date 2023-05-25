FlaskMarket
FlaskMarket is a web application developed using Flask, a Python web framework. It provides a simple marketplace where users can buy and sell items.

Project Structure
The project structure is organized as follows:

lua
Copy code
FlaskMarket/
|-- instance/
|   |-- market.db
|-- market/
|   |-- templates/
|   |   |-- includes/
|   |   |   |-- items_modals.html
|   |   |   |-- owned_items_modals.html
|   |   |-- base.html
|   |   |-- home.html
|   |   |-- login.html
|   |   |-- market.html
|   |   |-- register.html
|   |-- __init__.py
|   |-- forms.py
|   |-- models.py
|   |-- routes.py
|-- run.py
The instance/ directory contains the SQLite database file market.db, which stores the application's data.

The market/ directory contains the main application code and resources.

The templates/ directory holds the HTML templates used for rendering the application's views. It includes additional directories for reusable templates (includes/).

The __init__.py file initializes the Flask application and sets up the required extensions and configurations.

The forms.py file defines the Flask-WTF forms used for user registration, login, and item operations.

The models.py file contains the database models defined using SQLAlchemy, including the User and Item models.

The routes.py file defines the application routes and handles the logic for rendering views and processing user requests.

The run.py file is the entry point of the application, responsible for running the Flask development server.