from models import store


store_data = {
    "name": "hungy hippos",
}
product_data = [ {
    "name": "socks",
    "price": 5,
    "category": "apparel" 
    }, { 
    "name": "hoodie",
    "price": 12,
    "category": "apparel"
    }, {
    "name": "blue shirt",
    "price": 9,
    "category": "apparel"
    }, { 
    "name": "basketball",
    "price": 25,
    "category": "sports"
    }, { 
    "name": "pants",
    "price": 16,
    "category": "apparel"
    }]



# create store
store1 = store.Store(store_data)

# add product instances to store
for row in product_data:
    store1.add_product(row)

# sell product id = 1
store1.sell_product( 1 )


# inflation of 2% just hit
store1.inflation( 0.02 )

# clearance on apparel items - 60% discount
store1.set_clearance( "apparel", .60 )

# print store and products in store
print(store1.__dict__)
for product in store1.products:
    product.print_info()
