#!/usr/bin/python
import sys
sys.path.append("../..")

import ply.yacc as yacc
import errors
import declarations
from declarations import *
from mylexer import tokens
import mylexer

if "cmm" not in sys.argv[0]:
    print ("usage : cmm inputfile")
    raise SystemExit

############################################################################

escopo = Escopo()


############################################################################

# Parsing rules
precedence = (
    ('left','LPAREN','RPAREN'),
    ('left','AND','OR'),
    ('left','MAIOR','MENOR', 'MAIOREQUALS', 'MENOREQUALS', 'EQUALS', 'DIFF'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS', 'NOT', 'TERNARY'),
    )




#################################################################
#define
def p_empty(p):
    'empty :'
    pass

def p_define_end_of_instruction(p):
    'end : SEMICOLON'


def p_literal(t):
    '''literal : NUMBER
                | TRUE
                | FALSE
                | NORMALSTRING
                '''
    t[0]=t[1]

def p_sequence_literal(t):
    '''sequence_literal : literal COMMA sequence_literal
                        | literal'''


def p_define_type(t):
    '''type : INT
            | STRING
            | BOOL'''
    t[0]=t[1]

def p_variavel(t):
    '''variavel : NAME
                | NAME LCOLC expression RCOLC'''
    t[0] = t[1]

#################################################################
# sequence = (example)+
# list = (example)*
#
#################################################################

def p_program(t):
    'program : sequence_declaration'

def p_sequence_declaration(t):
    '''sequence_declaration : declaration sequence_declaration
                            | declaration'''

def p_declaration(t):
    '''declaration  : procedure
                    | function
                    | var_Declaration
                    '''
    t[0]=t[1]

def p_var_declaration(t):
    '''var_Declaration : type sequence_var_Especification end'''
    escopo.addVariable(t[2][0], t[1], t[2][1])
    t[0]=[t[1], t[2]]

def p_list_var_declaration(p):
    '''list_var_Declaration : var_Declaration list_var_Declaration
                            | empty'''

def p_var_especification(t):
    '''var_Especification   : NAME LCOLC NUMBER RCOLC
                            | NAME ASSIGN expression
                            | NAME
                            | NAME LCOLC NUMBER RCOLC ASSIGN LBRACE sequence_literal RBRACE'''

    if(len(t)==2):
        t[0]=[t[1], None]
    elif(len(t)==4):
        t[0]=[t[1], t[3]]


def p_sequence_var_Especification(t):
    '''sequence_var_Especification  : var_Especification COMMA sequence_var_Especification
                                    | var_Especification
    '''
    if len(t)<4:
         t[0] = t[1]
    else:
        t[0]=t[0]+t[1]

###############################################################


def p_define_parametro(t):
    '''parametro    : type NAME
                    | type NAME LCOLC RCOLC'''
    tmp={}
    tmp[t[2]]=Variable(t[2], t[1], None)
    t[0]= tmp


def p_list_parametro(t):
    '''list_parametro : sequence_parametro
                      | empty'''
    t[0]=t[1]

def p_sequence_parametro(t):
    '''sequence_parametro : parametro COMMA sequence_parametro
                          | parametro'''
    if(len(t)>2):
        t[0]=[t[1], t[3]]
    else:
        t[0]=t[1]

def p_procedure(t):
    '''procedure : NAME LPAREN list_parametro RPAREN LBRACE block RBRACE'''
    escopo.addProcedure(t[1], t[3])
    t[0]=[t[1], t[4]]

def p_function(t):
    '''function : type NAME LPAREN list_parametro RPAREN LBRACE block RBRACE'''
    escopo.addFunction(t[2], t[1], t[4])
    t[0]=[t[1], t[2], t[4]]
################################################################################
#expression

def p_ternary(p):
    '''expression : expression INTERROGATION expression COLON expression %prec TERNARY
    '''
    p[0] = p[3] if p[1] else p[5]

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]

def p_expression_not(p):
    'expression : EXPLAMATION expression %prec NOT'
    p[0] =  not p[2]

def p_expression(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_define_expression_literal(t):
    'expression : literal'
    t[0]=t[1]

def p_define_expression_var(t):
    'expression : variavel'
    t[0]=escopo.show(t[1])

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

def p_define_expression_subcall(t):
    'expression : subCall_statement end'
    t[0]=t[1]

def p_list_expression(t):
    '''list_expression : sequence_expression
                        | empty'''
    t[0]=t[1]

def p_sequence_expression(t):
    '''sequence_expression : expression COMMA sequence_expression
                            | expression'''
    t[0]= [t[1], t[3]] if (len(t)>2) else t[1]

def p_assign(p):
    '''assignment :   variavel ASSIGN expression
                  |   variavel MOD expression
                  |   variavel SUMEQUALS expression
                  |   variavel MINUSEQUALS expression
                  |   variavel TIMESEQUALS expression
                  |   variavel DIVIDEEQUALS expression
    '''

    if  p[2] ==  '=':
        escopo.change(p[1], p[3])
    elif p[2] == '%=':
        escopo.change(p[1], escopo.show(p[1]) /p[3])
    elif p[2] == '+=':
        escopo.change(p[1], escopo.show(p[1]) +p[3])
    elif p[2] == '-=':
        escopo.change(p[1], escopo.show(p[1])-p[3])
    elif p[2] == '*=':
        escopo.change(p[1], escopo.show(p[1]) *p[3])
    elif p[2] == '/=':
        escopo.change(p[1], escopo.show(p[1])/p[3])
    else: errors.unknownSignal(t)
    p[0]=escopo.show(p[1])

#########################################################################
#statements


def p_statement(t):
    '''statement    : if_statement
                    | while_statement
                    | for_statement
                    | break_statement
                    | return_statement
                    | assignment end
                    | subCall_statement end
                    | write_statement end
                    | read_statement end
    '''
    t[0]=t[1]

def p_list_statement(t):
    '''list_statement : statement list_statement
                        | empty'''

def p_statement_if(t):
    '''if_statement : IF LPAREN expression RPAREN LBRACE block RBRACE
                    | IF LPAREN expression RPAREN LBRACE block RBRACE ELSE LBRACE block RBRACE'''


    if(t[3]):
        t[0]=t[6]
    else:
        if(len(t)>10): #with else
            t[0]=t[10]

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
    '''subCall_statement : NAME LPAREN list_expression RPAREN'''

################################################################################
#I/O
def p_statement_write(t):
    '''write_statement : WRITE  list_expression '''
    print (t[3])


def p_statement_read(t):
    '''read_statement : READ variavel '''
    t[3].value = raw_input();

##############################################################################
#block

def p_block(t):
    '''block : list_var_Declaration list_statement'''
    t[0]=[t[1], t[2]]

###############################################################
#errors


'''def p_var_declaration_error(p):
    'var_Declaration : type error end'
    errors.VarDecError(p)

def p_var_declaration_error2(p):
    'var_Declaration : type var_Especification'
    errors.NoSemicolonError(p)

def p_var_declaration_error3(p):
    'var_Declaration : empty var_Especification end'
    errors.NoTypeError(p)'''

def p_error(t):
    parser.errok()
    errors.unknownError(t)


parser=yacc.yacc(start='program')  #build the parser
