from app.extensions import db

class Person(db.Model):
    __tablename__='people'
    person_id=db.Column(db.Integer, primary_key=True)
    person_name=db.Column(db.String, nullable=False)