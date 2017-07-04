#!/usr/bin/python
import sys
sys.path.append("../..")

from ply import *

'''if len(sys.argv) <2:
    print("usage : yply.py [-nocode] inputfile")
    raise SystemExit'''


'''
palavras reservadas
bool break for false if int return string true void while
'''
reserved = {
	'bool'	:	'BOOL',
	'break'	:	'BREAK',
	'for'	:	'FOR',
	'false'	:	'FALSE',
	'if'	:	'IF',
	'int'	:	'INT',
	'return':	'RETURN',
	'string':	'STRING',
	'true'	:	'TRUE',
	'void'	:	'VOID',
	'while'	:	'WHILE',
	'proc'	:	'PROCEDURE',	
	'func'	:	'FUNCTION'

}




tokens = ['NAME', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS',
 'RPAREN', 'LPAREN', 'RCOLC', 'LCOLC', 'RBRACE', 'LBRACE', 'COMMA', 'SEMICOLON', 'OR', 'AND', 'EXPLAMATION', 'INTERROGATION', 'COLON', 
 'PLUSPLUS', 'DIFF', 'MENOR', 'MAIOR', 'MENOREQUALS', 'MAIOREQUALS', 'SUMEQUALS', 'MINUSEQUALS', 'TIMESEQUALS', 'DIVIDEEQUALS', 'MOD', 'ASPAS']+ list(reserved.values())


'''
tokens e simbolos
( ) [ ] { } , ; + - * / == != > >= < <= || && ! = += -= *= /= %= ? :
'''
t_ignore 		= ' \t'

t_RPAREN		= r'\('
t_LPAREN		= r'\)'
t_RCOLC			= r'\['
t_LCOLC			= r'\]'
t_RBRACE		= r'\{'
t_LBRACE		= r'\}'

t_COMMA			= r','
t_SEMICOLON		= r';'
t_OR 			= r'\|\|'
t_AND			= r'&&'
t_EXPLAMATION	= r'!'
t_INTERROGATION = r'\?'
t_COLON 		= r':'


t_PLUSPLUS		= r'=='
t_DIFF			= r'!='
t_MENOR			= r'<'
t_MAIOR			= r'>'
t_MENOREQUALS	= r'<='
t_MAIOREQUALS 	= r'>='

t_SUMEQUALS		= r'\+='
t_MINUSEQUALS	= r'-='
t_TIMESEQUALS 	= r'\*='
t_DIVIDEEQUALS	= r'/='
t_MOD			= r'%='



t_PLUS   		= r'\+'
t_MINUS			= r'-'
t_TIMES			= r'\*'
t_DIVIDE		= r'/'
t_EQUALS		= r'='

t_ASPAS			= r'\"'




'''
t_BOOL 		= r'bool'
t_BREAK		= r'break'
t_FOR		= r'for'
t_FALSE		= r'false'
t_IF		= r'if'
t_INT		= r'int'
t_RETURN	= r'return'
t_STRING	= r'string'
t_TRUE		= r'true'
t_VOID		= r'void'
t_WHILE		= r'while'
t_PROCEDURE	= r'proc'	
t_FUNCTION	= r'func'
'''



def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'NAME')    # Check for reserved words
    return t

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_COMMENT_MONOLINE(t):
    r'//.*'
    pass
    # No return value. Token discarded

def t_ccode_comment(t):
    r'(/\*(.|\n)*?\*/)|(//.*)'
    pass



lex.lex()


'''if len(sys.argv) == 2:
    lex.input(open(sys.argv[1]).read())


while  True:
	tok = lex.token()
	if not tok: break

	print (tok)
	print ("\n")'''