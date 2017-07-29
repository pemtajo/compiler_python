

class Escopo(object):
    """docstring for Escopo."""
    names = {}

    def __init__(self):
        super(Escopo, self).__init__()


    def add(self, value):
        for element in value:
            try:
                self.names[element] #has a declaration with this name
                print("Same Name Variavel Error")
                return
            except:
                self.names[element]= value[element]


    def show(self, d):
        try:
            self.names[d].value
        except:
            for element in self.names:
                if isinstance(element, Procedure) or isinstance(element, Function):
                    try:
                        return self.names[element].escopo.show(d)
                    except:
                        continue
        return None

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
        return self.name+ " " + str(self.type) + " " + str(self.value)

    def __repr__(self):
        return "|"+self.name+ "," + str(self.type) + "," + str(self.value)+"|"

class Function(Declaration):
    """docstring for Function."""
    def __init__(self, name, type, parametros, block):
        super(Function, self).__init__()
        self.name = name
        self.type = type
        self.parametros = parametros
        self.block=block

    def __str__(self):
        return self.name+ " " + self.type + " " + str(self.parametros)

    def __repr__(self):
        return "|"+self.name+ "," + self.type + "," + str(self.parametros)+"|"

class Procedure(object):
    """docstring for Procedure."""
    def __init__(self, name, parametros, block):
        super(Procedure, self).__init__()
        self.name = name
        self.parametros=parametros
        self.block=block

    def __str__(self):
        return self.name+ " " +str(self.parametros)

    def __repr__(self):
        return "|"+self.name+ "," + str(self.parametros)+"|"

class Block(object):
    """docstring for Block."""
    def __init__(self, variaveis, statements):
        super(Block, self).__init__()
        print(variaveis)
        self.escopo=Escopo()
        escopo.add(variaveis)
        self.statements=statements

    def __str__(self):
        return self.escopo+ " " +str(self.statements)

    def __repr__(self):
        return "|"+self.escopo+ "," + str(self.statements)+"|"
