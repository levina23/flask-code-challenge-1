# Flask Pizza API

The Flask Pizza API is a versatile web application designed to help you manage pizza restaurants and their menus with ease. Whether you're building a small local pizzeria's website or a comprehensive pizza delivery platform, this API has you covered. It provides full CRUD (Create, Read, Update, Delete) functionality for restaurants and pizzas and allows you to associate pizzas with specific restaurants.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you start using the Flask Pizza API, make sure you have the following prerequisites installed on your system:

- Python 3.6+ installed on your machine.
- `pip` package manager installed.

## Installation

To get the Flask Pizza API up and running on your local system, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/levina23/flask-code-challenge-1
Navigate to the project directory:

cd flask-code-challenge-1
Create a virtual environment:

bash
python -m venv venv
Activate the virtual environment:

source venv/bin/activate
Install the required dependencies:

pipenv install && pipenv shell
Getting Started
Now that you have the Flask Pizza API installed, let's get started:

Make sure you are in the project directory:

cd flask-code-challenge-1
Ensure your virtual environment is activated.

Run the initial database migrations:

flask db upgrade
This command will create the necessary tables in the SQLite database.

Start the Flask development server:

python app.py
The server will run on http://127.0.0.1:5000/.

**API Endpoints**
The Flask Pizza API exposes several endpoints to interact with the system. Below is a list of available endpoints:

GET /restaurants: Retrieve a list of all restaurants.

GET /restaurants/<restaurant_id>: Retrieve information about a specific restaurant.

POST /restaurants: Create a new restaurant.

PUT /restaurants/<restaurant_id>: Update information about a restaurant.

DELETE /restaurants/<restaurant_id>: Delete a restaurant.

GET /pizzas: Retrieve a list of all pizzas.

GET /pizzas/<pizza_id>: Retrieve information about a specific pizza.

POST /pizzas: Create a new pizza.

PUT /pizzas/<pizza_id>: Update information about a pizza.

DELETE /pizzas/<pizza_id>: Delete a pizza.

GET /restaurants/<restaurant_id>/pizzas: Retrieve a list of pizzas associated with a specific restaurant.

POST /restaurants/<restaurant_id>/pizzas: Add a pizza to a restaurant's menu.

DELETE /restaurants/<restaurant_id>/pizzas/<pizza_id>: Remove a pizza from a restaurant's menu.

**Examples**
Here are some example use cases of the Flask Pizza API:

**Create a new restaurant:**
curl -X POST -H "Content-Type: application/json" -d '{"name": "Pizza Palace", "address": "123 Main St", "phone": "555-123-4567"}' http://127.0.0.1:5000/restaurants
curl http://127.0.0.1:5000/pizzas
**Add a pizza to a restaurant's menu:**
curl -X POST -H "Content-Type: application/json" -d '{"name": "Pepperoni Pizza", "price": 12.99}' http://127.0.0.1:5000/restaurants/1/pizzas

**Contributing**
Contributions to this project are welcome! If you'd like to contribute, please reach out to me on my GitHub @levina23.

License
This project is licensed under the MIT License.
