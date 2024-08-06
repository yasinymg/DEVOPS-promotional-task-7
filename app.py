from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    message = os.getenv('WELCOME_MESSAGE', 'Hello, Welcome to KodeCamp DevOps Bootcamp!')
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
