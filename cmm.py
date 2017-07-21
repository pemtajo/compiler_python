#!/usr/bin/python
import sys
sys.path.append("../..")

import grammar
import errors


if len(sys.argv) < 2:
    print ("usage : cmm.py inputfile")
    raise SystemExit

if len(sys.argv) == 3:
    if sys.argv[1] == '-nocode':
         mylexer.emit_code = 0
    else:
         print ("Unknown option '%s'" % sys.argv[1])
         raise SystemExit
    filename = sys.argv[2]
else:
    filename = sys.argv[1]


arquive = open(filename).read()

grammar.parser.parse(arquive)

print(grammar.parser)          # Show parser object
