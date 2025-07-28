from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Project, Task, Comment
from .forms import RegisterForm, LoginForm, ProjectForm, TaskForm
from .extensions import db
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return "<h1>Welcome to Task Manager App</h1>"

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data)
        user = User(email=form.email.data, password=hashed_pw, name=form.name.data)
        db.session.add(user)
        db.session.commit()
        flash("Registered successfully!", "success")
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Logged in!", "success")
            return redirect(url_for('main.dashboard'))
        flash("Invalid credentials", "danger")
    return render_template('login.html', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out.", "info")
    return redirect(url_for('main.index'))

@bp.route('/dashboard')
@login_required
def dashboard():
    projects = Project.query.filter_by(owner_id=current_user.id).all()
    return render_template('dashboard.html', projects=projects)

@bp.route('/project/new', methods=['GET', 'POST'])
@login_required
def new_project():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(name=form.name.data, description=form.description.data, owner_id=current_user.id)
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('new_project.html', form=form)

@bp.route('/project/<int:project_id>/task/new', methods=['GET', 'POST'])
@login_required
def new_task(project_id):
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            due_date=form.due_date.data,
            priority=form.priority.data,
            project_id=project_id,
            assigned_to=form.assigned_to.data
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('new_task.html', form=form)
