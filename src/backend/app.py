from flask import Flask
from flask_cors import CORS
from __init__ import create_app

app = create_app()

# Enable CORS
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)
