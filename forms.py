from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField, FileField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, URL
from wtforms_alchemy import PhoneNumberField

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
    phone_number = PhoneNumberField("Phone Number", validators=[DataRequired()])
    # links 
    social_1 = StringField('Social media link', validators=[DataRequired(), URL()])
    social_2 = StringField('Social media link', validators=[URL()])
    social_3 = StringField('Social media link', validators=[URL()])
    # more info
    profile_pic = FileField("Profile Picture")
    category = SelectField("Category", choices=[('tech',"Technology"),('fitness','Fitness'),('fashion','Fashion'),('beauty','Beauty'),('game','Gaming'),('edu','Educatoinal'),('travel','Travel'),('other','Other')], validators=[DataRequired()])
    biodata = TextAreaField("Bio/Description", validators=[DataRequired(), Length(max=150)])
    location = StringField("Location", validators=[DataRequired(), Length(max=50)])
    date_of_birth = DateField("Date of Birth", format='%Y-%m-%d', validators=[DataRequired()])
    # set password
    password = PasswordField("Enter your password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    # NEED A FLAG TAG FOR ADMIN REASONS

    submit = SubmitField('Register')

class SponsorRegistrationForm(FlaskForm):
    # basic
    firstname = StringField("First name", validators=[DataRequired()])
    lastname = StringField("Last name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired(),Length(min=4,max=16)]) 
    email = StringField("Enter your email", validators=[DataRequired(), Email()])
    phone_number = PhoneNumberField("Phone Number", validators=[DataRequired()])
    # company info
    company_name = StringField("Company/ Individual Name", validators=[DataRequired(), Length(min=4,max=50)])
    industry = StringField("industry", validators=[DataRequired(), Length(min=4,max=50)])
    website = StringField("Website",validators=[URL()])
    company_address = TextAreaField("Company Adress",validators=[DataRequired(),Length(min=15,max=100)])
    # set password
    password = PasswordField("Enter your password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    # NEED A FLAG TAG FOR ADMIN REASONS

    submit = SubmitField('Register')

    


