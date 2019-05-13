from flask import render_template, url_for, flash, redirect, request
from owlmap import app, db
from owlmap.forms import LoginForm, SearchForm, RegistrationForm, CrudForm
from owlmap.models import User, Point, Post, Maestro

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

# -------------------  CRUD para puntos --------------------------------------

@app.route("/addPunto", methods=['GET', 'POST'])
def addInfoPunto():
    form = RegistrationForm()
    if form.validate_on_submit():
        punto = Point(clave=form.clave.data, lat=form.latitud.data,
                lng=form.longitud.data, nom=form.nombre.data,
                desc=form.descripcion.data)
        db.session.add(punto)
        db.session.commit()
        flash('Información guardada correctamente', 'success')
        return redirect(url_for('displayInfoPuntos'))
    return render_template('addInfoPuntos.html', title='Agregar Información',
                            form=form, leged='Agregar información')

@app.route("/displayPuntos", methods=['GET', 'POST'])
def displayInfoPuntos():
    form = CrudForm()
    puntos = Point.query.all()
    return render_template('displayPuntos.html', form=form, puntos=puntos, title="Mostrar Información")

@app.route("/editInfoPunto/<puntoID>",  methods=['GET', 'POST'])
def editInfoPunto(puntoID):
    punto = Point.query.get_or_404(puntoID)
    form = RegistrationForm()

    if form.validate_on_submit():
        punto.clave = form.clave.data
        punto.lat = form.latitud.data
        punto.lng = form.longitud.data
        punto.nom = form.nombre.data
        punto.desc = form.descripcion.data
        db.session.commit()
        flash('Información guardada correctamente', 'success')
        return redirect('displayPuntos')

    elif request.method == 'GET':
        form.clave.data = punto.clave
        form.latitud.data = punto.lat
        form.longitud.data = punto.lng
        form.nombre.data = punto.nom
        form.descripcion.data = punto.desc

    return render_template('addInfoPuntos.html', form=form, punto=punto,
                            title="Editar Información", leged='Editar información')


@app.route("/deleteInfoPunto/<puntoID>",  methods=['POST'])
def deleteInfoPunto(puntoID):
    punto = Point.query.get_or_404(puntoID)
    db.session.delete(punto)
    db.session.commit()
    flash('Registro eliminado correctamente', 'success')
    return redirect('displayPuntos')

# -------------------  CRUD para maestros --------------------------------------

@app.route("/addMaestro", methods=['GET', 'POST'])
def addInfoMaestro():
    form = RegistrationForm()
    if form.validate_on_submit():
        maestro = Maestro(clave=form.clave.data, lat=form.latitud.data,
                lng=form.longitud.data, nom=form.nombre.data,
                desc=form.descripcion.data)
        db.session.add(maestro)
        db.session.commit()
        flash('Información guardada correctamente', 'success')
        return redirect(url_for('displayMaestros'))
    return render_template('addInfoMaestros.html', title='Agregar Información',
                            form=form, leged='Agregar información')

@app.route("/displayMaestros", methods=['GET', 'POST'])
def displayInfoMaestros():
    form = CrudForm()
    maestros = Maestro.query.all()
    return render_template('displayMaestros.html', form=form, maestros=maestros, title="Mostrar Información")

@app.route("/editInfoMaestro/<puntoID>",  methods=['GET', 'POST'])
def editInfoMaestro(maestroID):
    maestro = Point.query.get_or_404(maestroID)
    form = RegistrationForm()

    if form.validate_on_submit():
        maestro.clave = form.clave.data
        maestro.lat = form.latitud.data
        maestro.lng = form.longitud.data
        maestro.nom = form.nombre.data
        maestro.desc = form.descripcion.data
        db.session.commit()
        flash('Información guardada correctamente', 'success')
        return redirect('display')

    elif request.method == 'GET':
        form.clave.data = maestro.clave
        form.latitud.data = maestro.lat
        form.longitud.data = maestro.lng
        form.nombre.data = maestro.nom
        form.descripcion.data = maestro.desc

    return render_template('addInfoMaestros.html', form=form, maestro=maestro,
                            title="Editar Información", leged='Editar información')

@app.route("/deleteInfoMaestro/<maestroID>",  methods=['GET', 'POST'])
def deleteInfoMaestro(maestroID):
    maestro = Point.query.get_or_404(maestroID)
    db.session.delete(maestro)
    db.session.commit()
    flash('Registro eliminado correctamente', 'success')
    return redirect('displayMaestros')
