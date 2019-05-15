from flask import render_template, url_for, flash, redirect, request
from owlmap import app, db
from owlmap.forms import LoginForm, SearchForm, RegistrationForm, RegistrationFormMaestro
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
    form = SearchForm()
    if form.validate_on_submit():
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
        try:
            punto = Point(clave=form.clave.data, lat=form.latitud.data,
                    lng=form.longitud.data, nom=form.nombre.data,
                    desc=form.descripcion.data)
            db.session.add(punto)
            db.session.commit()
            flash('Información guardada correctamente', 'success')
            return redirect(url_for('displayInfoPuntos'))
        except:
            flash('Hubo un error al capturar la información', 'danger')
    return render_template('addInfoPuntos.html', title='Agregar Información',
                            form=form, legend='Agregar información')

@app.route("/displayPuntos", methods=['GET', 'POST'])
def displayInfoPuntos():
    puntos = Point.query.all()
    return render_template('displayPuntos.html', puntos=puntos, title="Mostrar Información")

@app.route("/editInfoPunto/<puntoID>",  methods=['GET', 'POST'])
def editInfoPunto(puntoID):
    punto = Point.query.get_or_404(puntoID)
    form = RegistrationForm()

    if form.validate_on_submit():
        try:
            punto.clave = form.clave.data
            punto.lat = form.latitud.data
            punto.lng = form.longitud.data
            punto.nom = form.nombre.data
            punto.desc = form.descripcion.data
            db.session.commit()
            flash('Información guardada correctamente', 'success')
            return redirect('displayPuntos')
        except:
            flash('Hubo un error al capturar la información', 'danger')

    elif request.method == 'GET':
        form.clave.data = punto.clave
        form.latitud.data = punto.lat
        form.longitud.data = punto.lng
        form.nombre.data = punto.nom
        form.descripcion.data = punto.desc

    return render_template('addInfoPuntos.html', form=form, punto=punto,
                            title="Editar Información", legend='Editar información')


@app.route("/deleteInfoPunto/<puntoID>",  methods=['GET','POST'])
def deleteInfoPunto(puntoID):
    punto = Point.query.get_or_404(puntoID)
    try:
        db.session.delete(punto)
        db.session.commit()
        flash('Registro eliminado correctamente', 'success')
    except:
        flash('Hubo un error en la eliminación de la información', 'danger')
    return redirect('displayPuntos')

# -------------------  CRUD para maestros --------------------------------------

@app.route("/addMaestro", methods=['GET', 'POST'])
def addInfoMaestro():
    form = RegistrationFormMaestro()
    puntos = Point.query.all()
    form.cubo.data = request.form.get('comp_select')
    if form.validate_on_submit():
        try:
            maestro = Maestro(exp=form.exp.data, cubo=form.cubo.data,
                        nombres=form.nombres.data, apellidos=form.apellidos.data,
                        email=form.email.data, tel=form.tel.data)
            db.session.add(maestro)
            db.session.commit()
            flash('Información guardada correctamente', 'success')
            return redirect(url_for('displayInfoMaestros'))
        except:
            flash('Hubo un error al capturar la información', 'danger')
    return render_template('addInfoMaestros.html', title='Agregar Información',
                            form=form, legend='Agregar información', puntos=puntos)

@app.route("/displayMaestros", methods=['GET', 'POST'])
def displayInfoMaestros():
    maestros = Maestro.query.all()
    return render_template('displayMaestros.html', maestros=maestros,
                            title="Mostrar Información")

@app.route("/editInfoMaestro/<maestroID>",  methods=['GET', 'POST'])
def editInfoMaestro(maestroID):
    maestro = Maestro.query.get_or_404(maestroID)
    form = RegistrationFormMaestro()
    puntos = Point.query.all()
    puntoinicial = Point.query.filter(Point.clave.contains(maestro.cubo)).first()

    form.cubo.data = request.form.get('comp_select')

    if form.validate_on_submit():
        try:
            maestro.exp = form.exp.data
            maestro.cubo = form.cubo.data 
            maestro.nombres = form.nombres.data
            maestro.apellidos = form.apellidos.data
            maestro.email = form.email.data
            maestro.tel = form.tel.data
            db.session.commit()
            flash('Información guardada correctamente', 'success')
            return redirect('displayMaestros')
        except:
            flash('Hubo un error al capturar la información', 'danger')

    elif request.method == 'GET':

        form.exp.data = maestro.exp
        form.nombres.data = maestro.nombres
        form.apellidos.data = maestro.apellidos
        form.email.data = maestro.email
        form.tel.data = maestro.tel
        form.cubo.data = maestro.cubo

    return render_template('addInfoMaestros.html', form=form, maestro=maestro,
                            title="Editar Información", legend='Editar información',
                            puntos=puntos, puntoinicial=puntoinicial)


@app.route("/deleteInfoMaestro/<maestroID>",  methods=['GET','POST'])
def deleteInfoMaestro(maestroID):
    maestro = Maestro.query.get_or_404(maestroID)
    try:
        db.session.delete(maestro)
        db.session.commit()
        flash('Registro eliminado correctamente', 'success')
    except:
        flash('Hubo un error en la eliminación de la información', 'danger')
    return redirect('displayMaestros')
