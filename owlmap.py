from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'autor' : 'Raúl Octavio Murcia Yocupicio',
        'titulo' : 'El primer post',
        'contenido' : 'Hola compañeros este es el primer post del blog jaja salu2.',
        'fecha' : '3 de Abril de 2019'
    },
    {
        'autor' : 'Raúlito Pérez',
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

@app.route("/login")
def login():
    return render_template('login.html', title='Iniciar Sesión')

@app.route("/forum")
def forum():
    return render_template('forum.html', title='Foro', name='Raúl y XI=imena', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
