#!/usr/bin/python
import sys
sys.path.append("../..")

import ply.yacc as yacc

def unknownSignal(t):
    print("Unknown Signal at '%s', in Line %d , Column %d!" % (t.value, t.lineno, t.lexpos))

def unknownError(t):
    print("Syntax error at '%s', in Line %d , Column %d" % (t.value, t.lineno, t.lexpos))
