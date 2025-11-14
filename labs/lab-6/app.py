"""app.py: render and route to webpages"""

import os
import bcrypt
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, session, url_for
from db.query import get_all, insert
from db.server import get_session, init_database
from db.schema import Users

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
    
    @app.route('/signup', methods=['GET','POST'])
    def signup():
        """Sign up page: enables users to sign up"""
        error: str
        is_valid: bool = False  
            
        if request.method == 'POST':
            try:
                fname = request.form["fname"]
                lname = request.form["lname"]
                email = request.form["email"]
                phone = request.form["phone"]
                password = request.form["password"]
                            
                if fname.isalpha():
                    print(f'Input: {fname} is valid.')
                    is_valid = True
                else:
                    error_msg = f'Input: {fname} is INVALID! First Name can only contain letters.'
                    print(f'Input: {fname} is valid.')
                    error = error_msg
                        
                if lname.isalpha():
                    print(f'Input: {lname} is valid.')
                    is_valid = True
                else:
                    error_msg = f'Input: {lname} is INVALID! Last Name can only contain letters.'
                    print(f'Input: {lname} is valid.')
                    error = error_msg
                        
                # If valid → hash password and insert
                if is_valid:
                    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                        
                    user = Users(
                        FirstName=fname,
                        LastName=lname,
                        Email=email,
                        PhoneNumber=phone,
                        Password=hashed_pw)
                    insert(user)
                    
                    return redirect(url_for('index'))
                    
            except Exception as e:
                print("Error inserting records:", e)
                user_error_msg = "Something went wrong. IDK I am losing my mind. Please try again later."
                return render_template('error.html', error=user_error_msg)
                logger.error(f"An error has occured: {error}")

        return render_template('signup.html')
    
    @app.route('/login', methods=['GET','POST'])
    def login():
        """Log in page: enables users to log in"""
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            session = get_session()
            try:
                # Query for a user that matches both email and password
                user = session.query(Users).filter_by(Email=email, Password=password).first()

                if user:
                    # Login successful
                    return redirect(url_for('success'))
                else:
                    # Login failed
                    return render_template('login.html', error="Invalid email or password")
            finally:
                session.close()
        # GET request: just render the login form
        return render_template('login.html')

    @app.route('/users')
    def users():
        """Users page: displays all users in the Users table"""
        all_users = get_all(Users)
        
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