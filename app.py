# Import the Flask class from the flask package
from flask import Flask

# Create an 'app' instance
app = Flask(__name__)

# Define a 'route' (a URL)
# This '/' means the homepage
@app.route('/')
def hello_world():
    # This is what the user will see in their browser
    return 'Hello, World!'
    