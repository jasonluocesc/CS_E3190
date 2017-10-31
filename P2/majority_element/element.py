class Element(object):
    
    def __init__(self, x):
        self.__x = x
    
    def __eq__(self, other):
        return self.__x == other.__x if isinstance(other, Element) else False
    
    def __str__(self):
        return str(self.__x)
        
def to_element_list(l):
    return [Element(x) for x in l]