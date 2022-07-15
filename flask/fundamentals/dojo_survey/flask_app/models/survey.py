from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.language = data['language']
        self.location = data['location']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def save( cls, data ):
        query = "INSERT INTO surveys ( name, location, language, comment ) VALUES \
            ( %(name)s, %(location)s, %(language)s, %(comment)s );"
        return connectToMySQL('dojo_survey').query_db( query, data )
    @classmethod
    def get_survey_by_id( cls, data ):
        query = "SELECT * FROM surveys WHERE id=%(id)s;"
        results = connectToMySQL('dojo_survey').query_db(query, data)
        survey = Survey(results[0])
        return survey
    @staticmethod
    def validate_survey(survey):
        is_valid = True
        if len(survey['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(survey["comment"]) < 10 or len(survey["comment"]) > 255:
            flash("Comment must be between 10 and 255 characters.")
            is_valid = False
        return is_valid