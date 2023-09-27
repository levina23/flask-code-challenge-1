# flask-code-challenge-1
# Flask Pizza API

The Flask Pizza API is a simple web application that allows you to manage pizza restaurants and their menus. You can create, read, update, and delete restaurants and pizzas, as well as associate pizzas with restaurants.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6+ installed on your system.
- pip package manager installed.

## Installation

Follow these steps to set up the Flask Pizza API:

1 Clone the repository to your local machine:
git clone https://github.com/levina23/flask-code-challenge-1
Navigate to the project directory:
 cd flask-code-challenge-1

**Create a virtual environment**:
  python -m venv venv

**Activate the virtual environment:**
  source venv/bin/activate

**Install the required dependencies:**
  pipenv install && pipenv shell
  
**Usage**
**Navigate to the project directory **
  cd flask-code-challenge-1
  Ensure your virtual environment is activated 

**Run the initial database migrations:**
flask db upgrade
This will create the necessary tables in the SQLite database.

Start the Flask development server:
python app.py
The server will run on http://127.0.0.1:5000/.

Use an API client (e.g., Postman) or make HTTP requests to interact with the API using the provided endpoints.

When you're finished, you can stop the server by pressing Ctrl+C.

**Contributing**
Contributions are welcome! If you'd like to contribute to this project, please reach out to me on my github @levina23

**License**
This project is licensed under the MIT License. 
