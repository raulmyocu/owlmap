from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Correo institucional', validators=[DataRequired(), Email()],
            render_kw={"placeholder": "Correo institucional"})
    password = PasswordField('Contresena', validators=[DataRequired()],
            render_kw={"placeholder": "Contrasena"})
    remember = BooleanField('Recordarme')
    submit = SubmitField('Iniciar sesion')
