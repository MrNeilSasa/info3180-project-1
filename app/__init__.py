from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_migrate import Migrate




app = Flask(__name__)
app.config['SECRET_KEY'] = "aef10f304d32e59c10840bd587dd42909ed1264ea03e5b0a8e41a74c668f95cb"  # Ideally you'd want this to be a much longer and more random string
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://project1:project1@localhost/project1'
app.config['UPLOAD_FOLDER'] = './uploads'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed

#app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views