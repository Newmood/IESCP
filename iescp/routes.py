import requests as rq
from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from iescp.forms import *
from iescp.models import *
from iescp import app, db, bcrypt

ads_posts= [
     {
          "author" : "Fell Technologies",
          "title" : "Promotional content on Fell G-series",
          "description" : "Talk about laptops in G-series for 1 min highlighting all features.",
          "budget" : "INR 15,000",
          "industry" : "Technology",
          "date_posted" : "03 August 2024",
          "end_date" : "10 August 2024",
          "public" : True
     },
     {
          "author" : "Babel FinCorp",
          "title" : "B-express Credit Card",
          "description" : "Talk about all features of B-express credit card (except interest rate)",
          "budget" : "INR 15,000",
          "industry" : "Banking",
          "date_posted" : "03 August 2024",
          "end_date" : "10 August 2024",
          "public" : True
     },
     {
          "author" : "Babel FinCorp",
          "title" : "B-express Credit Card",
          "description" : "Talk about all features of B-express credit card (except interest rate)",
          "budget" : "INR 15,000",
          "industry" : "Banking",
          "date_posted" : "03 August 2024",
          "end_date" : "10 August 2024",
          "public" : True
     }
]


@app.route("/")
def landing():
    return render_template('landing.html')

@app.route("/home")
@login_required
def home():
    return render_template('index.html', title="Home" ,ads_posts= ads_posts)

@app.route("/creator-register", methods=['GET','POST'])
def creator_register():
     if current_user.is_authenticated:
          return redirect(url_for('home'))
     creator_form = CreatorRegistrationForm()
     if creator_form.validate_on_submit():
          hashed_pwd = bcrypt.generate_password_hash(creator_form.password.data).decode('utf-8')
          user = CommonUser(role= 'Creator', username = creator_form.username.data, password = hashed_pwd, email = creator_form.email.data, firstname = creator_form.firstname.data, lastname= creator_form.lastname.data, phone_no = creator_form.phone_number.data )
          db.session.add(user)
          db.session.commit()
          userC = Creator(common_id= user.id, social_link_1= creator_form.social_1.data, social_link_2= creator_form.social_2.data, social_link_3= creator_form.social_3.data, category = creator_form.category.data, location = creator_form.location.data, dob = creator_form.date_of_birth.data, bio = creator_form.biodata.data)
          db.session.add(userC)
          db.session.commit()
          flash("Creator account has been created. Please login to continue.",'success')
          return redirect(url_for('login'))
     return render_template('creator/creator_register.html', title="Creator Register", creator_form=creator_form)

@app.route("/sponsor-register", methods=['GET','POST'])
def sponsor_register():
     if current_user.is_authenticated:
          return redirect(url_for('home'))
     sponsor_form = SponsorRegistrationForm()
     if sponsor_form.validate_on_submit():
          hashed_pwd = bcrypt.generate_password_hash(sponsor_form.password.data).decode('utf-8')
          user = CommonUser(role= 'Sponsor', username = sponsor_form.username.data, password = hashed_pwd, email=sponsor_form.email.data, firstname = sponsor_form.firstname.data, lastname= sponsor_form.lastname.data, phone_no = sponsor_form.phone_number.data)
          db.session.add(user)
          db.session.commit()
          userS = Sponsor(common_id= user.id, company= sponsor_form.company_name.data, industry =sponsor_form.industry.data, website=sponsor_form.website.data, company_address= sponsor_form.company_address.data)
          db.session.add(userS)
          db.session.commit()
          flash("Sponsor account has been created. Please login to continue.",'success')
          return redirect(url_for('login'))
     return render_template('sponsor/sponsor_register.html', title="Sponsor Register", sponsor_form=sponsor_form)



@app.route("/login", methods =['GET','POST'])
def login():
     if current_user.is_authenticated:
          return redirect(url_for('home'))
     form = LoginForm()
     if form.validate_on_submit():
          user = CommonUser.query.filter_by(email = form.email.data).first()

          if user and bcrypt.check_password_hash(user.password, form.password.data):
               login_user(user,remember=form.remember.data)
               # next_page = request.args.get('next')
               # if next_page:
               #      return redirect(next_page)
               return redirect(url_for('home'))
          else:
               flash('Login unsuccessful. Please check credentials and try again.','danger')
     return render_template('login.html', title="Login", form=form)

# @app.route("/register")
# def register():
#      creator_form = CreatorRegistrationForm()
#      sponsor_form = SponsorRegistrationForm()
#      return render_template('z_initial_register.html',title='register',creator_form=creator_form, sponsor_form=sponsor_form)


@app.route("/logout")
def logout():
     logout_user()
     return redirect(url_for('landing'))

@app.route("/campaign")
@login_required
def campaign():
     if current_user.role == "Sponsor":
          return render_template("sponsor/02_sponsor_camp_list.html", title= "Campaigns")
     elif current_user.role == "Creator":
          return render_template("creator/02_creator_campaigns.html", title= "Campaigns")
          
@app.route("/profile")
@login_required
def profile():
    return render_template('profile.html', title="Profile")
