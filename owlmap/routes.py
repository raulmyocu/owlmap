from flask import render_template, url_for, flash, redirect
from owlmap import app
from owlmap.forms import LoginForm
from owlmap.models import User, Post

posts = [
    {
        'autor' : 'Raul Octavio Murcia Yocupicio',
        'titulo' : 'El primer post',
        'contenido' : 'Hola companeros este es el primer post del blog jaja salu2.',
        'fecha' : '3 de Abril de 2019'
    },
    {
        'autor' : 'Raulito Perez',
        'titulo' : 'El otro post',
        'contenido' : 'Ayuda amigos estoy atrapado en la Matrix...',
        'fecha' : '3 de Abril de 2090'
    }
]

@app.route("/")
@app.route("/home")
@app.route("/map")
def home():
    return render_template('home.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Sesion Iniciada', 'success')
        return redirect(url_for('forum'))
    return render_template('login.html', title='Iniciar Sesion', form=form)

@app.route("/forum")
def forum():
    return render_template('forum.html', title='Foro', posts=posts)
