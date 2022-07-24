from models import product


class Store:
    def __init__( self, data ):
        self.name = data['name']
        self.products = []
    def add_product( self, new_product ):
        self.products.append(product.Product(new_product))
        return self
    def sell_product( self, id ):
        self.products[ id ].print_info()
        self.products.pop(id)
        return self
    def inflation( self, percent_increase ):
        for product in self.products:
            product.update_price( percent_increase, True )
        return self
    def set_clearance( self, category, percent_discount ):
        for product in self.products:
            if product.category == category:
                product.update_price( percent_discount, False )
        return self


