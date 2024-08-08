from datetime import datetime, timezone
from iescp import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
     return Sponsor.query.get(int(user_id))

class Sponsor(db.Model, UserMixin):
     id = db.Column(db.Integer, primary_key=True)
     username = db.Column(db.String(16), unique=True, nullable =False)
     email = db.Column(db.String(16), unique=True, nullable =False)
     profile_pic = db.Column(db.String(16), nullable =False, default='default.jpg')
     password = db.Column(db.String(60), nullable =False)
     posts = db.relationship('Post', backref='author',lazy=True)

     def __repr__(self):
          return f"User('{self.username}','{self.email}','{self.profile_pic}')"
     
class Post(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String(100), nullable =False)
     date_posted = db.Column(db.DateTime, nullable =False, default =datetime.now(timezone.utc))
     description = db.Column(db.Text, nullable =False)
     budget = db.Column(db.String(20), nullable =False)
     industry = db.Column(db.String(20), nullable =False)
     end_date = db.Column(db.String(20), nullable =False)
     user_id = db.Column(db.Integer,db.ForeignKey('sponsor.id'),nullable= False)

     def __repr__(self):
          return f"User('{self.title}','{self.date_posted}')"