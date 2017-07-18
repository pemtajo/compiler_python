#!/usr/bin/python
import sys
sys.path.append("../..")

import ply.yacc as yacc
import errors

from mylexer import tokens





if len(sys.argv) < 2:
    print ("usage : grammar.py [-nocode] inputfile")
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


############################################################################


############################################################################

# Parsing rules


precedence = (
    ('left','LPAREN','RPAREN'),
    ('left','AND','OR'),
    ('left','MAIOR','MENOR', 'MAIOREQUALS', 'MENOREQUALS', 'EQUALS', 'DIFF'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS', 'NOT'),
    )
###############################################################
#expressions
def p_error(t):
    errors.unknownError(t)

def p_define_end_of_instruction(p):
    'end : SEMICOLON'

def p_expression_type(t):
    'expression : type'
    t[0] = t[1]



def p_declaration(p):
    '''declaration : var_Declaration'''

def p_var_declaration(p):
    '''var_Declaration : type var_Especification end'''
###############################################################
#ERROS
def p_var_declaration_error(p):
    '''var_Declaration : type error end'''
    errors.VarDecError(p)

def p_var_declaration_error2(p):
    '''var_Declaration : type var_Especification'''
    errors.NoSemicolonError(p)


###############################################################
def p_var_especification(p):
    '''var_Especification : NAME LCOLC NUMBER RCOLC
                            | NAME ASSIGN expression
                            | NAME '''
                #| NAME LCOLC NUMBER RCOLC  ASSIGN LBRACE <literalSeq> RBRACE





###############################################################



def p_expression_logop(t):
    '''expression : expression MAIOR expression
                  | expression MENOR expression
                  | expression MAIOREQUALS expression
                  | expression MENOREQUALS expression
                  | expression EQUALS expression
                  | expression DIFF expression
                  | expression AND expression
                  | expression OR expression'''
    if t[2] == '>'  : t[0] = t[1] > t[3]
    elif t[2] == '<': t[0] = t[1] < t[3]
    elif t[2] == '>=': t[0] = t[1] >= t[3]
    elif t[2] == '<=': t[0] = t[1] <= t[3]
    elif t[2] == '==': t[0] = t[1] == t[3]
    elif t[2] == '!=': t[0] = t[1] != t[3]
    elif t[2] == '&&': t[0] = t[1] and t[3]
    elif t[2] == '||': t[0] = t[1] or t[3]
    else: errors.unknownSignal(t)




def p_define_type(p):
    '''type : INT
            | STRING
            | BOOL'''


def p_define_parametro(p):
    '''parametro : type NAME
                | type NAME LCOLC RCOLC'''
    p[0] = p[1]





def p_binary_operators(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    else: errors.unknownSignal(t)

def p_ternary(p):
    '''expression : expression INTERROGATION expression COLON expression
    '''

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]

def p_expression_not(p):
    'expression : EXPLAMATION expression %prec NOT'
    p[0] =  not p[2]

def p_expression(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

#see later
'''def p_true(t):
    'bool : TRUE'
    t[0] = "true"

def p_false(t):
    'bool : FALSE'
    t[0] = "false"'''





def p_assign(p):
    '''assignment :   NAME ASSIGN expression
                  |   NAME MOD expression
                  |   NAME SUMEQUALS expression
                  |   NAME MINUSEQUALS expression
                  |   NAME TIMESEQUALS expression
                  |   NAME DIVIDEEQUALS expression
    '''
    if   p[2] ==  '=':
        vars[p[1]] = p[3]
    elif p[2] == '%=':
        vars[p[1]] = p[1]/p[3]
    elif p[2] == '+=':
        vars[p[1]] = p[1]+p[3]
    elif p[2] == '-=':
        vars[p[1]] = p[1]-p[3]
    elif p[2] == '*=':
        vars[p[1]] = p[1]*p[3]
    elif p[2] == '/=':
        vars[p[1]] = p[1]/p[3]
    else: errors.unknownSignal(t)

#    vars[p[1]] = p[3]
#    p[0] = ('ASSIGN',p[1],p[3])

#def p_expression_name(t):
#    'expression : NAME'
    '''try:
        #t[0] = names[t[1]]
    except LookupError:
        print("Undefined name '%s'" % t[1])
        t[0] = 0'''

#########################################################################
#statements
'''<stmt> =>
        | <readStmt>
        | <writeStmt>'''

def p_statement_assign(t):
    '''statement    : if_statement
                    | while_statement
                    | for_statement
                    | break_statement
                    | return_statement
                    | assignment end
                    | subCall_statement end
    '''




def p_statement_if(t):
    '''if_statement : IF LPAREN expression RPAREN LBRACE block RBRACE
                | IF LPAREN expression RPAREN LBRACE block RBRACE ELSE LBRACE block RBRACE'''

def p_statement_while(t):
    'while_statement : WHILE LPAREN expression RPAREN LBRACE block RBRACE'

def p_statement_for(t):
    'for_statement  :  FOR LPAREN assignment SEMICOLON expression SEMICOLON assignment RPAREN LBRACE block RBRACE'


def p_statement_break(t):
    'break_statement    :   BREAK end'

def p_statement_return(t):
    '''return_statement : RETURN end
                        | RETURN expression end'''

def p_statement_subCall(t):
    '''subCall_statement : NAME LPAREN RPAREN'''


def p_variavel(t):
    '''variavel : NAME
                | NAME LCOLC expression RCOLC'''



##############################################################################
#block

def p_block(p):
    '''block : statement block
            | statement'''

parser=yacc.yacc()  #build the parser


print(parser.parse(open(filename).read()))
