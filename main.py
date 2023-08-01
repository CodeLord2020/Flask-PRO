from flask import Flask, request, redirect, render_template
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy
from models import User, db

app = Flask(__name__)
app.config.from_object(DevConfig)
db.init_app(app)


@app.route('/echo/<name>', methods = ['GET', 'POST'])
def hello(name):
    if request== 'POST':
        name = request.form.get('age','')
        age = request.form.get('name','')     
        response = "Hey there {}! You said you are {} years old.".format(name, age)
    response = "Hey there {}! How RE U DOING?".format(name)
    return response

@app.route('/add_user', methods=['POST'])
def add_user():
    new_user = User(username=request.json['username'], department=request.json['department'], password=request.json['password'])
    db.session.add(new_user)
    db.session.commit()
    return 'User added successfully!', 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)