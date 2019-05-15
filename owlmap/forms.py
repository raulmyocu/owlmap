from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Correo institucional', validators=[DataRequired()],
            render_kw={"placeholder": "Correo institucional"})
    password = PasswordField('Contraseña', validators=[DataRequired()],
            render_kw={"placeholder": "Contraseña"})
    remember = BooleanField('Recordarme')
    submit = SubmitField('Iniciar sesión')


class SearchForm(FlaskForm):
    searchfield = StringField('Busqueda', validators=[DataRequired()],
            render_kw={"placeholder": "¿Qué estás buscando?"})
    submit = SubmitField('Buscar')

class RegistrationForm(FlaskForm):
    clave = StringField('Clave del punto', validators=[Length(min=2, max=5), DataRequired()],
            render_kw={"placeholder": "Clave"})
    latitud = StringField('Latitud del punto', validators=[DataRequired()],
            render_kw={"placeholder": "Latitud"})
    longitud = StringField('Longitud del punto', validators=[DataRequired()],
            render_kw={"placeholder": "Longitud"})
    nombre = StringField('Nombre', validators=[Length(min=5, max=60), DataRequired()],
            render_kw={"placeholder": "Nombre"})
    descripcion = StringField('Descripción', validators=[DataRequired()],
            render_kw={"placeholder": "Descripción"})
    submit = SubmitField('Guardar información')


class RegistrationFormMaestro(FlaskForm):
    exp = StringField('Expediente', validators=[Length(min=10, max=20), DataRequired()],
            render_kw={"placeholder": "Expediente"})
    cubo = StringField('Cubiculo', validators=[DataRequired()],
            render_kw={"placeholder": "Cubículo"})
    nombres = StringField('Nombres', validators=[Length(min=5, max=60), DataRequired()],
            render_kw={"placeholder": "Nombres"})
    apellidos = StringField('Apellidos', validators=[Length(min=5, max=60), DataRequired()],
            render_kw={"placeholder": "Apellidos"})
    email = StringField('Correo', validators=[Length(min=5, max=60), DataRequired()],
            render_kw={"placeholder": "Correo electrónico"})
    tel = StringField('Telefono', validators=[Length(min=10, max=16), DataRequired()],
            render_kw={"placeholder": "Número de teléfono"})
    cubo = StringField('Cubo', validators=[Length(min=2, max=5), DataRequired()],
            render_kw={"placeholder": "Cubículo"})

    submit = SubmitField('Guardar información ')
