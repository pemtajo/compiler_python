

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

    def addFunction(self, name, type, parametros):
        f=Function(name, type, parametros)
        self.add(name, f)

    def addProcedure(self, name, parametros):
        p=Procedure(name, parametros)
        self.add(name, p)

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
        return "|"+self.name+ "," + self.type + "," + str(self.value)+"|"

class Function(Declaration):
    """docstring for Function."""
<<<<<<< HEAD

    def __init__(self, name, type, parametros):
        super(Function, self).__init__()
        self.name =name
        self.type = type
        self.parametros =parametros
=======
    def __init__(self, name, type, parametros):
        super(Function, self).__init__()
        self.name = name
        self.type = type
        self.parametros = parametros
>>>>>>> d4f8ee9f901ee2daa6e83dbc7fbcb5aae0b3f56d

    def __str__(self):
        return self.name+ " " + self.type + " " + str(self.parametros)

    def __repr__(self):
<<<<<<< HEAD
        return "["+self.name+ "," + self.type + "," + str(self.parametros)+"]"

class Procedure(Declaration):
    """docstring for Procedure."""
    def __init__(self, name, parametros):
        super(Procedure, self).__init__()
        self.name =name
        self.parametros =parametros

    def __str__(self):
        return self.name+ " " + str(self.parametros)

    def __repr__(self):
        return "["+self.name+ "," + str(self.parametros)+"]"
=======
        return "|"+self.name+ "," + self.type + "," + str(self.parametros)+"|"

class Procedure(object):
    """docstring for Procedure."""
    def __init__(self, name, parametros):
        super(Procedure, self).__init__()
        self.name = name
        self.parametros=parametros


    def __str__(self):
        return self.name+ " " +str(self.parametros)

    def __repr__(self):
        return "|"+self.name+ "," + str(self.parametros)+"|"
>>>>>>> d4f8ee9f901ee2daa6e83dbc7fbcb5aae0b3f56d
