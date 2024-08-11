from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user

def creator_required(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if current_user.is_authenticated and current_user.role=='Creator':
            return f(*args,**kwargs)
        else:
            flash("You must be a creator access that page.",'danger')
            return redirect(url_for('home'))
    return decorated_function
    
def sponsor_required(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if current_user.is_authenticated and current_user.role=='Sponsor':
            return f(*args,**kwargs)
        else:
            flash("You must be a sponsor access that page.",'danger')
            return redirect(url_for('home'))
    return decorated_function

# admin registered as sponsor, admin@admin.com
def admin_required(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if current_user.is_authenticated and current_user.email=='admin@admin.com':
            return f(*args,**kwargs)
        else:
            flash("You must be an admin access that page.",'danger')
            return redirect(url_for('home'))
    return decorated_function