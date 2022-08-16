import json

from flask import Flask,  request,jsonify
from flask_restful import  Api, Resource
from db import db,MasterCustomer
from flask_sqlalchemy import SQLAlchemy

# value = 'postgresql://postgres:postgres@localhost:5432/arda'
 
# model = create_engine(value)
app = Flask(__name__)
# # function to add profiles
api = Api(app)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy()
db.init_app(app)
# db.init_app(app)  
# db.session.commit()
class PersonalDetail(Resource):

    def post(self):
        try:
            print("in")
            data = request.get_json()
            print(data)
            customer_id = data['customer_id']
   
            marital_status = data['marital_status']
            
            father_name = data['father_name']
            mother_name = data['mother_name']
            print(marital_status)
            Master_Customer = MasterCustomer(customer_id,
           marital_status,father_name,mother_name)
            print(Master_Customer)
            
            db.session.add(Master_Customer)
            print("inin")
            db.session.commit()
            print("out")
            print(Master_Customer.customer_id)
            
            return jsonify({"status":"OK","message":"value added"},200)
        except Exception as e:
            print(e)
            return jsonify({"status":"Error","message":"ERROR"},400)

   

# class AdharDetail(Resource):

#     def post(self):
#         try:
#             data = request.get_json()
            
#             # aadharnor = data['aadharnor']
#             # address = data['address']
#             # dateofbirth = data['dateofbirth']
#             # name = data['name']
#             # gender = data['gender']
#             # phone = data['phone']

           
            
#             p = MasterCustomerAddress(customer_id =data['customer_id'],address=data['address'],
#             address_type = data['address_type'],
#             city = data['city'])
#             print(p)
            
#             db.session.add(p)
#             print("commit")
#             db.session.commit()
#             print("s\a")
#             return jsonify({"status":"OK","message":"value added"},200)
#         except Exception as e:
#             return jsonify({"status":"ERROR","message":"ERROR"},400)


# class AutoFill(Resource):
#     def post(self):
#         try:
#             data = request.json()
#             customer_id = data['customer_id']
#             check_Adhar = model.execute('select is_adhar_verified from master_customer where customer_id = %s; ',(customer_id)).fetchall()
#             print(check_Adhar)
#             return True 
#             # check_adhar = model.execute('select * from aadharinfo where adhar_id = %s;', (id)).fetchall()
#             # print(check_adhar)
#             # if check_adhar == []:
#             #     value = model.execute('select * from personal_details_aadhar  where  id=%s;', (id)).fetchall()
#             #     print(value[0][1], type(value))
#             #     print("CJSGHJSGCHJ")
#             #     value = value[0]
#             #     res = dict(zip(value.keys(), value.values()))
#             #     print(res,"personal end")
#             #     personal_value = {"id": res['id'], "marital_status": res['marital_status'],
#             #      "spouse_name": res['spouse_name'],
#             #                       "father_name": res['father_name'], "mother_name": res['mother_name']}
#             #     print(personal_value,type(personal_value))
#             #     print(json.dumps(personal_value),type(json.dumps(personal_value)))
                
#             #     return jsonify({"status": "OK", "message": "success", "id": res['id'], 
#             #     "data": personal_value})
#             # else:
#             #     print("in", id)
#             #     data = model.execute(
#             #         'select * from aadharinfo ai,personal_details_aadhar pda where ai.adhar_id= pda.id AND id=%s;',
#             #         (id))
#             #     print("after query")
#             #     data = data.fetchall()
#             #     print("Data:",data)
#             #     j = data[0]
#             #     res = dict(zip(j.keys(), j.values()))
#             #     address = res['address']
#             #     print(address['careof'])
#             #     address = address['house'],address['street'],address['landmark'],address['district'],address['state'],address['pin']
#             #     address = " ".join(address)
#             #     print(" ".join(address))
#             #     print(res['address'])
#             #     print(str(res['dateofbirth']),type(res["dateofbirth"]))
#             #     print(data[0])
#             #     print(type(data[0]))
#             #     age = age = (pd.to_datetime('today').year-pd.to_datetime(res['dateofbirth']).year)
#             #     print(age)
#             #     data_value = {"aadharnor":res['aadharnor'],"address":address,"dateofbirth":str(res['dateofbirth']),
#             #     "father_name":res['father_name'],"gender":res['gender'],"age":age,
#             #     "marital_status":res['marital_status'],"mother_name":res['mother_name'],
#             #     "name":res['name'],"phone":res['phone'],"spouse_name":res['spouse_name']}
#             #     return jsonify({"status": "OK", "message": "success", "id": res['id'],"data":data_value})

#         except Exception as e:
#             print(e)
#             #return jsonify({"status": "ERROR", "message": "Failure", "data": "ID not found"})

    


api.add_resource(PersonalDetail, '/personal-detail')

# # api.add_resource(AadharVerify, "/verify")

# # api.add_resource(Profile_detail, '/add')
# api.add_resource(AdharDetail, '/adhar-detail')
# # api.add_resource(Profile_detail, '/add')
# api.add_resource(PersonalDetail, '/personal-detail')


if __name__ == '__main__':  #python interpreter assigns "__main__" to the file you run
    app.run(debug=True, port=6000)








