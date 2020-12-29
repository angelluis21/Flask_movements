from movements import app
from flask import render_template 
import csv

@app.route('/')
def listaIngresos():      #También puede llamarse --> def index():
    fIngresos = open("movements/data/basededatos.csv", "r")
    csvReader = csv.reader(fIngresos, delimiter=',', quotechar='"')
    ingresos = list(csvReader)

    sumador = 0
    for ingreso in ingresos:
        sumador += float(ingreso[2])

    print(ingresos) #Ponemos este 'print' para ver en la consola. No hay que ponerlo para el código.

    return render_template("movementsList.html", datos=ingresos, total=sumador)

@app.route('/creaalta')
def nuevoIngreso():
    return 'Ya el miercoles si eso te enseño el formulario'