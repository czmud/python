from flask_app.config.mysqlconnection import connectToMySQL

class Favorite:
    db = 'books'
    def __init__( self , data ):
        self.id = data['id']
        self.user_id = data['user_id']
        self.book_id = data['book_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def save( cls, data ):
        query = "INSERT INTO favorites ( user_id, book_id ) VALUES \
            ( %(user_id)s, %(book_id)s );"
        return connectToMySQL(cls.db).query_db( query, data )