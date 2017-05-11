
import ply.yacc as yacc

import mylexer
 	
tokens=mylexer.tokens

def p_assign(p):
	'''assign : NAME EQUALS expr'''

def p_expr(p):
	'''expr : expr PLUS term
			| expr MINUS term
			| term'''

def p_term(p):
	'''term : term PLUS factor
			| term MINUS factor
			| factor'''

def p_factor(p):
	'''factor : NUMBER'''


def p_error(p):
    pass


yacc.yacc()  #build the parser


data = "x=3*4+5*6"
yacc.parse(data)