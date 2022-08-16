from ast import Delete
from flask import Flask,request
from flask_restful import Resource,Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)  #instantiate api for app

# app.route('/hello')
# def hello():
#     return ' Hello World'
# app.config['SQLALCHEMY_DATABSE_URI'] = 'postgresql://postgres:postgres@localhost/postgres'  #path and name of the database
app.config['SQLAlchemy_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/postgres'  #path and name of the database

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):   #returns the string value
        return self.name


<h1> This is the header </h1>

fakeDatabase = {
    1:{'name': 'Clean car'},
    2:{'name':'Write blog'},
    3:{'name': 'Start stream'}
}

class Items(Resource):
    def get(self):
        tasks = Task.queryall()
        return fakeDatabase #to get all the values

    def post(self):   #adding the item in the database
        data = request.json
        task = Task(name=data['name'])
        db.session.add(task)
        db.session.commit()
        tasks = Task.queryall()
        return tasks

        # itemId= len(fakeDatabase.keys()) + 1
        # fakeDatabase[itemId] = {'name': data['name']}
        # return fakeDatabase

class Item(Resource):
    def get(self,pk):
        task = Task.query.filter_by(id=pk)
        return fakeDatabase[pk] #to get single values 127.0.0.1/5000/1

    def put (self,pk): # To pdate the database
        data = request.json
        fakeDatabase[pk]['name']= data['name']
        return fakeDatabase

    def delete(self,pk):
        del fakeDatabase[pk]
        return fakeDatabase


api.add_resource(Items,'/')
api.add_resource(Item,'/<int:pk>')


if __name__ == '__main__':
    app.run(debug= True )
db.create_all()
