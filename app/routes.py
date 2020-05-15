from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    #mock user objects
    user = {'username': 'Sidd_Ajri'}
    posts = [
        {
            'author': {'username': 'Sidd_Ajri'},
            'body': 'Ima nap'
        },
        {
            'author': {'username': 'Nish'},
            'body': 'The Upload show was so cool!'
        }
    ]
    return render_template('index.html', title='Ahoy Maties', user=user, posts=posts) #rendering your HTML

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
