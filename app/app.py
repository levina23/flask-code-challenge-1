from flask import Flask, request, jsonify, make_response
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import db, Restaurant, Pizzas, Restaurant_pizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


app.route('/',methods=['GET'])
def index():
    data=jsonify({"message": "Pizza Restaurant domain."})
    return data



@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    try:
        # Query the database to get all restaurant records
        restaurants = Restaurant.query.all()
        # Create a list to store restaurant data
        restaurant_list = []
        for restaurant in restaurants:
            restaurant_list.append({
                'id': restaurant.id,
                'name': restaurant.name,
                'address': restaurant.address
            })
        return jsonify(restaurant_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Define a route to get information about a specific restaurant by ID
@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    try:
        # Query the database to get a restaurant record by its ID
        restaurant = Restaurant.query.get(id)
        # Check if the restaurant exists
        if restaurant is None:
            return jsonify({'error': 'Restaurant not found'}), 404
        # Create a list to store pizza data associated with the restaurant
        pizzas = []
        for rp in restaurant.restaurant_pizzas:
            pizzas.append({
                'id': rp.pizza.id,
                'name': rp.pizza.name,
                'ingredients': rp.pizza.ingredients
            })
        return jsonify({
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address,
            'pizzas': pizzas
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Define a route to create a new restaurant
@app.route('/restaurants', methods=['POST'])
def create_restaurant():
    try:
        data = request.get_json()
        name = data.get('name')
        address = data.get('address')
        new_restaurant = Restaurant(name=name, address=address)
        db.session.add(new_restaurant)
        db.session.commit()
        return jsonify({'message': 'Restaurant added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Define a route to delete a restaurant by ID
@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    try:
        restaurant = Restaurant.query.get(id)
        if restaurant is None:
            return jsonify({'error': 'Restaurant not found'}), 404
        for rp in restaurant.restaurant_pizzas:
            db.session.delete(rp)
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Define a route to get a list of all pizzas
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    try:
        pizzas = Pizzas.query.all()
        pizza_list = []
        for pizza in pizzas:
            pizza_list.append({
                'id': pizza.id,
                'name': pizza.name,
                'ingredients': pizza.ingredients
            })
        return jsonify(pizza_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Define a route to create a new pizza
@app.route('/pizzas', methods=['POST'])
def create_pizza():
    try:
        data = request.get_json()
        name = data.get('name')
        ingredients = data.get('ingredients')
        new_pizza = Pizzas(name=name, ingredients=ingredients)
        db.session.add(new_pizza)
        db.session.commit()
        return jsonify({'message': 'Pizza added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Define a route to create a new RestaurantPizza
@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    try:
        data = request.get_json()
        price = data.get('price')
        pizza_id = data.get('pizza_id')
        restaurant_id = data.get('restaurant_id')
        pizza = Pizzas.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)
        if pizza is None or restaurant is None:
            return jsonify({'error': 'Pizza or restaurant not found'}), 404
        new_restaurant_pizza =  Restaurant_pizza(
            price=price,
            pizza=pizza,
            restaurant=restaurant
        )
        db.session.add(new_restaurant_pizza)
        db.session.commit()
        return jsonify({
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
     app.run(debug=True)
