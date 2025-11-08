"""app.py: render and route to webpages"""

import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from db.query import get_all, get_session
from db.server import init_database
from db.schema import Users
from db import query
from hashshit import *

import loggingSetUp
from loggingSetUp import logger

# load environment variables from .env
load_dotenv()

# database connection - values set in .env
db_name = os.getenv('db_name')
db_owner = os.getenv('db_owner')
db_pass = os.getenv('db_pass')
db_url = f"postgresql://{db_owner}:{db_pass}@localhost/{db_name}"

def create_app():
    """Create Flask application and connect to your DB"""
    # create flask app
    app = Flask(__name__, 
                template_folder=os.path.join(os.getcwd(), 'templates'), 
                static_folder=os.path.join(os.getcwd(), 'static'))
    
    # connect to db
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    
    # Initialize database
    with app.app_context():
        if not init_database():
            print("Failed to initialize database. Exiting.")
            exit(1)

    # ===============================================================
    # routes
    # ===============================================================

    # create a webpage based off of the html in templates/index.html
    @app.route('/')
    def index():
        """Home page"""
        return render_template('index.html')
    
    def insertUser(record):
        session = get_session()
        try:
            session.add(record)
            session.commit()
            session.expire_all()

            # print("User Data committed correctly")#Debugging
            # data = session.query(Users).all()
            # print(type(data))

        except Exception as ex:
            session.rollback()
            render_template('/error.html', error = ex)
            print("Error in session dumbass",ex)
        finally:
            session.close() 
    
    @app.route('/signup', methods = ["GET", "POST"])
    def signup():
        try: 
            """Sign up page: enables users to sign up"""
            valid = True
            if request.method == 'POST':
                print("Signing up user")
                FirstName = rmWhitespace(request.form["firstName"])
                LastName=rmWhitespace(request.form["lastName"])
                Email=rmWhitespace(request.form["email"])
                PhoneNumber=rmWhitespace(request.form["phoneNumber"])
                Password=rmWhitespace(request.form["password"])
                Password = encrypt(Password)
                print("FIRSTNAME", FirstName.isalpha())
                
                if (not(FirstName.isalpha())):
                    logger.error("User tried to sign up with non alpha name")
                    return render_template('error.html', error = "Names (both first and last) can only have letters")   
                if (not (len(PhoneNumber) <= 10)):
                    logger.error("User tried an invalid (>10 digit) phone number")
                    return render_template('error.html', error = "Phone number cannot be greter than 10 digits")   

                user = Users(FirstName = FirstName, LastName = LastName, Email = Email, PhoneNumber = PhoneNumber, Password = Password)
                insertUser(user)
                # return redirect(url_for("success"))
            #TODO: implement sign up logic here

            return render_template('signup.html')
        except Exception as ex:
            logger.error("Error in signup route")
            return render_template('/error.html', error = ex)
            print("Error in session dumbass",ex)
    
    @app.route('/login', methods = ["GET", "POST"])
    def login():#This has the distinct problem that people with the same first and last name will mess things up 
        """Log in page: enables users to log in"""#Seeing as how this just needs to work for the lab I don't see it as an issue
        # session = get_session()#But I understand that the issue is there, I am not blind to it
        # print("TEST")
        print("REQUEST", request.method)
        if request.method == 'POST':
            session = get_session()
            fN = rmWhitespace(request.form["firstName"])
            lN = rmWhitespace(request.form["lastName"])
            if  (not(lN.isalpha or lN.isalpha)):
                logger.error("User tried to log in with non alpa name")
                return render_template('error.html', error = "Names (both first and last) can only have letters")   
            p = rmWhitespace(request.form["password"])
            gotPerson = session.query(Users).filter(Users.LastName.ilike(lN), Users.FirstName.ilike(fN)).first()
            if gotPerson != None:
                if compareHash(p, gotPerson.Password) :#gotPerson.Password == p
                    print("Success")
                    return redirect(url_for("success"))
                else:
                    print("Failure")
                    return redirect(url_for("login"))
                    # raise Exception("Password is incorrect")
            else:
                logger.error("User First Or Last Name Not Found")
                return render_template('error.html', error = "UserFirstOrLastNameNotFound")   

                         
            # 
        #TODO: implement login logic here

        return render_template('login.html')

    @app.route('/users', methods = ["GET"])
    def users():
        """Users page: displays all users in the Users table"""
        session = get_session()
        all_users = data = session.query(Users).all()#get_all(Users)
        print(type(all_users))
        return render_template('users.html', users=all_users)

    @app.route('/success')
    def success():
        """Success page: displayed upon successful login"""
        return render_template('success.html')

    return app

if __name__ == "__main__":
    app = create_app()
    # debug refreshes your application with your new changes every time you save
    app.run(debug=True)