import os
from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError
from models import db  # Import the db object from your models.py file
from models import Restaurant
from routes import bp as routes_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'  # SQLite database
db.init_app(app)  # Initialize the db object

migrate = Migrate(app, db)

# Register the Blueprint to use the routes
app.register_blueprint(routes_blueprint)

# Define your routes here
@app.route('/')
def home():
    return "Welcome to the Pizza API!"

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Rest of your route definitions...

if __name__ == '__main__':
    app.run(debug=True)
