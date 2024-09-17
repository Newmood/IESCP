# IESCP

This is Flask application for IESCP - Influencer Engagement and Sponsorship Coordination Platform, an individual university project.

## Features
The app includes the following features in a simple manner, could be improved further :
- User Authentication
- User Roles (Creator, Sponsor) 
- Creation of Campaign post by sponsor
- Creation of Ad request corresponding to particular campaign post by either creator or sponsor, accept or reject by other party.
- Creator Profile and Dashboard
- Sponsor Profile and Dashboard
- Browse pages for creators and sponsors
- Admin page to manage all data
- Dashboard page to view data in charts format (used ChartJS)

## Libraries used
The usual Flask framework with HTML, CSS, JS, Bootstrap, ChartJS.

## Installation
I was doing the project in a windows machine :
1. Clone the repository
2. Create a virtual environment
    -    ```pip install virtualenv``` then ```python -m venv .venv```
3. Install the dependencies
    -    ```pip install -r requirements.txt```

4. Activate the virtual environment
    -    ```.venv\Scripts\activate```
    - PowerShell has execution policies that control the conditions under which scripts are allowed to run. By default, the execution policy may be set to restrict the running of scripts, which can affect activating a Python virtual environment if you're using PowerShell.
    - If you encounter this issue, you can first change the execution policy by running the following command in PowerShell then try again:
        ```powershell
            Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
        ```

5. Creating database (currently not included inside app, run the following command to create database)
    -   In a python terminal, run the following commands one by one.
        ```python
            from app import app,db
            with app.app_context():
            db.create_all()
        ```
    - Flask migrate is not in use, but it is a good tool to use for database migrations.
6. Run the app
    -   ```flask run.py```

## Recommended changes
which I may or may not do in the future:
- Use of Flask-Blueprint for better organization of the app.
- Use of Flask-SocketIO for real-time communication between users.
- Use of Flask-Migrate for database migrations.
- Use of Flask-Caching for caching the data.
- Use of Flask-HTTPAuth for HTTP authentication.
- Use of Flask-JWT for JSON Web Tokens.
- Use of Flask-RESTful for RESTful API.
- Use of Flask-Admin for better management of the app.


