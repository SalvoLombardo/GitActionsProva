from flask import Blueprint,render_template
from app.extensions import db
from app.models import Person
from app.schema_ma import person_schema


main_bp= Blueprint('main_bp', __name__)

@main_bp.get('/')
def main():
    person=Person.query.first()


    if person:
        return person_schema.jsonify(person)
    else:
        return (f'Hello moto')

@main_bp.get('/second')
def second():
    second_person_id=2
    person2=Person.query.filter(Person.person_id==second_person_id).first()


    if person2:
        return person_schema.jsonify(person2)
    else:
        return (f'Hello moto')



    