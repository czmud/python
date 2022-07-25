
class Pet:
    def __init__(self, data):
        self.name = data['name']
        self.type = data['type']
        self.tricks = data['tricks']
        self.health = data['health']
        self.energy = data['energy']
        self.sound = data['sound']
    def sleep( self ):
        self.energy += 25
        return self
    def eat( self ):
        self.energy += 5
        self.health += 10
        return self
    def play( self ):
        self.health += 5
        return self
    def noise( self ):
        print(self.sound)
        return self

