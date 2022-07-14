from flask import Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy

bp = Blueprint('model', __name__)
db = SQLAlchemy()

# Creamos la tabla de vendedor 01
class Vendedor01(db.Model):
    __tablename__ = 'vendedor_01'
    vend1_id = db.Column(db.Integer, primary_key=True)
    vend1_ci = db.Column(db.String(10), nullable=False)
    vend1_nombre_apellido = db.Column(db.String(80), nullable=False)
    vend1_direccion = db.Column(db.String(120), nullable=False)
    vend1_telefono = db.Column(db.String(15), nullable=False)
    vend1_email = db.Column(db.String(50))
    
    @classmethod
    def create(cls, vend1_ci, vend1_nombre_apellido, vend1_direccion, vend1_telefono, vend1_email):
        vendedor1 = Vendedor01(vend1_ci=vend1_ci, vend1_nombre_apellido=vend1_nombre_apellido, vend1_direccion=vend1_direccion, vend1_telefono=vend1_telefono, vend1_email=vend1_email)
        return vendedor1.save()
    
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
            "vend1_ci" : self.vend1_ci, 
            "vend1_nombre_apellido" : self.vend1_nombre_apellido, 
            "vend1_direccion" : self.vend1_direccion, 
            "vend1_telefono" : self.vend1_telefono, 
            "vend1_email" : self.vend1_email
                }

# Creamos la tabla de vendedor 02
class Vendedor02(db.Model):
    __tablename__ = 'vendedor_02'
    vend2_id = db.Column(db.Integer, primary_key=True)
    vend2_ci = db.Column(db.String(10), nullable=False)
    vend2_nombre_apellido = db.Column(db.String(80), nullable=False)
    vend2_direccion = db.Column(db.String(120), nullable=False)
    vend2_telefono = db.Column(db.String(15), nullable=False)
    vend2_email = db.Column(db.String(50))
  
    @classmethod
    def create(cls, vend2_ci, vend2_nombre_apellido, vend2_direccion, vend2_telefono, vend2_email):
        vendedor2 = Vendedor02(vend2_ci=vend2_ci, vend2_nombre_apellido=vend2_nombre_apellido, vend2_direccion=vend2_direccion, vend2_telefono=vend2_telefono, vend2_email=vend2_email)
        return vendedor2.save()
    
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
            "vend2_ci" : self.vend2_ci, 
            "vend2_nombre_apellido" : self.vend2_nombre_apellido, 
            "vend2_direccion" : self.vend2_direccion, 
            "vend2_telefono" : self.vend2_telefono, 
            "vend2_email" : self.vend2_email
                }

# Creamos la tabla de cliente titular 01
class ClienteTitular01(db.Model):
    __tablename__ = 'cliente_titular_01'
    ct1_id = db.Column(db.Integer, primary_key=True)
    ct1_ci = db.Column(db.String(10), nullable=False)
    ct1_nombre_apellido = db.Column(db.String(80), nullable=False)
    ct1_direccion = db.Column(db.String(120), nullable=False)
    ct1_telefono = db.Column(db.String(15), nullable=False)
    ct1_email = db.Column(db.String(50))

    @classmethod
    def create(cls, ct1_ci, ct1_nombre_apellido, ct1_direccion, ct1_telefono, ct1_email):
        cliente_titular_01 = ClienteTitular01(ct1_ci=ct1_ci, ct1_nombre_apellido=ct1_nombre_apellido, ct1_direccion=ct1_direccion, ct1_telefono=ct1_telefono, ct1_email=ct1_email)
        return cliente_titular_01.save()
    
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
            "ct1_ci" : self.ct1_ci, 
            "ct1_nombre_apellido" : self.ct1_nombre_apellido, 
            "ct1_direccion" : self.ct1_direccion, 
            "ct1_telefono" : self.ct1_telefono, 
            "ct1_email" : self.ct1_email
                }

class ClienteTitular02(db.Model):
    __tablename__ = 'cliente_titular_02'
    ct2_id = db.Column(db.Integer, primary_key=True)
    ct2_ci = db.Column(db.String(10), nullable=False)
    ct2_nombre_apellido = db.Column(db.String(80), nullable=False)
    ct2_direccion = db.Column(db.String(120), nullable=False)
    ct2_telefono = db.Column(db.String(15), nullable=False)
    ct2_email = db.Column(db.String(50))

    @classmethod
    def create(cls, ct2_ci, ct2_nombre_apellido, ct2_direccion, ct2_telefono, ct2_email):
        cliente_titular_02 = ClienteTitular02(ct2_ci=ct2_ci, ct2_nombre_apellido=ct2_nombre_apellido, ct2_direccion=ct2_direccion, ct2_telefono=ct2_telefono, ct2_email=ct2_email)
        return cliente_titular_02.save()
    
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
            "ct2_ci" : self.ct2_ci, 
            "ct2_nombre_apellido" : self.ct2_nombre_apellido, 
            "ct2_direccion" : self.ct2_direccion, 
            "ct2_telefono" : self.ct2_telefono, 
            "ct2_email" : self.ct2_email
                }

