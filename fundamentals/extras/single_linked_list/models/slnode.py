class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    def print_node( self ):
        print(f'{id(self.value)} with object value: {self.value}')
        return self
