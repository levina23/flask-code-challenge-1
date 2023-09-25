import os
from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'  # SQLite database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define your models (Restaurant, Pizza, and RestaurantPizza) here
class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(255))
    pizzas = db.relationship('Pizza', secondary='restaurant_pizza', back_populates='restaurants')

    def __init__(self, name, address):
        self.name = name
        self.address = address

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    ingredients = db.Column(db.String(255))
    restaurants = db.relationship('Restaurant', secondary='restaurant_pizza', back_populates='pizzas')

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')
    pizza = db.relationship('Pizza', back_populates='pizza_restaurants')

# Add the restaurant_pizza table for the many-to-many relationship
db.Table(
    'restaurant_pizza',
    db.metadata,
    db.Column('restaurant_id', db.Integer, db.ForeignKey('restaurant.id'), primary_key=True),
    db.Column('pizza_id', db.Integer, db.ForeignKey('pizza.id'), primary_key=True),
    extend_existing=True
)

# Define the root route ("/")
@app.route('/')
def home():
    return "Welcome to the Pizza API!"

# Define the favicon.ico route
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Define your routes here
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurant_list = [{"id": r.id, "name": r.name, "address": r.address} for r in restaurants]
    return jsonify(restaurant_list)

# Rest of your route definitions...

if __name__ == '__main__':
    app.run(debug=True)
