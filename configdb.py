from owlmap import db

db.create_all()

from owlmap.models import User

admin = User(exp=000000, email='admin@owlmap.com', password='admin123', nombres='John', apellidos='Doe')

db.session.add(admin)
db.session.commit()
