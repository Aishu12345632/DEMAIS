from flask import Flask, render_template, request
import requests
app = Flask(__name__)
API_KEY = "98284da501aa12de56f8e74f07155135"

def aqi_parameters(aqi):
    if aqi<=50:
        return "Air this clean doesn’t come every day — open those windows!"
    elif aqi<=100:
        return "Light exercise outdoors is fine, just avoid peak traffic roads."
    elif aqi<=200:
        return "Air quality is manageable, but indoor workouts may feel better."
    else:
        return "Masks help, especially near traffic-heavy areas."
    