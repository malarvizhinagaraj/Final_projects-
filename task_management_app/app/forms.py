from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, DateField, SelectField
from wtforms.validators import DataRequired, Email, Length

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class ProjectForm(FlaskForm):
    name = StringField("Project Name", validators=[DataRequired()])
    description = TextAreaField("Description")
    submit = SubmitField("Create Project")

class TaskForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = TextAreaField("Description")
    due_date = DateField("Due Date", format='%Y-%m-%d')
    priority = SelectField("Priority", choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    assigned_to = StringField("Assign To (User ID)")
    submit = SubmitField("Create Task")
