#!/usr/bin/python3
"""Create a basics routes and register the blueprint"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import environ, getenv

app = Flask(__name__)
app.url_map.strict_slashes = False

host = environ.get('HBNB_API_HOST') or '0.0.0.0'
port = environ.get('HBNB_API_PORT') or 5000

app.register_blueprint(app_views)


@app.teardown_appcontext
def close(Error):
    """Close the storage"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Return error page 404 """
    return jsonify({'error': 'Not found'}), 404


if __name__ == "__main__":
    app.run(host=host, port=port, debug=True, threaded=True)
