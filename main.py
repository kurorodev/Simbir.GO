from flask import Flask
from DataBase.DataBase import *

app = Flask(__name__)

from Models.User.UserModel import *
Base.metadata.create_all(bind=engine)

@app.route('/')
def index():
    return "Hello, World!"

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(debug=True)