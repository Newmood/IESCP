from datetime import datetime, timezone
from iescp import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
     return CommonUser.query.get(int(user_id))

class CommonUser(db.Model,UserMixin):
     __tablename__ = 'commonuser'
     id = db.Column(db.Integer, primary_key=True)
     role = db.Column(db.String(25), nullable=False) # sponsor or creator
     username = db.Column(db.String(16), unique=True, nullable =False)    
     password = db.Column(db.String(60), nullable =False)
     email = db.Column(db.String(50), unique=True, nullable =False)
     firstname = db.Column(db.String(50), nullable=False)
     lastname = db.Column(db.String(50), nullable=False)
     profile_pic = db.Column(db.String(16), nullable =False, default='default.jpg')
     status = db.Column(db.String(12), nullable= False, default='Public') #public or private profile for browse page
     flag = db.Column(db.String(5), nullable=False, default='No') # flag for admin
     phone_no = db.Column(db.String(16), nullable = False)
     

     def __repr__(self):
          return f"User('{self.id}','{self.role}','{self.status}')"


class Sponsor(db.Model, UserMixin):
     __tablename__ = 'sponsor'
     id = db.Column(db.Integer, primary_key=True)
     company = db.Column(db.String(50), nullable = False)
     industry = db.Column(db.String(50), nullable=False)
     website= db.Column(db.String(120), nullable=False)
     company_address = db.Column(db.Text, nullable=False)
     common_id = db.Column(db.Integer, db.ForeignKey('commonuser.id'), nullable = False)
     common_user = db.relationship('CommonUser', backref='sponsor', uselist=False)

     def __repr__(self):
          return f"User('{self.common_id}')"
     

class Creator(db.Model, UserMixin):
     __tablename__ = 'creator'
     id = db.Column(db.Integer, primary_key=True)
     social_link_1 = db.Column(db.String(120), nullable=False)
     social_link_2 = db.Column(db.String(120))
     social_link_3 = db.Column(db.String(120))
     category = db.Column(db.String(50), nullable= False)
     location= db.Column(db.String(100), nullable= False)
     dob = db.Column(db.DateTime, nullable=False)
     bio = db.Column(db.Text, nullable= False)
     common_id = db.Column(db.Integer, db.ForeignKey('commonuser.id'), nullable = False)
     common_user = db.relationship('CommonUser', backref='creator', uselist=False)

     def __repr__(self):
          return f"User('{self.common_id}')"
     
class Post(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String(100), nullable =False)
     date_posted = db.Column(db.DateTime, nullable =False, default =datetime.now(timezone.utc))
     description = db.Column(db.Text, nullable =False)
     budget = db.Column(db.String(20), nullable =False)
     industry = db.Column(db.String(20), nullable =False)
     end_date = db.Column(db.DateTime, nullable =False)
     user_id = db.Column(db.Integer,db.ForeignKey('sponsor.id'),nullable= False)
     status = db.Column(db.String(20), nullable=False, default='Public')
     author = db.relationship('Sponsor', backref='posts', lazy=True)

     def __repr__(self):
          return f"User('{self.title}','{self.date_posted}')"


class AdRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey('commonuser.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('commonuser.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    budget = db.Column(db.String(20), nullable=False)
    expected_completion_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending')  # pending, accepted, rejected

    post = db.relationship('Post', backref='ad_requests')
    sender = db.relationship('CommonUser', foreign_keys=[sender_id], backref='sent_ad_requests')
    receiver = db.relationship('CommonUser', foreign_keys=[receiver_id], backref='received_ad_requests')
