from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Post
from .forms import RegisterForm, LoginForm, PostForm
from . import db
import markdown

# ✅ THIS LINE FIXES YOUR ERROR
bp = Blueprint('main', __name__)

def api_register():
    data = request.json
    if not all(k in data for k in ('username', 'email', 'password')):
        return jsonify({'error': 'Missing data'}), 400

    existing = User.query.filter((User.email == data['email']) | (User.username == data['username'])).first()
    if existing:
        return jsonify({'error': 'User already exists'}), 409

    user = User(
        username=data['username'],
        email=data['email'],
        password=generate_password_hash(data['password'])
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201


@bp.route('/api/login', methods=['POST'])
def api_login():
    data = request.json
    user = User.query.filter_by(email=data.get('email')).first()
    if user and check_password_hash(user.password, data.get('password')):
        login_user(user)
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'error': 'Invalid credentials'}), 401


@bp.route('/api/posts', methods=['POST'])
@login_required
def api_create_post():
    data = request.json
    if not all(k in data for k in ('title', 'content')):
        return jsonify({'error': 'Missing title or content'}), 400

    post = Post(title=data['title'], content=data['content'], user_id=current_user.id)
    db.session.add(post)
    db.session.commit()
    return jsonify({'message': 'Post created', 'post_id': post.id}), 201
