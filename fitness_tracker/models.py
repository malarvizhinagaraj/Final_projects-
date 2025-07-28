from app import db

class ExerciseLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    duration = db.Column(db.Integer)  # in minutes
    calories = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.utcnow)

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    goal_type = db.Column(db.String(100))
    target = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

class BodyMeasurement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Float)
    waist = db.Column(db.Float)
    chest = db.Column(db.Float)
    biceps = db.Column(db.Float)
    date = db.Column(db.DateTime, default=datetime.utcnow)

class CalorieLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food = db.Column(db.String(100))
    calories = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.utcnow)

class WaterLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)  # in liters
    date = db.Column(db.DateTime, default=datetime.utcnow)
