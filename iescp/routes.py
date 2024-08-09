import requests as rq
from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from iescp.forms import *
from iescp.models import *
from iescp.decorators import creator_required, sponsor_required
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

@app.route("/home")
@login_required
def home():
    return render_template('index.html', title="Home" ,ads_posts= ads_posts)


# DASHBOARD PAGE ----------------------------
@app.route("/dashboard")
@login_required
def dashboard():
     if current_user.role == "Sponsor":
          return render_template("sponsor/01_sponsor_dashboard.html", title= "Dashboard")
     elif current_user.role == "Creator":
          creator_data = Creator.query.filter_by(common_id=current_user.id).first()
          return render_template("creator/01_creator_dashboard.html", title= "Dashboard", creator_data=creator_data)
     else:
          return redirect(url_for('home'))
     

# CAMPAIGN PAGE ----------------------------
@app.route("/campaign")
@login_required
def campaign():
     if current_user.role == "Sponsor":
          return render_template("sponsor/02_sponsor_camp_list.html", title= "Campaigns")
     elif current_user.role == "Creator":
          return render_template("creator/02_creator_campaigns.html", title= "Campaigns")
     else:
          return redirect(url_for('home'))
     
# BROWSE PAGE ----------------------------
@app.route("/browse")
@login_required
def browse():
     if current_user.role == "Sponsor":
          return render_template("sponsor/03_browse_creator.html", title= "Browse")
     elif current_user.role == "Creator":
          creator_data = Creator.query.filter_by(common_id=current_user.id).first()
          return render_template("creator/03_browse_camps.html", title= "Browse", creator_data = creator_data)
     else:
          return redirect(url_for('home'))
          

# PROFILE PAGE ----------------------------
@app.route("/creator-profile", methods=['GET','POST'])
@login_required
@creator_required
def creator_profile():
     creator_data = Creator.query.filter_by(common_id=current_user.id).first()
     update_form = UpdateAccountCreator()
     if update_form.validate_on_submit():
          current_user.username = update_form.username.data
          current_user.profile_pic = update_form.profile_pic.data
          creator_data.social_link_1 = update_form.social_1.data
          creator_data.social_link_2 = update_form.social_2.data
          creator_data.social_link_3 = update_form.social_3.data
          creator_data.category = update_form.category.data
          creator_data.location = update_form.location.data
          creator_data.dob = update_form.date_of_birth.data
          creator_data.bio = update_form.biodata.data
          db.session.commit()
          flash("Your profile has been updated.",'success')
          return redirect(url_for('creator_profile'))
     elif request.method == 'GET':
          update_form.username.data = current_user.username
          update_form.social_1.data = creator_data.social_link_1
          update_form.social_2.data = creator_data.social_link_2
          update_form.social_3.data = creator_data.social_link_3
          update_form.category.data = creator_data.category
          update_form.location.data = creator_data.location
          update_form.date_of_birth.data = creator_data.dob
          update_form.biodata.data = creator_data.bio
     return render_template('creator/creator_profile.html', title="Profile", creator_data= creator_data, update_form=update_form)

@app.route("/sponsor-profile", methods=['GET','POST'])
@login_required
@sponsor_required
def sponsor_profile():
     sponsor_data = Sponsor.query.filter_by(common_id=current_user.id).first()
     update_form = UpdateAccountSponsor()
     if update_form.validate_on_submit():
          current_user.username = update_form.username.data
          current_user.profile_pic = update_form.profile_pic.data
          sponsor_data.company = update_form.company_name.data
          sponsor_data.industry = update_form.industry.data
          sponsor_data.website = update_form.website.data
          sponsor_data.company_address = update_form.company_address.data
          db.session.commit()
          flash("Your profile has been updated.",'success')
          return redirect(url_for('sponsor_profile'))
     elif request.method == 'GET':
          update_form.username.data = current_user.username
          update_form.company_name.data = sponsor_data.company
          update_form.industry.data = sponsor_data.industry
          update_form.website.data = sponsor_data.website
          update_form.company_address.data = sponsor_data.company_address
     return render_template('sponsor/sponsor_profile.html', title="Profile", sponsor_data=sponsor_data, update_form=update_form)




