from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

#define global reg expressions for data validation
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Email:
    db = 'email_schema'
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def save( cls, data ):
        query = "INSERT INTO emails ( email ) VALUES ( %(email)s );"
        return connectToMySQL(cls.db).query_db( query, data )
    @classmethod
    def delete_email_by_id( cls, data ):
        query = "DELETE FROM emails WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db( query, data )
    @classmethod
    def get_all( cls ):
        query = "SELECT * FROM emails;"
        results = connectToMySQL(cls.db).query_db(query)
        emails = []
        for row in results:
            emails.append(cls(row))
        return emails
    @staticmethod
    def validate_email(data):
        is_valid = True
        if not email_regex.match(data['email']):
            is_valid = False
            flash("email is not valid")
        if Email.email_exists(data):
            is_valid = False
            flash("email already exists")
        return is_valid
    @classmethod
    def email_exists( cls, data):
        query = "SELECT email FROM emails WHERE email = %(email)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        print(len(results))
        if len(results) > 0:
            return True
        return False
