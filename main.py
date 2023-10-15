from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from DataBase.DataBase import *
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

client = app.test_client()

from Models.User.UserModel import *
Base.metadata.create_all(bind=engine)

jwt = JWTManager(app)

@app.route('/api/Account/SignUp', methods=['POST']) #Регистрация аккаунта
def register():
    params = request.json
    user = AccountModel(**params)
    db_session.add(user)
    db_session.commit()
    token = user.get_token()
    return {'access_token': token}

@app.route('/api/Account/SignIn', methods=['POST']) #Вход в аккаунт
def login():
    params = request.json
    user = AccountModel.authenticate(**params)
    token = user.get_token()
    return {'access_token': token}

@app.route('/api/Account/Me', methods=['GET'])
@jwt_required()
def getAccount():
    user_id = get_jwt_identity()
    account = AccountModel.query.filter(
        AccountModel.id == user_id
    ).all()
    serialized =[]
    for user in account:
        serialized.append({
            'id': user.id,
            'name': user.name,
            'password': user.password
        })
        return serialized

@app.route('/api/Account/Update', methods=['PUT'])
@jwt_required()
def updateAccount():
    user_id = get_jwt_identity()
    params = request.json
    item = AccountModel.query.filter(
        AccountModel.id == user_id
    ).first()
    for key, value in params.items():
        setattr(item, key, value)
    db_session.commit()
    serialized = {
        'id': item.id,
        'name': item.name,
        'password': item.password
    }
    return serialized

@app.route('/')
def index():
    return "Hello, World!"

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(debug=True)