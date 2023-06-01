from flask import Flask
from routes.contacts import contacts
from utils.db import db

app = Flask(__name__)
app.secret_key = "secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost:3306/flask_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(contacts)
