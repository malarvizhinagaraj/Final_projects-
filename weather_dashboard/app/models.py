from .extensions import db

class UserPreference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100))
    units = db.Column(db.String(10))  # 'metric' or 'imperial'
