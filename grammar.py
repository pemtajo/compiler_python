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
    '''sequence_literal : literal sequence_literal
                        | literal'''

def p_define_type(p):
    '''type : INT
            | STRING
            | BOOL'''

def p_variavel(t):
    '''variavel : NAME
                | NAME LCOLC expression RCOLC'''

###############################################################
#errors


def p_var_declaration_error(p):
    '''var_Declaration : type error end'''
    errors.VarDecError(p)

def p_var_declaration_error2(p):
    '''var_Declaration : type var_Especification'''
    errors.NoSemicolonError(p)

def p_var_declaration_error3(p):
    '''var_Declaration : empty var_Especification end'''
    errors.NoTypeError(p)

def p_error(t):
    errors.unknownError(t)


#################################################################

def p_program(t):
    'program : sequence_declaration'

def p_declaration(p):
    '''declaration : var_Declaration
                    | procedure
                    | function'''

def p_sequence_declaration(t):
    '''sequence_declaration : declaration sequence_declaration
                            | declaration'''

def p_var_declaration(p):
    '''var_Declaration : type var_Especification end'''

def p_list_var_declaration(p):
    '''list_var_Declaration : var_Declaration list_var_Declaration
                            | empty'''

def p_var_especification(p):
    '''var_Especification : NAME LCOLC NUMBER RCOLC
                            | NAME ASSIGN literal
                            | NAME
                            | NAME LCOLC NUMBER RCOLC ASSIGN LBRACE sequence_literal RBRACE'''

###############################################################


def p_define_parametro(p):
    '''parametro : type NAME
                | type NAME LCOLC RCOLC'''

def p_list_parametro(t):
    '''list_parametro : sequence_parametro
                      | empty'''

def p_sequence_parametro(t):
    '''sequence_parametro : parametro COMMA sequence_parametro
                          | parametro'''



def p_procedure(t):
    '''procedure : NAME LPAREN list_parametro RPAREN LBRACE block RBRACE'''
    errors.print_all("Procedure")

def p_function(t):
    '''function : type NAME LPAREN list_parametro RPAREN LBRACE block RBRACE'''
    errors.print_all("function")

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
    t[0] = t[1]

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



#see later
'''def p_true(t):
    'bool : TRUE'
    t[0] = "true"

def p_false(t):
    'bool : FALSE'
    t[0] = "false"'''





def p_assign(p):
    '''assignment :   variavel ASSIGN expression
                  |   variavel MOD expression
                  |   variavel SUMEQUALS expression
                  |   variavel MINUSEQUALS expression
                  |   variavel TIMESEQUALS expression
                  |   variavel DIVIDEEQUALS expression
    '''
    if   p[2] ==  '=':
        p[1] = p[3]
    elif p[2] == '%=':
        p[1] = p[1]/p[3]
    elif p[2] == '+=':
        p[1] = p[1]+p[3]
    elif p[2] == '-=':
        p[1] = p[1]-p[3]
    elif p[2] == '*=':
        p[1] = p[1]*p[3]
    elif p[2] == '/=':
        p[1] = p[1]/p[3]
    else: errors.unknownSignal(t)


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


def p_list_statement(t):
    '''list_statement : statement list_statement
                        | empty'''

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

################################################################################
#I/O
def p_statement_write(t):
    '''write_statement : WRITE LPAREN expression RPAREN'''
    print (t[3])


def p_statement_read(t):
    '''read_statement : READ LPAREN variavel RPAREN'''
    t[3].value = raw_input();

##############################################################################
#block

def p_block(p):
    '''block : list_var_Declaration list_statement'''



def p_list_expression(t):
    '''list_expression : sequence_expression
                        | empty'''

def p_sequence_expression(t):
    '''sequence_expression : expression COMMA list_expression
                            | expression'''







parser=yacc.yacc(start='program', debug=True)  #build the parser

arquive = open(filename).read()

parser.parse(arquive)
