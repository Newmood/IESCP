from flask import Flask
from flask import render_template, url_for, flash, redirect, request
import requests as rq
from forms import *

app = Flask(__name__)

app.config['SECRET_KEY'] = '7cf5fbfb549d204db232cebd4500fdb3'

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
def home():
    return render_template('index.html', title="Home" ,ads_posts= ads_posts)

@app.route("/creator-register", methods=['GET','POST'])
def creator_register():
     creator_form = CreatorRegistrationForm()
     if creator_form.validate_on_submit():
          flash("Creator account has been created. Please login to continue.",'success')
          return redirect(url_for('login'))
     return render_template('creator/creator_register.html', title="Creator Register", creator_form=creator_form)

@app.route("/sponsor-register", methods=['GET','POST'])
def sponsor_register():
     sponsor_form = SponsorRegistrationForm()
     if sponsor_form.validate_on_submit():
          flash("Sponsor account has been created. Please login to continue.",'success')
          return redirect(url_for('login'))
     return render_template('sponsor/sponsor_register.html', title="Sponsor Register", sponsor_form=sponsor_form)



@app.route("/login", methods =['GET','POST'])
def login():
     form = LoginForm()
     if form.validate_on_submit():
          if form.email.data == "admin@admin.com":
               return redirect(url_for('home'))
          else:
               flash('Login unsuccessful. Please check credentials and try again.','danger')
     return render_template('login.html', title="Login", form=form)

@app.route("/register")
def register():
     creator_form = CreatorRegistrationForm()
     sponsor_form = SponsorRegistrationForm()
     return render_template('z_initial_register.html',title='register',creator_form=creator_form, sponsor_form=sponsor_form)

if __name__ == "__main__":
        app.run(debug=True)