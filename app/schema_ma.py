from app.extensions import ma
from app.models import Person
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance=True

person_schema=PersonSchema()