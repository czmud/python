from models import pet

class Ninja:
    def __init__( self, data ):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.pet = pet.Pet( data['pet'] )
        self.treats = data['treats']
        self.pet_food = data['pet_food']
    def walk( self ):
        self.pet.play()
        return self
    def feed( self ):
        self.pet.eat()
        return self
    def bathe( self ):
        self.pet.noise()
        return self