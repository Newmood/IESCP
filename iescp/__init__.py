from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)



app.config['SECRET_KEY'] = '7cf5fbfb549d204db232cebd4500fdb3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from iescp import routes