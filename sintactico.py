import ply.yacc as yacc

from lexico import tokens

sinresult = ""

precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE')
    )

def p_cuerpo(p):
    '''cuerpo : expression
             | impresion
             | asignacion
             | leer
             | funcionstruct
             | estructurasControl
             | operaciones
             | cuerpo NEWLINE cuerpo'''
    global sinresult
    p[0] = sinresult
   

def p_impresion(p):
    '''impresion : PUTS factor
                    | PUTS comparacion
                    | PUTS comparacion_bool
                    | PUTS STRING
                    | PUTS variables'''
    global sinresult
    sinresult += "\n Imprimir"


def p_leer(p):
    'leer : PUTS STRING NEWLINE variables EQUAL GETS PUNTO CHOMP'
    global sinresult
    sinresult += "\n Leer"

def p_expression_mat(p):
    'expression : factor operadoresMat factor'
    global sinresult
    sinresult += "\n Operaciones Numeros"

def p_operacionstring(p):
    '''operacionstring : STRING PLUS STRING
                     | STRING TIMES INT
                     | STRING PLUS operacionstring'''
    global sinresult
    sinresult += "\n Operaciones con STRING"
def p_operaciones(p):
    '''operaciones : operacionstring
                    | comparacion_bool
                    | comparacionb
                    | comparacion'''


def p_comparacioon(p):
   '''comparacioon : factor operadoresComp factor
                | factor operadoresEquals factor
                | STRING operadoresEquals STRING'''
   global sinresult
   sinresult += "\n Comparacion STRING o NUMEROS"

def p_comparacion(p):
    '''comparacion : comparacioon
                   | comparacioon operadoresBool comparacion '''

def p_comparacion_bool(p):
    'comparacion_bool : booleanos operadoresEquals booleanos'
    global sinresult
    sinresult+="\n Comparacion BOOLEAN"

def p_comparacionb(p):
     '''comparacionb : booleanos operadoresBool booleanos
                           | booleanos operadoresBool comparacionb'''
     global sinresult
     sinresult += "\n Comparacion BOOLEAN"

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
            | FLOAT'''

def p_factor_expr(p):
    'factor : expression'

def p_booleanos(p):
    '''booleanos : TRUE
        | FALSE
    '''

def p_operadoresBool(p):
    '''operadoresBool : AND
                        | OR'''
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
                  | variables EQUAL struct
                  | variables EQUAL operaciones'''

    global sinresult
    sinresult += "\n Asignacion"

#AQUI PUEDEN DEFINIR LAS DEMAS ESTRUCTURAS
def p_struct(p):
    '''struct : conjunto
                | formacion
                | hash'''

def p_conjunto(p):
    '''conjunto : SET arr
                | SET LCOR RCOR'''
    global sinresult
    sinresult += "\n Set"

def p_valor(p):
    '''valor : INT
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
    '''funcionsconjunto : conjunto PUNTO ADD LPAREN valor RPAREN
                        | conjunto PUNTO ADD LPAREN arr RPAREN
                        | conjunto PUNTO MERGE LPAREN conjunto RPAREN
                        | conjunto PUNTO SIZE LPAREN RPAREN
                        | conjunto PUNTO SIZE'''
    global sinresult
    sinresult += "\n Función de Set"

def p_contenido(p):
    '''contenido : impresion
                 | asignacion
                 | funcionstruct'''

def p_repetircontenido(p):
    '''repetircontenido : contenido
                         | contenido SEMICOLON repetircontenido'''

def p_condicion(p):
    '''condicion : comparacion
                | comparacion_bool
                | comparacionb
                | booleanos'''

def p_sentenciafor(p):
    '''sentenciafor : FOR variables IN LPAREN INT PUNTO PUNTO INT RPAREN NEWLINE repetircontenido NEWLINE END
                    | FOR variables IN LPAREN INT PUNTO PUNTO INT RPAREN NEWLINE sentenciaif NEWLINE END
                    | FOR variables IN LPAREN INT PUNTO PUNTO INT RPAREN NEWLINE sentenciaif NEWLINE repetircontenido NEWLINE END'''
    global sinresult
    sinresult += "\n Sentencia for"

def p_sentenciaif(p):
    '''sentenciaif : IF condicion NEWLINE repetircontenido NEWLINE END
                   | IF condicion NEWLINE repetircontenido NEWLINE sentenciaelsif'''
    global sinresult
    sinresult += "\n Sentencia if"

def p_sentenciaelsif(p):
    '''sentenciaelsif : ELSIF condicion NEWLINE repetircontenido NEWLINE END
                      | ELSIF condicion NEWLINE repetircontenido NEWLINE sentenciaelsif'''
    global sinresult
    sinresult += "\n Sentencia elsif"


def p_sentenciawhile(p):
    '''sentenciawhile : WHILE condicion NEWLINE repetircontenido NEWLINE END
                      | WHILE condicion NEWLINE sentenciaif NEWLINE END'''
    global sinresult
    sinresult += "\n Sentencia while"

def p_estructurasControl(p):
    '''estructurasControl : sentenciaif
                           | sentenciawhile
                           | sentenciafor'''

def p_formacion(p):
    '''formacion : LCOR repetirvalor RCOR
                | LCOR RCOR
                | ARRAY PUNTO NEW LPAREN INT RPAREN
                | ARRAY PUNTO NEW LPAREN  RPAREN'''
    global sinresult
    sinresult += "\n Array"

def p_funcionsformacion(p):
    '''funcionsformacion : formacion PUNTO LENGTH LPAREN RPAREN
                        | formacion PUNTO PUSH LPAREN repetirvalor RPAREN
                        | formacion PUNTO SAMPLE LPAREN RPAREN
                        | formacion PUNTO SAMPLE LPAREN INT RPAREN
                        | formacion PUNTO FIRST
                        | formacion PUNTO FIRST LPAREN RPAREN'''
    global sinresult
    sinresult += "\n Funcion de Array"

def p_hash(p):
    'hash : LBRACE hash_content RBRACE'
    global sinresult
    sinresult += "\n hash"

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
    '''clave : STRING
            | INT
            | FLOAT'''
def p_value(p):
    '''value : valor
            | struct'''

def p_hash_store(p):
    'hash_add : hash PUNTO STORE LPAREN clave COMMA value RPAREN'

def p_hash_delete(p):
    'hash_delete : hash PUNTO DELETE LPAREN clave RPAREN'

def p_hash_key(p):
    'hash_key : hash PUNTO KEY LPAREN value RPAREN'

def p_funcionsHash(p):
    '''funcionsHash : hash_add
                    | hash_delete
                    | hash_key'''

    global sinresult
    sinresult += "\n Función de Hash"

# Error rule for syntax errors
def p_error(p):
    global sinresult
    if p:
        print("Syntax error at token %s" %  p.value)
        sinresult += "\n Syntax error at token " + p.value
        # Just discard the token and tell the parser it's okay.
    else:
        sinresult += "\n Syntax error at EOF"
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

'''while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)'''