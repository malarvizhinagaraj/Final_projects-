from flask import Blueprint, request, jsonify
from app import db
from models import ExerciseLog

api = Blueprint('api', __name__)

@api.route('/api/log', methods=['POST'])
def log_from_device():
    data = request.json
    log = ExerciseLog(name=data['name'], duration=data['duration'], calories=data['calories'])
    db.session.add(log)
    db.session.commit()
    return jsonify({"status": "success", "message": "Log added"}), 201
