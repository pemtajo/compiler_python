

names={ }

class Variable(object):
    """Exclusive class for control variables"""
    """docstring for Variable."""
    def __init__(self, arg):
        super(Variable, self).__init__()
        self.arg = arg


def add(type, t):
    if(t[1]==''):
        if(type=="int"):
            t[1]=0
        elif(type=="bool"):
            t[1]=False

    names[t[0]]=[type, t[1]]

def show(v):
    return names[v][1]

def change(v, value):
    names[v][1]=value
