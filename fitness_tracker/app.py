from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
from models import *

@app.route('/')
def index():
    exercises = ExerciseLog.query.order_by(ExerciseLog.date.desc()).all()
    return render_template('index.html', exercises=exercises)

@app.route('/log', methods=['GET', 'POST'])
def log_exercise():
    if request.method == 'POST':
        name = request.form['name']
        duration = request.form['duration']
        calories = request.form['calories']
        log = ExerciseLog(name=name, duration=duration, calories=calories)
        db.session.add(log)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('log_exercise.html')

@app.route('/goals', methods=['GET', 'POST'])
def goals():
    if request.method == 'POST':
        goal_type = request.form['type']
        target = request.form['target']
        new_goal = Goal(goal_type=goal_type, target=target)
        db.session.add(new_goal)
        db.session.commit()
        return redirect(url_for('goals'))
    goals = Goal.query.all()
    return render_template('goals.html', goals=goals)

@app.route('/progress')
def progress():
    measurements = BodyMeasurement.query.order_by(BodyMeasurement.date.desc()).all()
    return render_template('progress.html', measurements=measurements)

if __name__ == '__main__':
    app.run(debug=True)
