import ply.yacc as yacc

from lexico import tokens

sinresult = ""

def p_cuerpo(p):
    """cuerpo : expression
             | impresion
             | asignacion
             | leer
             | funcionstruct
             | sentenciafor
             | sentenciawhile
             | sentenciaElsif"""

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
    '''struct : conjunto
                | formacion
                | hash'''

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
    '''funcionstruct : funcionsconjunto
                        | funcionsformacion
                        | funcionsHash'''

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


def p_condicion(p):
    '''condicion : comparacion
                | comparacion_bool
                | booleanos
                | ARRAY PUNTO NEW LPAREN arr RPAREN'''

def p_sentenciawhile(p):
    'sentenciawhile : WHILE condicion  DO repetircontenido END'

def p_formacion(p):
    '''formacion : LCOR repetirvalor RCOR
                | LCOR RCOR
                | ARRAY PUNTO NEW LPAREN INT RPAREN
                | ARRAY PUNTO NEW LPAREN  RPAREN'''

def p_funcionsformacion(p):
    '''funcionsformacion : variables PUNTO LENGTH LPAREN RPAREN
                        | variables PUNTO PUSH LPAREN repetirvalor RPAREN
                        | variables PUNTO SAMPLE LPAREN variables RPAREN
                        | variables PUNTO FIRST
                        | variables PUNTO FIRST LPAREN RPAREN'''

def p_hash(p):
    'hash : LBRACE hash_content RBRACE'

def p_hash_elements(p):
    '''hash_elements : hash_element hash_more_elements'''

def p_hash_content(p):
    '''hash_content : hash_element 
                    | hash_elements'''

def p_hash_element(p):
    'hash_element : clave FLECHA value'

def p_hash_more_elements(p):
    '''hash_more_elements : COMMA hash_element
                            | COMMA hash_element hash_more_elements'''
def p_clave(p):
    '''clave : variables                                                     
            | STRING
            | INT
            | FLOAT'''
def p_value(p):
    '''value : valor
            | struct'''

def p_hash_store(p):
    'hash_add : variables PUNTO STORE LPAREN hash_element RPAREN'

def p_hash_delete(p):
    'hash_delete : variables PUNTO LPAREN clave RPAREN'

def p_hash_key(p):
    'hash_key : variables PUNTO KEY LPAREN value RPAREN'

def p_funcionsHash(p):
    '''funcionsHash : hash_add
                    | hash_delete
                    | hash_key'''
def p_sentenciaElsif(p):
    'sentenciaElsif : IF condicion repetircontenido mas_sentencias END'

def p_mas_sentencias(p):
    '''mas_sentencias : ELSIF repetircontenido 
                        | ELSIF repetircontenido mas_sentencias'''
# Error rule for syntax errors
def p_error(p):
    global sinresult
    if p:
        print("Syntax error at token", p.type)
        sinresult += ("Syntax error at token " + p.type)
        # Just discard the token and tell the parser it's okay.
    else:
        sinresult += ("Syntax error at EOF")
        print("Syntax error at EOF")
# Build the parser

parser = yacc.yacc()
def getSintatic(linea):
    global sinresult
    sinresult = ""
    while True:
        try:
            s = linea
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)

        break
    return sinresult

"""while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)"""