from models import slist


# create a new instance of a linked list with values for testing methods
my_list = slist.SList()

my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()    # chaining, yeah!
print(my_list.head)

print(my_list.remove_from_back().value)
my_list.add_to_back("not").add_to_back("so").add_to_back("great")
my_list.add_to_back("not").add_to_back("so").add_to_back("good")
my_list.add_to_front("every")
my_list.add_to_front("all")
my_list.add_to_front("most")


my_list.remove_val("not")
my_list.remove_val("good")
my_list.remove_val("most")
my_list.remove_val("silly")


my_list.insert_at( "happy", 5 )

my_list.print_values()