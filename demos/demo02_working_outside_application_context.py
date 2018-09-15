from flask import Flask, current_app, request


app = Flask(__name__)

a = current_app
d = a.config['DEBUG']
