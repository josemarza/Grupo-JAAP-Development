from flask import Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy

bp = Blueprint('model', __name__)
db = SQLAlchemy()

# Creamos la tabla de vendedor
class Vendedor(db.Model):
    __tablename__ = 'vendedor'
    vend_id = db.Column(db.Integer, primary_key=True)
    vend_ci = db.Column(db.String(10), nullable=False)
    vend_nombre_apellido = db.Column(db.String(80), nullable=False)
    vend_direccion = db.Column(db.String(120), nullable=False)
    vend_telefono = db.Column(db.String(15), nullable=False)
    vend_email = db.Column(db.String(50))
    
    @classmethod
    def create(cls, vend_ci, vend_nombre_apellido, vend_direccion, vend_telefono, vend_email):
        vendedor = Vendedor(vend_ci=vend_ci, vend_nombre_apellido=vend_nombre_apellido, vend_direccion=vend_direccion, vend_telefono=vend_telefono, vend_email=vend_email)
        return vendedor.save()
    
    def save(self):
        try:
            db.session.add(self) #Añadi  
            db.session.commit() #Guarda
            return self
        except Exception as e:
            print(e)
            return None
    
    def delete(self):
        try:    
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False
    
    def json(self):
        return {
            'id': self.id,
            "vend_ci" : self.vend_ci, 
            "vend_nombre_apellido" : self.vend_nombre_apellido, 
            "vend_direccion" : self.vend_direccion, 
            "vend_telefono" : self.vend_telefono, 
            "vend_email" : self.vend_email
                }
# Creamos la tabla de cliente titular
class ClienteTitular(db.Model):
    __tablename__ = 'cliente_titular'
    ct_id = db.Column(db.Integer, primary_key=True)
    ct_ci = db.Column(db.String(10), nullable=False)
    ct_nombre_apellido = db.Column(db.String(80), nullable=False)
    ct_direccion = db.Column(db.String(120), nullable=False)
    ct_telefono = db.Column(db.String(15), nullable=False)
    ct_email = db.Column(db.String(50))

    @classmethod
    def create(cls, ct_ci, ct_nombre_apellido, ct_direccion, ct_telefono, ct_email):
        cliente_titular = ClienteTitular(ct_ci=ct_ci, ct_nombre_apellido=ct_nombre_apellido, ct_direccion=ct_direccion, ct_telefono=ct_telefono, ct_email=ct_email)
        return cliente_titular.save()
    
    def save(self):
        try:
            db.session.add(self) #Añadi  
            db.session.commit() #Guarda
            return self
        except Exception as e:
            print(e)
            return None
    
    def delete(self):
        try:    
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False
    
    def json(self):
        return {
            'id': self.id,
            "ct_ci" : self.ct_ci, 
            "ct_nombre_apellido" : self.ct_nombre_apellido, 
            "ct_direccion" : self.ct_direccion, 
            "ct_telefono" : self.ct_telefono, 
            "ct_email" : self.ct_email
                }

class Codeudor(db.Model):
    __tablename__ = 'codeudor'
    cd_id = db.Column(db.Integer, primary_key=True)
    cd_ci = db.Column(db.String(10), nullable=False)
    cd_nombre_apellido = db.Column(db.String(80), nullable=False)
    cd_direccion = db.Column(db.String(120), nullable=False)
    cd_telefono = db.Column(db.String(15), nullable=False)
    cd_email = db.Column(db.String(50))

    @classmethod
    def create(cls, cd_ci, cd_nombre_apellido, cd_direccion, cd_telefono, cd_email):
        codeudor = Codeudor(cd_ci=cd_ci, cd_nombre_apellido=cd_nombre_apellido, cd_direccion=cd_direccion, cd_telefono=cd_telefono, cd_email=cd_email)
        return codeudor.save()
    
    def save(self):
        try:
            db.session.add(self) #Añadi  
            db.session.commit() #Guarda
            return self
        except Exception as e:
            print(e)
            return None
    
    def delete(self):
        try:    
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False
    
    def json(self):
        return {
            'id': self.id,
            "cd_ci" : self.cd_ci, 
            "cd_nombre_apellido" : self.cd_nombre_apellido, 
            "cd_direccion" : self.cd_direccion, 
            "cd_telefono" : self.cd_telefono, 
            "cd_email" : self.cd_email
                }

