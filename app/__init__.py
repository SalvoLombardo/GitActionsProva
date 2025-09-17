from flask import Flask
from app.extensions import db, migrate, ma
from app.routes.routes import main_bp

import os
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app=Flask(__name__)

    
    

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    db.init_app(app)
    migrate.init_app(app,db)
    ma.init_app(app)

    app.register_blueprint(main_bp)



    return app

