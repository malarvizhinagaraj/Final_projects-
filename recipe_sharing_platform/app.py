from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models import *

@app.route('/')
def index():
    recipes = Recipe.query.order_by(Recipe.timestamp.desc()).all()
    return render_template('index.html', recipes=recipes)

@app.route('/recipe/<int:recipe_id>')
def recipe_view(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    reviews = Review.query.filter_by(recipe_id=recipe_id).all()
    return render_template('recipe.html', recipe=recipe, reviews=reviews)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        dietary_tags = request.form.get('dietary_tags', '')
        new_recipe = Recipe(title=title, ingredients=ingredients, instructions=instructions, dietary_tags=dietary_tags)
        db.session.add(new_recipe)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('submit.html')

if __name__ == "__main__":
    app.run(debug=True)
