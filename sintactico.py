import ply.yacc as yacc

from lexico import tokens

def p_cuerpo(p):
    """cuerpo : expression
             | impresion"""
def p_impresion(p):
    '''impresion : PUTS factor
                    | PUTS comparacion
                    | PUTS comparacion_bool
                    | PUTS STRING'''

def p_expression_mat(p):
    'expression : factor operadoresMat factor'




def p_comparacion(p):
    'comparacion : factor operadoresComp factor'

def p_comparacion_bool(p):
    'comparacion_bool : booleanos operadoresBool booleanos'

def p_operadoresComp(p):
    '''operadoresComp : MAYORQUE
                    | MENORQUE
                    | operadoresEquals'''

def p_operadoresMat(p):
    '''operadoresMat : PLUS
                    | MINUS
                    | TIMES
                    | DIVIDE
                    | MOD'''

def p_factor_num(p):
    '''factor : INT
            | variables
            | FLOAT
            | booleanos'''

def p_factor_expr(p):
    'factor : expression'

def p_booleanos(p):
    '''booleanos : TRUE
        | FALSE
    '''
def p_operadoresBool(p):
    '''operadoresBool : AND
                        | OR
                        | operadoresEquals'''
def p_operadoresEqual(p):
    '''operadoresEquals : EQUALSX2
                        | NOTEQUALS'''
def p_variables(p):
    '''variables : ID
                | CONSTANT
                | GLOBAL'''

# Error rule for syntax errors
def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
    else:
        print("Syntax error at EOF")
# Build the parser
parser = yacc.yacc()
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)