from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField, FileField, DateField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo, URL, Optional
from wtforms_alchemy import PhoneNumberField
from iescp.models import *

class LoginForm(FlaskForm):
    email = StringField("Enter your email", validators=[DataRequired(), Email()])
    password = PasswordField("Enter your password", validators=[DataRequired(), Length(min=8)])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")

class CreatorRegistrationForm(FlaskForm):
    # basic
    firstname = StringField("First name", validators=[DataRequired()])
    lastname = StringField("Last name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired(),Length(min=4,max=16)]) 
    email = StringField("Enter your email", validators=[DataRequired(), Email()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])
    # links 
    social_1 = StringField('Social media link 1', validators=[DataRequired(), URL()])
    social_2 = StringField('Social media link 2', validators=[Optional() ,URL()])
    social_3 = StringField('Social media link 3', validators=[Optional() , URL()])
    # more info
    profile_pic = FileField("Profile Picture")
    category = SelectField("Category", choices=[('Technology',"Technology"),('Fitness','Fitness'),('Fashion','Fashion'),('Beauty','Beauty'),('Gaming','Gaming'),('Educational','Educational'),('Travel','Travel'),('Other','Other')], validators=[DataRequired()])
    biodata = TextAreaField("Bio/Description", validators=[DataRequired(), Length(max=500)])
    location = StringField("Location", validators=[DataRequired(), Length(max=50)])
    date_of_birth = DateField("Date of Birth", format='%Y-%m-%d', validators=[DataRequired()])
    # set password
    password = PasswordField("Enter your password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Register')

    def validate_username(self,username):
        user = CommonUser.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username not available, please choose another.')
    
    def validate_email(self,email):
        user = CommonUser.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Account with this email aready exists. Want to log in instead?')

class SponsorRegistrationForm(FlaskForm):
    # basic
    firstname = StringField("First name", validators=[DataRequired()])
    lastname = StringField("Last name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired(),Length(min=4,max=16)]) 
    email = StringField("Enter your email", validators=[DataRequired(), Email()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])
    # company info
    profile_pic = FileField("Profile Picture")
    company_name = StringField("Company/ Individual Name", validators=[DataRequired(), Length(min=4,max=50)])
    industry = StringField("Industry", validators=[DataRequired(), Length(min=4,max=50)])
    website = StringField("Website",validators=[URL()])
    company_address = TextAreaField("Company Address",validators=[DataRequired(),Length(min=15,max=100)])
    # set password
    password = PasswordField("Enter your password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Register')

    def validate_username(self,username):
        user = CommonUser.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username not available, please choose another.')
    
    def validate_email(self,email):
        user = CommonUser.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Account with this email aready exists. Want to log in instead?')

    
class UpdateAccountCreator(FlaskForm):
    username = StringField("Username", validators=[DataRequired(),Length(min=4,max=16)]) 
    # links 
    social_1 = StringField('Social media link 1', validators=[DataRequired(), URL()])
    social_2 = StringField('Social media link 2', validators=[Optional() ,URL()])
    social_3 = StringField('Social media link 3', validators=[Optional() , URL()])
    # more info
    profile_pic = FileField("Profile Picture")
    category = SelectField("Category", choices=[('Technology',"Technology"),('Fitness','Fitness'),('Fashion','Fashion'),('Beauty','Beauty'),('Gaming','Gaming'),('Educational','Educational'),('Travel','Travel'),('Other','Other')], validators=[DataRequired()])
    biodata = TextAreaField("Bio/Description", validators=[DataRequired(), Length(max=500)])
    location = StringField("Location", validators=[DataRequired(), Length(max=50)])
    date_of_birth = DateField("Date of Birth", format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Update')

    def validate_username(self,username):
        if username.data != current_user.username:
            user = CommonUser.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username not available, please choose another.')

class UpdateAccountSponsor(FlaskForm):
    # basic
    username = StringField("Username", validators=[DataRequired(),Length(min=4,max=16)]) 
    # company info
    profile_pic = FileField("Profile Picture")
    company_name = StringField("Company/ Individual Name", validators=[DataRequired(), Length(min=4,max=50)])
    industry = StringField("Industry", validators=[DataRequired(), Length(min=4,max=50)])
    website = StringField("Website",validators=[URL()])
    company_address = TextAreaField("Company Address",validators=[DataRequired(),Length(min=15,max=100)])

    submit = SubmitField('Register')

    def validate_username(self,username):
        user = CommonUser.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username not available, please choose another.')
