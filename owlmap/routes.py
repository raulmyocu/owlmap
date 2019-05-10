from flask import render_template, url_for, flash, redirect
from owlmap import app, db
from owlmap.forms import LoginForm, SearchForm, RegistrationForm
from owlmap.models import User, Point, Post

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
    },
    {
        'autor' : 'Raulito Perez',
        'titulo' : 'El otro post',
        'contenido' : 'Ayuda amigos estoy atrapado en la Matrix...',
        'fecha' : '3 de Abril de 2090'
    },
    {
        'autor' : 'Raulito Perez',
        'titulo' : 'El otro post',
        'contenido' : 'Ayuda amigos estoy atrapado en la Matrix...',
        'fecha' : '3 de Abril de 2090'
    }
]

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
@app.route("/map", methods=['GET', 'POST'])
def home():
    print("entraste a home")
    form = SearchForm()
    if form.validate_on_submit():
        print("simon si entendí carnal")
        results = Point.query.filter(Point.nom.contains(form.searchfield.data)).all()
        return render_template('home.html', form=form, results=results)
    return render_template('home.html', form=form)

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

@app.route("/add", methods=['GET', 'POST'])
def addInfo():
    form = RegistrationForm()
    if form.validate_on_submit():
        punto = Point(clave=form.clave.data, lat=form.latitud.data,
                lng=form.longitud.data, nom=form.nombre.data,
                desc=form.descripcion.data)
        db.session.add(punto)
        db.session.commit()
        flash('Información guardada correctamente', 'success')
        return redirect(url_for('addInfo'))
    return render_template('addInfo.html', title='Agregar Información', form=form)
