from flask import Flask
from app.model import db, Vendedor, ClienteTitular, Codeudor, Vehiculo, PlanDePago
from app.config import config

def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(environment)
    with app.app_context():
        db.init_app(app)
        db.create_all()
    from app.controller import (main)
    app.register_blueprint(main.bp)
    return app

environment = config['development']

app = create_app(environment)



