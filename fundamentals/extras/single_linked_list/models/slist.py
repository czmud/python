from models import slnode

class SList:
    def __init__( self ):
        self.head = None
    def add_to_front( self, val  ):    # added this line, takes a value
        new_node = slnode.SLNode( val )   # create a new instance of our Node class using the given value
        current_head = self.head    # save the current head in a variable
        new_node.next = current_head
        self.head = new_node
        return self
    def add_to_back( self, val ):
        if self.head == None:
            self.add_to_front( val )
            return self
        new_node = slnode.SLNode( val )
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = new_node
        return self
    def remove_from_front( self ):
        removed_value = self.head
        self.head = self.head.next
        return removed_value
    def remove_from_back( self ):
        runner = self.head
        while runner.next.next != None:
            runner = runner.next
        removed_value = runner.next
        runner.next = None
        return removed_value
    
    def remove_val( self, val ):
        if self.head.value == val:
            print("removed head")
            self.remove_from_front().value
            return self
        runner = self.head
        while runner.next != None:
            if runner.next.value == val:
                if runner.next.next == None:
                    print("removed last")
                    self.remove_from_back()
                    return self
                else:
                    print("removed middle")
                    print("--")
                    runner.next.print_node()
                    print("--")
                    runner.next = runner.next.next
                    return self
            runner = runner.next
        print(f'Error: value "{val}" does not exist in list')
        return self
    def insert_at( self, val, n ):
        if n == 0:
            self.add_to_front( val )
            return self
        runner = self.head
        next_index = 1
        while runner != None:
            if n == next_index:
                temp_hold = runner.next
                runner.next = slnode.SLNode( val )
                runner.next.next = temp_hold
                print(f'inserted at n = {next_index}')
                return self
            next_index += 1
            runner = runner.next
        if n == next_index:
            self.add_to_back( val )
            return self

        print(f'Error: position argument given as n = {n} but list only {next_index - 1} long')
        print(f'please enter value where 0 <= n <= {next_index}')
        return self

    def print_values ( self ):
        runner = self.head
        while runner != None:
            runner.print_node()
            runner = runner.next
        return self







