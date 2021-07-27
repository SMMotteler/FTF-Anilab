# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request, redirect
from datetime import datetime
from model import getImageUrlFrom
from flask_pymongo import PyMongo
import os
from bson.objectid import ObjectId

# -- Initialization section --
app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.getenv('DBNAME')
dbname = app.config['MONGO_DBNAME']    
app.config['USER'] = os.getenv('DBUSER')
user = app.config['USER']    
app.config['MONGO_PWD'] = os.getenv('DBPWD')   
pwd = app.config['MONGO_PWD']    

is_prod = os.environ.get('IS_HEROKU', None)
if is_prod:
    dbname = os.environ.get('DBNAME')
    user = os.environ.get('DBUSER')
    pwd = os.environ.get('DBPWD')
# URI of database   
app.config['MONGO_URI'] = f"mongodb+srv://{user}:{pwd}@cluster0.seola.mongodb.net/{dbname}?retryWrites=true&w=majority"
mongo = PyMongo(app)

# -- Routes section --
@app.route('/')
@app.route('/homepage')
def home():
    return render_template('homepage.html')

@app.route('/recipes')
def handle_recipes():
    return render_template('recipes.html')

@app.route('/index')
def index():
    collection = mongo.db.recipe_collection
    recipes = collection.find({})
    return render_template("index.html", time = datetime.now(), recipes=recipes)

@app.route('/your_recipe', methods = ['GET', 'POST'])
def handle_recipe():
    if request.method == "GET":
       return "You didn't put in a recipe :("
    else:
       print(request.form)
       recipe_name = request.form['recipe_name']
       img_url = request.form['img_url']
       user = request.form['user']
       ingredients = request.form['ingredients']
       recipe_steps = request.form['recipe_steps']

       # get the collection you want to use
       collection = mongo.db.recipe_collection
       # insert the new data
       collection.insert({'recipe': recipe_name, 'img': img_url, 'user': user, 'ingredients': ingredients, 'recipe_steps': recipe_steps})
       return render_template("your_recipe.html", url = img_url, recipe=recipe_name, time = datetime.now())

# Delete one using id
@app.route('/remove/<recipe_id>')
def remove_event(recipe_id):
   collection = mongo.db.recipe_collection
   collection.delete_one({'_id': ObjectId(recipe_id)})
   return redirect('/')

@app.route('/recipes/<recipe_id>')
def show_recipe(recipe_id):
   return "This is a placeholder for showing individual recipes"

@app.route('/about')
def about():
    return "This is a placeholder for our About page"

@app.route('/form')
def form():
    return "This is a placeholder for our Form page"