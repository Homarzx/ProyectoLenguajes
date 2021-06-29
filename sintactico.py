import ply.yacc as yacc

from lexico import tokens

def p_cuerpo(p):
    """cuerpo : expression
             | impresion
             | asignacion
             | leer
             | funcionstruct
             | sentenciafor"""
def p_impresion(p):
    '''impresion : PUTS factor
                    | PUTS comparacion
                    | PUTS comparacion_bool
                    | PUTS STRING'''

def p_leer(p):
    'leer : GETS PUNTO CHOMP'

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
            | FLOAT'''

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


def p_asignacion(p):
    '''asignacion : variables EQUAL factor
                  | variables EQUAL STRING
                  | variables EQUAL booleanos
                  | variables EQUAL comparacion_bool
                  | variables EQUAL struct'''

#AQUI PUEDEN DEFINIR LAS DEMAS ESTRUCTURAS
def p_struct(p):
    'struct : conjunto'

def p_conjunto(p):
    '''conjunto : SET arr
                | SET LCOR RCOR'''

def p_valor(p):
    '''valor : INT
             | ID
             | STRING
             | booleanos
             | FLOAT'''

def p_repetirvalor(p):
    '''repetirvalor : valor
                    | valor COMMA repetirvalor'''

#Sirve para que me de un arreglo [1,"hola",34.5]
def p_arr(p):
    'arr : LCOR repetirvalor RCOR'

def p_funcionstruct(p):
    'funcionstruct : funcionsconjunto'

def p_funcionsconjunto(p):
    '''funcionsconjunto : variables PUNTO ADD LPAREN valor RPAREN
                        | variables PUNTO ADD LPAREN arr RPAREN
                        | variables PUNTO MERGE LPAREN variables RPAREN
                        | variables PUNTO SIZE LPAREN RPAREN
                        | variables PUNTO SIZE'''

def p_contenido(p):
    '''contenido : impresion
                 | asignacion
                 | funcionstruct'''
def p_repetircontenido(p):
    '''repetircontenido : contenido
                        | contenido repetircontenido'''

def p_sentenciafor(p):
    'sentenciafor : FOR variables IN LPAREN INT PUNTO PUNTO INT RPAREN repetircontenido END'


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