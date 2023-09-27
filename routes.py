from flask import Blueprint, jsonify
from models import Pizza

# Create a Blueprint for your routes
bp = Blueprint('routes', __name__)

# Define your routes using the Blueprint
@bp.route('/pizza', methods=['GET'])  # Use lowercase route names
def get_pizza():
    pizzas = Pizza.query.all()  # Replace with logic to fetch pizza data from your database
    pizza_data = [{"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients} for pizza in pizzas]
    return jsonify(pizza_data)

@bp.route('/pizzas', methods=['GET'])  # Use lowercase route names
def get_pizzas():
    pizzas = Pizza.query.all()  # Replace with logic to fetch pizzas data from your database
    pizza_data = [{"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients} for pizza in pizzas]
    return jsonify(pizza_data)

# Rest of your route definitions...

# Import this Blueprint in your app.py and register it to use the routes
# Example in app.py:
# from flask import Flask
# from routes import bp as routes_blueprint
# app = Flask(__name__)
# app.register_blueprint(routes_blueprint)

# Rest of your app.py code...
