
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import DATE,BIGINT,BOOLEAN,JSON
from flask import Flask
# from sqlalchemy.sql import text
# from datetime import datetime

app = Flask(__name__)
app.debug = True

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/postgres'

db = SQLAlchemy(app)  #conecting db with python


class MasterCustomer(db.Model):
    __tablename__='master_customer'
    customer_id = db.Column(db.String,
                 nullable=False,
                 primary_key=True)
    # created_at = db.Column(db.DateTime, default=datetime.now)
    # updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    marital_status = db.Column(db.String,nullable=False)
    father_name = db.Column(db.String,nullable=False)
    mother_name = db.Column(db.String,nullable=False)

    # pan_number = db.Column(db.String(),nullable=False)
    # is_adhar_verified = db.Column(BOOLEAN,nullable=False)
    # is_pan_verfied = db.Column(BOOLEAN,nullable=False)
    # adhar_verified_date = db.Column(db.DateTime,default=datetime.now)
    # pan_verified_date = db.Column(db.DateTime,default=datetime.now)
    # customer_name = db.Column(db.String(),nullable=False)
    # marital_status = db.Column(db.String(),nullable=False)
    # spouse_name = db.Column(db.String(),nullable=False)
    # father_name = db.Column(db.String(),nullable=False)
    # mother_name = db.Column(db.String(),nullable=False)

    def __init__(self,customer_id,marital_status,father_name,mother_name):
            self.customer_id = customer_id
            # self.phone_number=phone_number
            # self.adhar_number = adhar_number
            # self.pan_number = pan_number
            # self.is_adhar_verified = is_adhar_verified
            # self.is_pan_verfied = is_pan_verfied
            # self.adhar_verified_date=adhar_verified_date
            # self.pan_verified_date = pan_verified_date
            # self.customer_name = customer_name
            self.marital_status = marital_status
            # self.spouse_name = spouse_name
            self.father_name = father_name
            self.mother_name = mother_name

# class MasterCustomerAddress(db.Model):
#     __tablename__='master_customer_address'
#     customer_id = db.Column(db.String,ForeignKey('master_customer.customer_id'),
#                  nullable=False,
#                  primary_key=True,
#                  server_default=text('uuid_generate_v4()'))
#     created_at = db.Column(db.DateTime, default=datetime.now)
#     updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

#     address = db.Column(JSON,nullable=False)
#     address_type =  db.Column(db.String(),nullable=False)
#     city = db.Column(db.String(),nullable=False)

#     def __init__(self,customer_id,address,address_type,city):
#          self.customer_id=customer_id
#          self.address=address
#          self.address_type=address_type
#          self.city = city

db.create_all()