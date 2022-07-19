from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Book:
    db = 'books'
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users = []
        self.users_not_liked = []
    @classmethod
    def save( cls, data ):
        query = "INSERT INTO books ( title, num_of_pages ) VALUES \
            ( %(title)s, %(num_of_pages)s );"
        return connectToMySQL(cls.db).query_db( query, data )
    @classmethod
    def get_book_by_id( cls, data ):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id \
            = favorites.book_id LEFT JOIN users ON favorites.user_id \
            = users.id WHERE books.id=%(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        books = cls(results[0])
        for row in results:
            if row['users.id'] != None:
                user_data = {
                    'id': row['users.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }
                books.users.append(user.User(user_data))
        books.users_not_liked = Book.users_not_liked_by_id(data)
        return books
    @classmethod
    def get_all( cls ):
        query = "SELECT * FROM books;"
        results = connectToMySQL(cls.db).query_db(query)
        books = []
        for row in results:
            books.append(cls(row))
        return books
    @classmethod
    def users_not_liked_by_id( cls, data ):
        query = "SELECT * FROM users LEFT JOIN favorites ON users.id \
            = favorites.user_id WHERE user_id NOT IN (SELECT user_id \
            FROM favorites WHERE book_id = %(id)s) OR user_id IS NULL;"
        results = connectToMySQL(cls.db).query_db(query, data)
        users = []
        if len(results) > 0:
            users.append(user.User(results[0]))
        for row in results:
            if users[-1].id != row['id']:
                users.append(user.User(row))
        return users
