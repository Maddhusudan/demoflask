from flask import Flask, jsonify
from vercel_wsgi import handle_request

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify(message="Hello from Flask on Vercel!")

# Vercel uses this handler
def handler(environ, start_response):
    return handle_request(app, environ, start_response)
