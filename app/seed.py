from faker import Faker
import random
from app import app

from models import db, Restaurant, Pizzas, Restaurant_pizza

with app.app_context():

    fake = Faker()

    Restaurant.query.delete()
    Pizzas.query.delete()
    Restaurant_pizza.query.delete()
    db.session.commit()

    restaurants = []
    for i in range(20):
        restaurant = Restaurant(name= fake.company(), address = fake.address())
        restaurants.append(restaurant)
        
    db.session.add_all(restaurants)
    db.session.commit()

    pizzas = []
    for i in range(20):
        pizza = Pizzas(name = fake.name(), ingredients = fake.sentence())
        pizzas.append(pizza)
    db.session.add_all(pizzas)
    db.session.commit()

    restaurant_pizzas = []
    for i in range(20):
        
        random_pizza = random.choice(pizzas)
        random_restaurant = random.choice(restaurants)
        
        restaurant_pizza = Restaurant_pizza(
            pizza_id = random_pizza.id,
            restaurant_id = random_restaurant.id,
            price = random.randint(1, 30)
        )
        restaurant_pizzas.append(restaurant_pizza)
    db.session.add_all(restaurant_pizzas)
    db.session.commit()        