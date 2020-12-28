from movements import app
from flask import render_template 

import random

@app.route('/')
def listaMovimientos():  #También puede llamarse --> def index():
    return render_template("movementsList.html")