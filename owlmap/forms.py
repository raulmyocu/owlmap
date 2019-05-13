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

class CrudForm(FlaskForm):
    editar = SubmitField('editar')
    eliminar = SubmitField('eliminar')
