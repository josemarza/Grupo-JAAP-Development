from flask import Blueprint, render_template, request
from datetime import datetime
from app.model import Vehiculo, ClienteTitular, Codeudor

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

# Direccionar al formulario de vehiculos

@bp.route('/nuevovehiculo')
def nuevovehiculo():
    return render_template('nuevovehiculo.html')

@bp.route('/api/nuevovehiculo',methods=['POST'])
def apinuevovehiculo():
    datos_vehiculo=request.form
    print(datos_vehiculo)
    fecha_actual=datetime.now()
    
    carga_de_vehiculo = Vehiculo.create(
        vehic_chasis=datos_vehiculo['vehic_chasis'], vehic_marca=datos_vehiculo['vehic_marca'], vehic_modelo=datos_vehiculo['vehic_modelo'], vehic_anho=datos_vehiculo['vehic_anho'], vehic_tipo=datos_vehiculo['vehic_tipo'], vehic_color=datos_vehiculo['vehic_color'], vehic_combustible=datos_vehiculo['vehic_combustible'], vehic_kilometraje=datos_vehiculo['vehic_kilometraje'], vehic_estado=datos_vehiculo['vehic_estado'])
    return render_template("nuevovehiculo.html")



# Direccionar al formulario de nuevo cliente
@bp.route('/nuevocliente')
def nuevocliente():
    return render_template('nuevocliente.html')

@bp.route('/api/nuevocliente',methods=['POST'])
def apinuevocliente():
    nuevo_cliente=request.form
    print(nuevo_cliente)
    fecha_actual=datetime.now()
    
    carga_de_nuevo_cliente = ClienteTitular.create(
        ct_ci=nuevo_cliente['ct_ci'], ct_nombre_apellido=nuevo_cliente['ct_nombre_apellido'], ct_direccion=nuevo_cliente['ct_direccion'], ct_telefono=nuevo_cliente['ct_telefono'], ct_email=nuevo_cliente['ct_email'])
    return render_template("nuevocliente.html")


# Direccionar al formulario de nuevo codeudor
@bp.route('/nuevocodeudor')
def nuevocodeudor():
    return render_template('nuevocodeudor.html')

@bp.route('/api/nuevocodeudor',methods=['POST'])
def apinuevocodeudor():
    nuevo_codeudor=request.form
    print(nuevo_codeudor)
    fecha_actual=datetime.now()
    
    carga_de_nuevo_codeudor = Codeudor.create(
        cd_ci=nuevo_codeudor['cd_ci'], cd_nombre_apellido=nuevo_codeudor['cd_nombre_apellido'], cd_direccion=nuevo_codeudor['cd_direccion'], cd_telefono=nuevo_codeudor['cd_telefono'], cd_email=nuevo_codeudor['cd_email'])
    return render_template("nuevocodeudor.html")

