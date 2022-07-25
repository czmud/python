from models import underscore

under = underscore.Underscore()

list1 = [1,2,3,4,5,6,7,8,9,10,11]

cube_map = under.map( list1, lambda x: x**3 )
print(cube_map)
div_by_three_find = under.find(list1, lambda x: x % 3 == 0 and x > 5)
print(div_by_three_find)
div_by_three_filter = under.filter(list1, lambda x: x % 3 == 0)
print(div_by_three_filter)
div_by_three_reject = under.reject(list1, lambda x: x % 3 == 0)
print(div_by_three_reject)