from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c233aca78b9bef9f68a9c2f3a4ae7d72'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    exp = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    nombres = db.Column(db.String(60), nullable=False)
    apellidos = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.exp}', '{self.email}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_exp = db.Column(db.Integer, db.ForeignKey('user.exp'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


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

if __name__ == '__main__':
    app.run(debug=True)