class Vehiculo(db.Model):
    __tablename__ = 'vehiculo'
    vehic_id = db.Column(db.Integer, primary_key=True)
    vehic_chasis = db.Column(db.String(17), nullable=False)
    vehic_marca = db.Column(db.String(20), nullable=False)
    vehic_modelo = db.Column(db.String(20), nullable=False)
    vehic_anho = db.Column(db.Integer, nullable=False)
    vehic_tipo = db.Column(db.String(20), nullable=False)
    vehic_color = db.Column(db.String(20))
    vehic_combustible = db.Column(db.String(20))
    vehic_kilometraje = db.Column(db.Integer)
    vehic_estado = db.Column(db.String(20))

    @classmethod
    def create(cls, vehic_chasis, vehic_marca, vehic_modelo, vehic_anho, vehic_tipo, vehic_color,vehic_combustible, vehic_kilometraje, vehic_estado):
        vehiculo = Vehiculo(vehic_chasis=vehic_chasis, vehic_marca=vehic_marca, vehic_modelo=vehic_modelo, vehic_anho=vehic_anho, vehic_tipo=vehic_tipo, vehic_color=vehic_color, vehic_combustible=vehic_combustible, vehic_kilometraje=vehic_kilometraje, vehic_estado=vehic_estado)
        return vehiculo.save()
    
    def save(self):
        try:
            db.session.add(self) #Añadi  
            db.session.commit() #Guarda
            return self
        except Exception as e:
            print(e)
            return None
    
    def delete(self):
        try:    
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False
    
    def json(self):
        return {
            'id': self.id,
            'vehic_chasis':self.vehic_chasis, 
            'vehic_marca':self.vehic_marca, 
            'vehic_modelo':self.vehic_modelo, 
            'vehic_anho':self.vehic_anho, 
            'vehic_tipo':self.vehic_tipo, 
            'vehic_color':self.vehic_color, 
            'vehic_combustible':self.vehic_combustible, 
            'vehic_kilometraje':self.vehic_kilometraje, 
            'vehic_estado':self.vehic_estado           
                }

class PlanDePago(db.Model):
    __tablename__ = 'plan_de_pago'
    plan_pago_id = db.Column(db.Integer, primary_key=True)
    plan_pago_cliente_01 = db.Column(db.String, db.ForeignKey('cliente_titular.ct_nombre_apellido', ondelete="CASCADE"))
    plan_pago_cliente_02 = db.Column(db.String, db.ForeignKey('cliente_titular.ct_nombre_apellido', ondelete="CASCADE"))
    plan_pago_codeudor_01 = db.Column(db.String, db.ForeignKey('codeudor.cd_nombre_apellido', ondelete="CASCADE"))
    plan_pago_codeudor_02 = db.Column(db.String, db.ForeignKey('codeudor.cd_nombre_apellido', ondelete="CASCADE"))
    plan_pago_codeudor_03 = db.Column(db.String, db.ForeignKey('codeudor.cd_nombre_apellido', ondelete="CASCADE"))
    plan_pago_entrega = db.Column(db.Integer, nullable=False)
    plan_pago_cant_cuotas = db.Column(db.Integer, nullable=False)
    plan_pago_monto_cuota = db.Column(db.Integer, nullable=False)
    plan_pago_cant_refuerzos = db.Column(db.Integer, nullable=False)
    plan_pago_monto_refuerzos = db.Column(db.Integer, nullable=False)
    plan_pago_id_vehic = db.Column(db.Integer, db.ForeignKey("vehiculo.vehic_id", ondelete="CASCADE"))

    @classmethod
    def create(cls, plan_pago_cliente_01, plan_pago_cliente_02, plan_pago_codeudor_01, plan_pago_codeudor_02, plan_pago_codeudor_03,  plan_pago_entrega, plan_pago_cant_cuotas, plan_pago_monto_cuota, plan_pago_cant_refuerzos, plan_pago_monto_refuerzos, plan_pago_id_vehic):
        plan_de_pago = PlanDePago(plan_pago_cliente_01 = plan_pago_cliente_01, plan_pago_cliente_02 = plan_pago_cliente_02, plan_pago_codeudor_01 = plan_pago_codeudor_01, plan_pago_codeudor_02 = plan_pago_codeudor_02, plan_pago_codeudor_03 = plan_pago_codeudor_03, plan_pago_entrega = plan_pago_entrega, plan_pago_cant_cuotas = plan_pago_cant_cuotas, plan_pago_monto_cuota = plan_pago_monto_cuota, plan_pago_cant_refuerzos = plan_pago_cant_refuerzos, plan_pago_monto_refuerzos = plan_pago_monto_refuerzos, plan_pago_id_vehic = plan_pago_id_vehic)
        return plan_de_pago.save()
    
    def save(self):
        try:
            db.session.add(self) #Añadi  
            db.session.commit() #Guarda
            return self
        except Exception as e:
            print(e)
            return None
    
    def delete(self):
        try:    
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False
    
    def json(self):
        return {
            'id': self.id,
            'plan_pago_cliente_01' : self.plan_pago_cliente_01,
            'plan_pago_cliente_02' : self.plan_pago_cliente_02,
            'plan_pago_codeudor_01' : self.plan_pago_codeudor_01,
            'plan_pago_codeudor_02' : self.plan_pago_codeudor_02,
            'plan_pago_codeudor_03' : self.plan_pago_codeudor_03,
            'plan_pago_entrega' : self.plan_pago_entrega, 
            'plan_pago_cant_cuotas' : self.plan_pago_cant_cuotas, 
            'plan_pago_monto_cuota' : self.plan_pago_monto_cuota, 
            'plan_pago_cant_refuerzos' : self.plan_pago_cant_refuerzos, 
            'plan_pago_monto_refuerzos' : self.plan_pago_monto_refuerzos, 
            'plan_pago_id_vehic' : self.plan_pago_id_vehic                
            }




