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
DBNAME = app.config['MONGO_DBNAME']    
app.config['USER'] = os.getenv('DBUSER')
USER = app.config['USER']    
app.config['MONGO_PWD'] = os.getenv('DBPWD')   
PWD = app.config['MONGO_PWD']    
# URI of database   
app.config['MONGO_URI'] = f"mongodb+srv://{USER}:{PWD}@cluster0.seola.mongodb.net/{DBNAME}?retryWrites=true&w=majority"

mongo = PyMongo(app)

# -- Routes section --
@app.route('/')
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
 
       # get the collection you want to use
       collection = mongo.db.recipe_collection
 
       # insert the new data
       collection.insert({'recipe': recipe_name, 'img': img_url})
       recipe = request.form['recipe_name']
       url = request.form['img_url']
       return render_template("yourgif.html", url = url, recipe=recipe, time = datetime.now())

