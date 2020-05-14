from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():	
    user = {'username': 'Sidd_Ajri'}    #mock user object
    return render_template('index.html', title='Ahoy Maties', user=user) #rendering your HTML
