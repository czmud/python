from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
import random
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#define global reg expressions for data validation
password_regex = re.compile(r'^.*(?=.{8,})(?=.*[a-zA-Z])(?=.*\d)(?=.*[!#$%&? "]).*$')
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# name_regex = re.compile(r^)


# ^.*(?=.{8,})(?=.*[a-zA-Z])(?=.*\d)(?=.*[!#$%&? "]).*$

# ---

# ^.*              : Start
# (?=.{8,})        : Length
# (?=.*[a-zA-Z])   : Letters
# (?=.*\d)         : Digits
# (?=.*[!#$%&? "]) : Special characters
# .*$              : End



class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.salt = data['salt']
        self.password_hash = data['password_hash']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @property
    def full_name(self):
        return self.first_name+" "+self.last_name
    @classmethod
    def save( cls, data ):
        query = "INSERT INTO users ( first_name, last_name, email, password_hash, salt ) VALUES \
            ( %(first_name)s, %(last_name)s, %(email)s, %(password_hash)s, %(salt)s );"
        return connectToMySQL('login_and_registration').query_db( query, data )
    @classmethod
    def get_user_by_email( cls, data ):
        query = "SELECT * FROM users WHERE email=%(email)s;"
        results = connectToMySQL('login_and_registration').query_db(query, data)
        user = User(results[0])
        return user
    @classmethod
    def get_user_by_id( cls, data ):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        results = connectToMySQL('login_and_registration').query_db(query, data)
        user = User(results[0])
        return user
    @staticmethod
    def user_exists(user):
        query = "SELECT email FROM users;"
        results = connectToMySQL('login_and_registration').query_db(query)
        for row in results:
            if user['email'] == row['email']:
                return True
        return False
    @staticmethod
    def validate_login(data):
        if not password_regex.match(data['password']):
            flash("email and password combination did not match", "login")
            return False
        if not email_regex.match(data['email']):
            flash("email and password combination did not match", "login")
            return False
        elif not User.user_exists(data):
            flash("email and password combination did not match", "login")
            return False
        else:
            user = User.get_user_by_email(data)
            password_string = data['password'] + user.salt
        if not bcrypt.check_password_hash(user.password_hash, password_string):
            flash("email and password combination did not match", "login")
            return False
        return True
    
    @staticmethod
    def validate_user(user):
        is_valid = True
        if not email_regex.match(user['email']):
            is_valid = False
            flash("must enter valid email", "create")
        elif User.user_exists(user):
            is_valid = False
            flash("account already exists for this email", "create")
        if not password_regex.match(user['password']):
            is_valid = False
            flash("must enter valid password", "create")
            flash("password must contain 8 characters", "create")
        elif not password_regex.match(user['password_confirm']):
            is_valid = False
            flash("passwords and confirmation do not match", "create")
        elif user['password'] != user['password_confirm']:
            is_valid = False
            flash("passwords and confirmation do not match", "create")
        return is_valid
    @staticmethod
    def generate_salt():
        salt = ''
        for i in range(16):
            next_char = random.randint(0,61)
            if next_char <= 9:
                next_char += 48
            elif next_char <= 35:
                next_char += 55
            else:
                next_char += 61
            salt += chr(next_char)
        return salt
    @staticmethod
    def hash_password(user, salt):
        print(user['password'])
        password_string = user['password'] + salt
        password_hash = bcrypt.generate_password_hash(password_string)
        print(password_hash)
        return password_hash