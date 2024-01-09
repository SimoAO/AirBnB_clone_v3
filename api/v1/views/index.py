#!/usr/bin/python3
"""blueprint routes status module"""

from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
from models import storage
from models.amnity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', strict_slashes=False)
def status():
    """Returns a JSON: status: OK"""
    return jsonify({
        "status": "OK",
    })


@app_views.route('/stats', strict_slashes=False)
def stats():
    """An endpoint that retrieves the num of each objs by type"""
    amenities = storage.count("Amenity")
    cities = storage.count("City")
    places = storage.count("Place")
    reviews = storage.count("Review")
    states = storage.count("State")
    users = storage.count("User")
    return jsonify({
        "amenities": amenities,
        "cities": cities,
        "places": places,
        "reviews": reviews,
        "states": states,
        "users": users,
    })
