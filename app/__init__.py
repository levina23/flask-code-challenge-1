from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'  # SQLite database
db = SQLAlchemy(app)

def create_app():
    from app import routes  # Import routes within the create_app function
    return app
