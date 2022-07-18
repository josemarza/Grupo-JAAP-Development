from flask import Blueprint, render_template, request
from datetime import datetime
from app.model import Vehiculo

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/nuevovehiculo')
def nuevovehiculo():
    return render_template('nuevovehiculo.html')

@bp.route('/nuevovehiculo2')
def nuevovehiculo2():
    return render_template('nuevovehiculo2.html')

@bp.route('/api/nuevovehiculo',methods=['POST'])
def apinuevovehiculo():
    datos_vehiculo=request.form
    print(datos_vehiculo)
    fecha_actual=datetime.now()
    
    carga_de_vehiculo = Vehiculo.create(
        vehic_chasis=datos_vehiculo['vehic_chasis'], vehic_marca=datos_vehiculo['vehic_marca'], vehic_modelo=datos_vehiculo['vehic_modelo'], vehic_anho=datos_vehiculo['vehic_anho'], vehic_tipo=datos_vehiculo['vehic_tipo'], vehic_color=datos_vehiculo['vehic_color'], vehic_combustible=datos_vehiculo['vehic_combustible'], vehic_kilometraje=datos_vehiculo['vehic_kilometraje'], vehic_estado=datos_vehiculo['vehic_estado'])
    return render_template("nuevovehiculo.html")
