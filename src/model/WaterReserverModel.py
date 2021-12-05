from src import db, login_manager
# This UserMixing is used to integrate login_manager
from flask_login import UserMixin 
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20),  nullable=False, default = 'default.jpeg')
    password  = db.Column(db.String(60),  nullable=False)
   
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}' )"

# dam name can be mahi, kadana, panam
class Dam(db.Model):
    __tablename__ = 'dam'
    id = db.Column(db.Integer, primary_key=True)
    dam_name = db.Column(db.String(120), unique=True, nullable=False)
    active_flag =  db.Column(db.String(1),  nullable=False)
    demandData = db.relationship('DemandData')
    #storage = db.relationship('Storage')
    #inflow = db.relationship('Inflow')

    def __repr__(self):
        return f"Dam('{self.dam_name}', '{self.active_flag}' )"

#type can be irrigation, hydropower
class DemandType(db.Model):
    __tablename__ = 'demandType'
    id = db.Column(db.Integer, primary_key=True)
    type =  db.Column(db.String(20), unique=True, nullable=False)
    demandData = db.relationship('DemandData')
    def __repr__(self):
        return f"Dam('{self.type}' )"


class DemandData(db.Model):
    __tablename__ = 'demandData'
    id = db.Column(db.Integer, primary_key=True)
    demand_value =  db.Column(db.Numeric(10,3), nullable=False)
    dam_id =  db.Column(db.Integer, db.ForeignKey('dam.id'), nullable=False)
    demand_type_id = db.Column(db.Integer, db.ForeignKey('demandType.id'), nullable=False)
    demand_data_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"Dam('{self.demand_value}', '{self.demand_data_date}', '{self.dam_id}', '{self.demand_id}')"

class Storage(db.Model):
    __tablename__ = 'storage'
    id = db.Column(db.Integer, primary_key=True)
    dam_id =  db.Column(db.Integer, db.ForeignKey('dam.id'), nullable=False)
    storage_value = db.Column(db.Numeric(10,3), nullable=False)
    area_value = db.Column(db.Numeric(10,3), nullable=False)
    elevation_value = db.Column(db.Numeric(10,3), nullable=True)

    def __repr__(self):
        return f"Dam('{self.storage_value}', '{self.area_value}', '{self.elevation_value}' )"

class Inflow(db.Model):
    __tablename__ = 'inflow'
    id = db.Column(db.Integer, primary_key=True)
    dam_id =  db.Column(db.Integer, db.ForeignKey('dam.id'), nullable=False)
    four_near_future = db.Column(db.Numeric(10,3), nullable=True)
    eight_near_future = db.Column(db.Numeric(10,3), nullable=True)
    four_far_future = db.Column(db.Numeric(10,3), nullable=True)
    eight_far_future = db.Column(db.Numeric(10,3), nullable=True)
    inflow_data_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"Dam('{self.dam_id}','{self.inflow_data_date}', '{self.four_near_future}','{self.eight_near_future}','{self.four_far_future}', '{self.eight_far_future}' )"
