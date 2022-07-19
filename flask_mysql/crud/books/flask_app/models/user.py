from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class User:
    db = 'books'
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []
        self.books_not_liked = []
    @property
    def full_name(self):
        return self.first_name+" "+self.last_name
    @classmethod
    def save( cls, data ):
        query = "INSERT INTO users ( first_name, last_name ) VALUES \
            ( %(first_name)s, %(last_name)s );"
        return connectToMySQL(cls.db).query_db( query, data )
    @classmethod
    def get_user_by_id( cls, data ):
        query = "SELECT * FROM users LEFT JOIN favorites ON users.id \
            = favorites.user_id LEFT JOIN books ON favorites.book_id \
            = books.id WHERE users.id=%(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        users = cls(results[0])
        for row in results:
            if row['books.id'] != None:
                book_data = {
                    'id': row['books.id'],
                    'title': row['title'],
                    'num_of_pages': row['num_of_pages'],
                    'created_at': row['books.created_at'],
                    'updated_at': row['books.updated_at']
                }
                users.books.append(book.Book(book_data))
        users.books_not_liked = User.books_not_liked_by_id(data)
        return users
    @classmethod
    def get_all( cls ):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users
    @classmethod
    def books_not_liked_by_id( cls, data ):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id \
            = favorites.book_id WHERE book_id NOT IN (SELECT book_id \
            FROM favorites WHERE user_id = %(id)s) OR book_id IS NULL;"
        results = connectToMySQL(cls.db).query_db(query, data)
        books = []
        if len(results) > 0:
            books.append(book.Book(results[0]))
        for row in results:
            if books[-1].id != row['id']:
                books.append(book.Book(row))
        return books

