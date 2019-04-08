from owlmap import app

if __name__ == '__main__':
    app.run(debug=True)

#Añadir parámetro host='0.0.0.0' para correr servidor en red local
#Añadir parámetro ssl_context='adhoc' para correr mediante protocolo https
## (Es necesario hacer 'pip install pyopenssl')
