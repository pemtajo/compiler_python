

class Escopo(object):
    """docstring for Escopo."""
    names = {}

    def __init__(self):
        super(Escopo, self).__init__()


    def add(self,name, value):
        try:
            self.names[name] #has a declaration with this name
            print("Same Name Variavel Error")
            return
        except:
            self.names[name]= value


    def addVariable(self, name, type, value):
        v=Variable(name, type, value)
        self.add(name, v)

    def show(self, d):
        return self.names[d].value

    def change(self, v, value):
        self.names[v].value=value

    def all(self):
        return self.names


class Declaration(object):
    """docstring for Declaration."""
    name=''

    def __init__(self):
        super(Declaration, self).__init__()

    def __str__(self):
     return self.name

    def name(self):
        return self.name

class Variable(Declaration):
    """Exclusive class for control variables"""
    """docstring for Variable."""
    name=''
    type=''
    value=None

    def __init__(self, name, type, value):
        super(Variable, self).__init__()
        self.name = name
        self.type = type
        self.value = value
        if(value==None):
            if(type=="int"):
                self.value=0
            elif(type=="bool"):
                self.value=False
            elif(type=="string"):
                self.value=''

    def __str__(self):
        return self.name+ " " + self.type + " " + str(self.value)

    def __repr__(self):
        return "["+self.name+ "," + self.type + "," + str(self.value)+"]"

class Function(object):
    """docstring for Function."""
    def __init__(self):
        super(Function, self).__init__()
