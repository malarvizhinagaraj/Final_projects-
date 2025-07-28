import requests
from flask import Blueprint, render_template, request, redirect, url_for
from .models import UserPreference
from .extensions import db
from datetime import datetime, timedelta

bp = Blueprint('main', __name__)

API_KEY = 'your_openweathermap_api_key'
BASE_URL = 'https://api.openweathermap.org/data/2.5/'

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        units = request.form.get('units', 'metric')
        pref = UserPreference(location=location, units=units)
        db.session.add(pref)
        db.session.commit()
        return redirect(url_for('main.dashboard', loc=location, units=units))
    return render_template('index.html')

@bp.route('/dashboard')
def dashboard():
    location = request.args.get('loc', 'New York')
    units = request.args.get('units', 'metric')

    current_url = f"{BASE_URL}weather?q={location}&appid={API_KEY}&units={units}"
    forecast_url = f"{BASE_URL}forecast?q={location}&appid={API_KEY}&units={units}"

    current_data = requests.get(current_url).json()
    forecast_data = requests.get(forecast_url).json()

    severe_alerts = []
    if 'weather' in current_data:
        for w in current_data['weather']:
            if w['id'] < 800:
                severe_alerts.append(w['description'])

    return render_template('dashboard.html',
                           current=current_data,
                           forecast=forecast_data,
                           location=location,
                           units=units,
                           alerts=severe_alerts)
