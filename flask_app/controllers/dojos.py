from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def new_all_dojos():
    dojos = Dojo.get_all()
    for dojo in dojos:
        print(dojo)
    return render_template('dojos.html', all_dojos=dojos)

@app.route('/add_dojo', methods=['POST'])
def add_dojo():
    data = {
        "name": request.form["name"]
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {
        'id': id
    }
    data = Dojo.get_dojo(data)[0]
    return render_template("dojo_show.html", ninjas=Dojo.get_dojo_ninjas(data), dojo=data)

@app.route('/new_ninja')
def new_ninja():
    dojos = Dojo.get_all()
    
    return render_template('new_ninja.html', dojos=dojos)

@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo_id" : request.form['dojo']
    }
    Ninja.save(data)
    return redirect('/dojos')