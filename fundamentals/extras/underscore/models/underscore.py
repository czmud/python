

class Underscore:
    def map( self, iterable, callback ):
        results = []
        for val in iterable:
            results.append(callback(val))
        return results
    def find( self, iterable, callback ):
        for val in iterable:
            if callback(val):
                return val
        return None
    def filter( self, iterable, callback ):
        results = []
        for val in iterable:
            if callback(val):
                results.append(val)
        if len(results) > 0:
            return results
        return None
    def reject( self, iterable, callback ):
        results = []
        for val in iterable:
            if not callback(val):
                results.append(val)
        if len(results) > 0:
            return results
        return None

