from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Initialize app and database connection
app = Flask(__name__)

# Konfigurasi MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://dav:dav@localhost:3306/0692_db_MVC'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.app_context().push()