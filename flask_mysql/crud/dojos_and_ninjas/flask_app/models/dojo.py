from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    @property
    def ninja_count(self):
        return len(self.ninjas)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id \
            = ninjas.dojo_id;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        
        dojos = [ Dojo(results[0])]
        
        #dojo[0] = class object Dojo from results[0]

        for row in results:
            
            if row['id'] != dojos[-1].id:
                dojos.append( cls(row) )
            if row['ninjas.id'] != None:
                ninja_data = {
                    'id': row['ninjas.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'age': row['age'],
                    'dojo_id': row['dojo_id'],
                    'created_at': row['created_at'],
                    'updated_at': row['updated_at']
                }
                new_ninja = Ninja(ninja_data)
                dojos[-1].ninjas.append(new_ninja)

        return dojos



    @classmethod
    def save( cls, data ):
        query = "INSERT INTO dojos ( name ) VALUES ( %(name)s );"
        return connectToMySQL('dojos_and_ninjas').query_db( query, data )
    @classmethod
    def get_dojo_by_id( cls, data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id \
            = ninjas.dojo_id WHERE dojos.id=%(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)

        dojo = Dojo(results[0])
        for row in results:

            if row['ninjas.id'] != None:
                ninja_data = {
                    'id': row['ninjas.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'age': row['age'],
                    'dojo_id': row['dojo_id'],
                    'created_at': row['created_at'],
                    'updated_at': row['updated_at']
                }
                new_ninja = Ninja(ninja_data)
                dojo.ninjas.append(new_ninja)
    

        return dojo