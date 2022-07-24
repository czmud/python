import copy

class Product:
    def __init__( self, data ):
        self.name = data['name']
        self.price = data['price']
        self.category = data['category']
    def update_price( self, percent_change, is_increased ):
        if is_increased:
            self.price = round(self.price *( 1 + percent_change ), 2)
        else:
            self.price = round(self.price * ( 1 - percent_change ), 2)
        return self
    def print_info( self ):
        print(f'product: {self.name}, category: {self.category}, price: {self.price}')
        return self