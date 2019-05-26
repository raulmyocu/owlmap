from flask import render_template, url_for, flash, redirect, request, request
from owlmap import app, db
from owlmap.forms import LoginForm, RegistrationForm, RegistrationFormMaestro, RegistrationFormCubSal
from owlmap.models import User, Maestro, Edificio, Salon, Cubiculo, Servicios
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
@app.route("/map", methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash('Sesion Iniciada', 'success')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Error al iniciar sesión. Verifique el correo y contraseña', 'danger')
    return render_template('login.html', title='Iniciar Sesion', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/displayInfo", methods=['GET', 'POST'])
@login_required
def displayInfo():
    edificios = Edificio.query.all()
    cubiculos = Cubiculo.query.all()
    salones = Salon.query.all()
    servicios = Servicios.query.all()
    return render_template('displayInfo.html', edificios=edificios, salones=salones,
    cubiculos=cubiculos, servicios=servicios, title="Mostrar Información")

@app.route("/addInfo", methods=['GET', 'POST'])
@login_required
def addInfo():
    return render_template('addInfo.html', title="Agregar Información")

# ---------------------  CRUD para Edificios --------------------------------------

@app.route("/addEdificio", methods=['GET', 'POST'])
@login_required
def addInfoEdificio():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            edificio = Edificio(clave=form.clave.data, lat=form.latitud.data,
                    lng=form.longitud.data, nom=form.nombre.data,
                    desc=form.descripcion.data)
            db.session.add(edificio)
            db.session.commit()
            flash('Información guardada correctamente', 'success')
            return redirect(url_for('displayInfo'))
        except:
            db.session.rollback()
            flash('Hubo un error al capturar la información', 'danger')
    return render_template('addInfoEdificios.html', title='Agregar información de edificio',
                            form=form, legend='Agregar información de edificio')

@app.route("/editInfoEdificio/<edificioID>",  methods=['GET', 'POST'])
@login_required
def editInfoEdificio(edificioID):
    edificio = Edificio.query.get_or_404(edificioID)
    form = RegistrationForm()

    if form.validate_on_submit():
        try:
            edificio.clave = form.clave.data
            edificio.lat = form.latitud.data
            edificio.lng = form.longitud.data
            edificio.nom = form.nombre.data
            edificio.desc = form.descripcion.data
            db.session.commit()
            flash('Información guardada correctamente', 'success')
            return redirect(url_for('displayInfo'))
        except:
            db.session.rollback()
            flash('Hubo un error al capturar la información', 'danger')

    elif request.method == 'GET':
        form.clave.data = edificio.clave
        form.latitud.data = edificio.lat
        form.longitud.data = edificio.lng
        form.nombre.data = edificio.nom
        form.descripcion.data = edificio.desc

    return render_template('addInfoEdificios.html', form=form, edificio=edificio,
                            title="Editar Información de edificio", legend='Editar información de edificio')


@app.route("/deleteInfoEdificio/<edificioID>",  methods=['GET','POST'])
@login_required
def deleteInfoEdificio(edificioID):
    edificio = Edificio.query.get_or_404(edificioID)
    try:
        db.session.delete(edificio)
        db.session.commit()
        flash('Registro eliminado correctamente', 'success')
    except:
        flash('Hubo un error en la eliminación de la información', 'danger')
    return redirect(url_for('displayInfo'))



# ---------------------  CRUD para Cubiculo --------------------------------------

@app.route("/addCubiculo", methods=['GET', 'POST'])
@login_required
def addInfoCubiculo():
    form = RegistrationFormCubSal()
    edificios = Edificio.query.all()
    if edificios:
        form.edificio.data = request.form.get('comp_select')
        if form.validate_on_submit():
            try:
                cubiculo = Cubiculo(clave=form.clave.data, lat=form.latitud.data,
                        lng=form.longitud.data, nom=form.nombre.data,
                        desc=form.descripcion.data, edif_clave=form.edificio.data)
                db.session.add(cubiculo)
                db.session.commit()
                flash('Información guardada correctamente', 'success')
                return redirect(url_for('displayInfo'))
            except:
                db.session.rollback()
                flash('Hubo un error al capturar la información', 'danger')
    else:
        form.edificio.data = '--'
        if form.validate_on_submit():
            try:
                cubiculo = Cubiculo(clave=form.clave.data, lat=form.latitud.data,
                        lng=form.longitud.data, nom=form.nombre.data,
                        desc=form.descripcion.data, edif_clave=form.edificio.data)
                db.session.add(cubiculo)
                db.session.commit()
                flash('Información guardada correctamente', 'success')
                return redirect(url_for('displayInfo'))
            except:
                db.session.rollback()
                flash('Hubo un error al capturar la información', 'danger')

    return render_template('addInfoCubiculos.html', title='Agregar información de cubículo',
                            form=form, legend='Agregar información de cubículo', edificios=edificios)

@app.route("/editInfoCubiculo/<cubiculoID>",  methods=['GET', 'POST'])
@login_required
def editInfoCubiculo(cubiculoID):
    cubiculo = Cubiculo.query.get_or_404(cubiculoID)
    edificios = Edificio.query.all()
    edifinicial = Edificio.query.filter(Edificio.clave.contains(cubiculo.edif_clave)).first()
    form = RegistrationFormCubSal()

    form.edificio.data = request.form.get('comp_select')

    if form.validate_on_submit():
        try:
            cubiculo.clave = form.clave.data
            cubiculo.lat = form.latitud.data
            cubiculo.lng = form.longitud.data
            cubiculo.nom = form.nombre.data
            cubiculo.desc = form.descripcion.data
            cubiculo.edif_clave = form.edificio.data
            db.session.commit()
            flash('Información guardada correctamente', 'success')
            return redirect(url_for('displayInfo'))
        except:
            db.session.rollback()
            flash('Hubo un error al capturar la información', 'danger')

    elif request.method == 'GET':
        form.clave.data = cubiculo.clave
        form.latitud.data = cubiculo.lat
        form.longitud.data = cubiculo.lng
        form.nombre.data = cubiculo.nom
        form.descripcion.data = cubiculo.desc
        form.edificio.data = cubiculo.edif_clave

    return render_template('addInfoCubiculos.html', form=form, edificios=edificios, edifinicial=edifinicial,
                            title="Editar Información", legend='Editar información de cubículo')


@app.route("/deleteInfoCubiculo/<cubiculoID>",  methods=['GET','POST'])
@login_required
def deleteInfoCubiculo(cubiculoID):
    cubiculo = Cubiculo.query.get_or_404(cubiculoID)
    try:
        db.session.delete(cubiculo)
        db.session.commit()
        flash('Registro eliminado correctamente', 'success')
    except:
        flash('Hubo un error en la eliminación de la información', 'danger')
    return redirect(url_for('displayInfo'))

# ---------------------  CRUD para Salon --------------------------------------

@app.route("/addSalon", methods=['GET', 'POST'])
@login_required
def addInfoSalon():
    form = RegistrationFormCubSal()
    edificios = Edificio.query.all()
    if edificios:
        form.edificio.data = request.form.get('comp_select')
        if form.validate_on_submit():
            try:
                salon = Salon(clave=form.clave.data, lat=form.latitud.data,
                        lng=form.longitud.data, nom=form.nombre.data,
                        desc=form.descripcion.data, edif_clave=form.edificio.data)
                db.session.add(salon)
                db.session.commit()
                flash('Información guardada correctamente', 'success')
                return redirect(url_for('displayInfo'))
            except:
                db.session.rollback()
                flash('Hubo un error al capturar la información', 'danger')
    else:
        form.edificio.data = '--'
        if form.validate_on_submit():
            try:
                salon = Salon(clave=form.clave.data, lat=form.latitud.data,
                        lng=form.longitud.data, nom=form.nombre.data,
                        desc=form.descripcion.data, edif_clave=form.edificio.data)
                db.session.add(salon)
                db.session.commit()
                flash('Información guardada correctamente', 'success')
                return redirect(url_for('displayInfo'))
            except:
                db.session.rollback()
                flash('Hubo un error al capturar la información', 'danger')

    return render_template('addInfoSalones.html', title='Agregar información de salón',
                            form=form, legend='Agregar información de salón', edificios=edificios)

@app.route("/editInfoSalon/<salonID>",  methods=['GET', 'POST'])
@login_required
def editInfoSalon(salonID):
    salon = Salon.query.get_or_404(salonID)
    edificios = Edificio.query.all()
    edifinicial = Edificio.query.filter(Edificio.clave.contains(salon.edif_clave)).first()
    form = RegistrationFormCubSal()

    form.edificio.data = request.form.get('comp_select')

    if form.validate_on_submit():
        try:
            salon.clave = form.clave.data
            salon.lat = form.latitud.data
            salon.lng = form.longitud.data
            salon.nom = form.nombre.data
            salon.desc = form.descripcion.data
            salon.edif_clave = form.edificio.data
            db.session.commit()
            flash('Información guardada correctamente', 'success')
            return redirect(url_for('displayInfo'))
        except:
            db.session.rollback()
            flash('Hubo un error al capturar la información', 'danger')

    elif request.method == 'GET':
        form.clave.data = salon.clave
        form.latitud.data = salon.lat
        form.longitud.data = salon.lng
        form.nombre.data = salon.nom
        form.descripcion.data = salon.desc
        form.edificio.data = salon.edif_clave

    return render_template('addInfoSalones.html', form=form, edificios=edificios, edifinicial=edifinicial,
                            title="Editar Información", legend='Editar información de cubículo')


@app.route("/deleteInfoSalon/<salonID>",  methods=['GET','POST'])
@login_required
def deleteInfoSalon(salonID):
    salon = Salon.query.get_or_404(salonID)
    try:
        db.session.delete(salon)
        db.session.commit()
        flash('Registro eliminado correctamente', 'success')
    except:
        flash('Hubo un error en la eliminación de la información', 'danger')
    return redirect(url_for('displayInfo'))
# ---------------------  CRUD para Servicios --------------------------------------

@app.route("/addServicios", methods=['GET', 'POST'])
@login_required
def addInfoServicio():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            servicio = Servicios(clave=form.clave.data, lat=form.latitud.data,
                    lng=form.longitud.data, nom=form.nombre.data,
                    desc=form.descripcion.data)
            db.session.add(servicio)
            db.session.commit()
            flash('Información guardada correctamente', 'success')
            return redirect(url_for('displayInfo'))
        except:
            #db.session.rollback()
            flash('Hubo un error al capturar la información', 'danger')
    return render_template('addInfoServicios.html', title='Agregar información de servicio',
                            form=form, legend='Agregar información')

@app.route("/editInfoServicio/<servicioID>",  methods=['GET', 'POST'])
@login_required
def editInfoServicio(servicioID):
    servicio = Servicios.query.get_or_404(servicioID)
    form = RegistrationForm()

    if form.validate_on_submit():
        try:
            servicio.clave = form.clave.data
            servicio.lat = form.latitud.data
            servicio.lng = form.longitud.data
            servicio.nom = form.nombre.data
            servicio.desc = form.descripcion.data
            db.session.commit()
            flash('Información guardada correctamente', 'success')
            return redirect(url_for('displayInfo'))
        except:
            db.session.rollback()
            flash('Hubo un error al capturar la información', 'danger')

    elif request.method == 'GET':
        form.clave.data = servicio.clave
        form.latitud.data = servicio.lat
        form.longitud.data = servicio.lng
        form.nombre.data = servicio.nom
        form.descripcion.data = servicio.desc

    return render_template('addInfoServicios.html', form=form, servicio=servicio,
                            title="Editar Información", legend='Editar información de servicio')


@app.route("/deleteInfoServicio/<servicioID>",  methods=['GET','POST'])
@login_required
def deleteInfoServicio(servicioID):
    servicio = Servicios.query.get_or_404(servicioID)
    try:
        db.session.delete(servicio)
        db.session.commit()
        flash('Registro eliminado correctamente', 'success')
    except:
        flash('Hubo un error en la eliminación de la información', 'danger')
    return redirect(url_for('displayInfo'))


# -------------------  CRUD para maestros --------------------------------------

@app.route("/addMaestro", methods=['GET', 'POST'])
@login_required
def addInfoMaestro():
    form = RegistrationFormMaestro()
    cubiculos = Cubiculo.query.all()
    if cubiculos:
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
                db.session.rollback()
                flash('Hubo un error al capturar la información', 'danger')
    else:
        form.cubo.data = '--'
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
                db.session.rollback()
                flash('Hubo un error al capturar la información', 'danger')

    return render_template('addInfoMaestros.html', title='Agregar Información',
                            form=form, legend='Agregar información de maestro', cubiculos=cubiculos)

@app.route("/displayMaestros", methods=['GET', 'POST'])
@login_required
def displayInfoMaestros():
    maestros = Maestro.query.all()
    return render_template('displayMaestros.html', maestros=maestros,
                            title="Mostrar Información")

@app.route("/editInfoMaestro/<maestroID>",  methods=['GET', 'POST'])
@login_required
def editInfoMaestro(maestroID):
    maestro = Maestro.query.get_or_404(maestroID)
    form = RegistrationFormMaestro()
    cubiculos = Cubiculo.query.all()
    cuboinicial = Cubiculo.query.filter(Cubiculo.clave.contains(maestro.cubo)).first()

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
            return redirect(url_for('displayInfoMaestros'))
        except:
            db.session.rollback()
            flash('Hubo un error al capturar la información de maestro', 'danger')

    elif request.method == 'GET':

        form.exp.data = maestro.exp
        form.nombres.data = maestro.nombres
        form.apellidos.data = maestro.apellidos
        form.email.data = maestro.email
        form.tel.data = maestro.tel
        form.cubo.data = maestro.cubo

    return render_template('addInfoMaestros.html', form=form, maestro=maestro,
                            title="Editar Información", legend='Editar información de maestro',
                            cubiculos=cubiculos, cuboinicial=cuboinicial)


@app.route("/deleteInfoMaestro/<maestroID>",  methods=['GET','POST'])
@login_required
def deleteInfoMaestro(maestroID):
    maestro = Maestro.query.get_or_404(maestroID)
    try:
        db.session.delete(maestro)
        db.session.commit()
        flash('Registro eliminado correctamente', 'success')
    except:
        db.session.rollback()
        flash('Hubo un error en la eliminación de la información', 'danger')
    return redirect(url_for('displayInfoMaestros'))

# -------------------  Búsqueda --------------------------------------

@app.route("/search=<stringToSearch>")
def search(stringToSearch):
    conectores = ["de", "la", "el", "en", "y", "a", "los", "se", "del", "las", "con", "una", "su",
                "para", "es", "al", "como", "o", "pero", "me", "entre"] # Palabras comunes que no necesitamos buscar

    results = Edificio.query.filter(Edificio.nom.contains(stringToSearch)).all()
    print(render_template('results.html', results=results))
    return render_template('results.html', results=results)
