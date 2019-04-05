from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Correo institucional', validators=[DataRequired()],
            render_kw={"placeholder": "Correo institucional"})
    password = PasswordField('Contraseña', validators=[DataRequired()],
            render_kw={"placeholder": "Contraseña"})
    remember = BooleanField('Recordarme')
    submit = SubmitField('Iniciar sesión')