class Codeudor01(db.Model):
    __tablename__ = 'codeudor_01'
    cd1_id = db.Column(db.Integer, primary_key=True)
    cd1_ci = db.Column(db.String(10), nullable=False)
    cd1_nombre_apellido = db.Column(db.String(80), nullable=False)
    cd1_direccion = db.Column(db.String(120), nullable=False)
    cd1_telefono = db.Column(db.String(15), nullable=False)
    cd1_email = db.Column(db.String(50))

    @classmethod
    def create(cls, cd1_ci, cd1_nombre_apellido, cd1_direccion, cd1_telefono, cd1_email):
        codeudor_01 = Codeudor01(cd1_ci=cd1_ci, cd1_nombre_apellido=cd1_nombre_apellido, cd1_direccion=cd1_direccion, cd1_telefono=cd1_telefono, cd1_email=cd1_email)
        return codeudor_01.save()
    
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
            "cd1_ci" : self.cd1_ci, 
            "cd1_nombre_apellido" : self.cd1_nombre_apellido, 
            "cd1_direccion" : self.cd1_direccion, 
            "cd1_telefono" : self.cd1_telefono, 
            "cd1_email" : self.cd1_email
                }

class Codeudor02(db.Model):
    __tablename__ = 'codeudor_02'
    cd2_id = db.Column(db.Integer, primary_key=True)
    cd2_ci = db.Column(db.String(10), nullable=False)
    cd2_nombre_apellido = db.Column(db.String(80), nullable=False)
    cd2_direccion = db.Column(db.String(120), nullable=False)
    cd2_telefono = db.Column(db.String(15), nullable=False)
    cd2_email = db.Column(db.String(50))


    @classmethod
    def create(cls, cd2_ci, cd2_nombre_apellido, cd2_direccion, cd2_telefono, cd2_email):
        codeudor_02 = Codeudor02(cd2_ci=cd2_ci, cd2_nombre_apellido=cd2_nombre_apellido, cd2_direccion=cd2_direccion, cd2_telefono=cd2_telefono, cd2_email=cd2_email)
        return codeudor_02.save()
    
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
            "cd2_ci" : self.cd2_ci, 
            "cd2_nombre_apellido" : self.cd2_nombre_apellido, 
            "cd2_direccion" : self.cd2_direccion, 
            "cd2_telefono" : self.cd2_telefono, 
            "cd2_email" : self.cd2_email
                }

class Codeudor03(db.Model):
    __tablename__ = 'codeudor_03'
    cd3_id = db.Column(db.Integer, primary_key=True)
    cd3_ci = db.Column(db.String(10), nullable=False)
    cd3_nombre_apellido = db.Column(db.String(80), nullable=False)
    cd3_direccion = db.Column(db.String(120), nullable=False)
    cd3_telefono = db.Column(db.String(15), nullable=False)
    cd3_email = db.Column(db.String(50))

    @classmethod
    def create(cls, cd3_ci, cd3_nombre_apellido, cd3_direccion, cd3_telefono, cd3_email):
        codeudor_03 = Codeudor03(cd3_ci=cd3_ci, cd3_nombre_apellido=cd3_nombre_apellido, cd3_direccion=cd3_direccion, cd3_telefono=cd3_telefono, cd3_email=cd3_email)
        return codeudor_03.save()
    
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
            "cd3_ci" : self.cd3_ci, 
            "cd3_nombre_apellido" : self.cd3_nombre_apellido, 
            "cd3_direccion" : self.cd3_direccion, 
            "cd3_telefono" : self.cd3_telefono, 
            "cd3_email" : self.cd3_email
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
            'vehic_chasis':vehic_chasis, 
            'vehic_marca':vehic_marca, 
            'vehic_modelo':vehic_modelo, 
            'vehic_anho':vehic_anho, 
            'vehic_tipo':vehic_tipo, 
            'vehic_color':vehic_color, 
            'vehic_combustible':vehic_combustible, 
            'vehic_kilometraje':vehic_kilometraje, 
            'vehic_estado':vehic_estado           
                }

class PlanDePago(db.Model):
    __tablename__ = 'plan_de_pago'
    plan_pago_id = db.Column(db.Integer, primary_key=True)
    plan_pago_entrega = db.Column(db.Integer, nullable=False)
    plan_pago_cant_cuotas = db.Column(db.Integer, nullable=False)
    plan_pago_monto_cuota = db.Column(db.Integer, nullable=False)
    plan_pago_cant_refuerzos = db.Column(db.Integer, nullable=False)
    plan_pago_monto_refuerzos = db.Column(db.Integer, nullable=False)
    plan_pago_id_vehic = db.Column(db.Integer, db.ForeignKey("vehiculo.vehic_id", ondelete="CASCADE"))

    @classmethod
    def create(cls, plan_pago_entrega, plan_pago_cant_cuotas, plan_pago_monto_cuota, plan_pago_cant_refuerzos, plan_pago_monto_refuerzos, plan_pago_id_vehic):
        plan_de_pago = PlanDePago(plan_pago_entrega = plan_pago_entrega, plan_pago_cant_cuotas = plan_pago_cant_cuotas, plan_pago_monto_cuota = plan_pago_monto_cuota, plan_pago_cant_refuerzos = plan_pago_cant_refuerzos, plan_pago_monto_refuerzos = plan_pago_monto_refuerzos, plan_pago_id_vehic = plan_pago_id_vehic)
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
            'plan_pago_entrega' : plan_pago_entrega, 
            'plan_pago_cant_cuotas' : plan_pago_cant_cuotas, 
            'plan_pago_monto_cuota' : plan_pago_monto_cuota, 
            'plan_pago_cant_refuerzos' : plan_pago_cant_refuerzos, 
            'plan_pago_monto_refuerzos' : plan_pago_monto_refuerzos, 
            'plan_pago_id_vehic' : plan_pago_id_vehic                
            }




