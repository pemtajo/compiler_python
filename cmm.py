#!/usr/bin/python
import sys
sys.path.append("../..")

import grammar
import errors

imprimir=False
if len(sys.argv) < 2:
    print ("usage : cmm [-debug] inputfile")
    raise SystemExit

if len(sys.argv) == 3:
    if sys.argv[1] == '-debug':
        imprimir =  True;
    else:
         print ("Unknown option '%s'" % sys.argv[1])
         raise SystemExit
    filename = sys.argv[2]
else:
    filename = sys.argv[1]

arquive = open(filename).read()

grammar.parser.parse(arquive)

if imprimir:
    print(grammar.var_global)          # Show parser object
