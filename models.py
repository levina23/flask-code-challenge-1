from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define your models (Restaurant, Pizza, and RestaurantPizza) here
class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(255))
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant')
    pizzas = db.relationship('Pizza', secondary='restaurant_pizza', back_populates='restaurants')

    def __init__(self, name, address):
        self.name = name
        self.address = address

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    ingredients = db.Column(db.String(255))
    pizza_restaurants = db.relationship('RestaurantPizza', back_populates='pizza')
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
