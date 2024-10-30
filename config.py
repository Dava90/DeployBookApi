from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Initialize app and database connection
app = Flask(__name__)

# Konfigurasi MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://dbBookAPI_wheatfoxme:8b6cda738c342fd35f3641d530f4903b4fcb7f6a@lu74v.h.filess.io:3305/dbBookAPI_wheatfoxme'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.app_context().push()
