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
             | struct
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

def p_sentenciaif_error(p):
    '''sentenciaif : IF error NEWLINE repetircontenido NEWLINE END
                   | IF error NEWLINE repetircontenido NEWLINE sentenciaelsif'''
    global sinresult
    sinresult += "\n condicion no valida en sentencia if"

def p_expression_mat(p):
    'expression : factor operadoresMat factor'

def p_expression_mat_error_factors(p):
    'expression : factor operadoresMat error'
    global sinresult
    sinresult += " Un numero solo se debe operar con otro"

def p_expression_mat_error(p):
    'expression : factor error factor'
    global sinresult
    sinresult += " Operacion numerica no definida"


def p_comparacion_todo(p):
    '''comparacionTodo : STRING operadoresEquals factor
                        | STRING operadoresEquals STRING
                        | booleanos operadoresEquals STRING
                        | STRING operadoresEquals booleanos
                        | factor operadoresEquals STRING
                        | factor operadoresEquals factor'''

def p_operacionstring(p):
    '''operacionstring : STRING PLUS STRING
                     | STRING TIMES INT
                     | STRING TIMES FLOAT
                     | STRING PLUS operacionstring'''
def p_operacionstring_error(p):
    '''operacionstring : STRING error STRING
                     | STRING error INT
                     | STRING error operacionstring'''
    global sinresult
    sinresult += " Operaciones no definida con STRING"

def p_operacionstring_error_element(p):
    '''operacionstring : STRING PLUS error
                     | STRING TIMES error'''
    global sinresult
    sinresult += " Operaciones no definida con STRING"

def p_operaciones(p):
    '''operaciones : operacionstring
                    | comparacion_bool
                    | comparacionb
                    | comparacion
                    '''




def p_comparacion_numeros(p):
    'comparacioNumeros : factor operadoresComp factor'

def p_comparacion_numeros_error(p):
    'comparacioNumeros : factor operadoresComp error'
    global sinresult
    sinresult += "\n No se puede comparar un tipo de dato numerico con otro tipo de dato"

def p_comparacion(p):
    '''comparacion : comparacioNumeros
                    | comparacionTodo
                    | comparacioNumeros operadoresBool comparacion
                   | comparacionTodo operadoresBool comparacion
                   '''

def p_comparacion_bool(p):
    'comparacion_bool : booleanos operadoresEquals booleanos'


def p_comparacionb(p):
     '''comparacionb : booleanos operadoresBool booleanos
                           | booleanos operadoresBool comparacionb'''
def p_comparacionb_error(p):
    '''comparacionb : booleanos error booleanos
                    | booleanos error comparacionb'''
    global sinresult
    sinresult+=" operacion no definida para BOOLEAN"

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
                | GLOBAL
                | CONSTANT'''

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

def p_parametro(p):
    '''parametros :  variables
                    | valor
                    | variables COMMA parametros
                    | valor COMMA parametros'''


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

def p_sentenciafor_error(p):
    '''sentenciafor : FOR variables IN LPAREN error PUNTO PUNTO error RPAREN NEWLINE repetircontenido NEWLINE END
                    | FOR variables IN LPAREN error PUNTO PUNTO error RPAREN NEWLINE sentenciaif NEWLINE END
                    | FOR variables IN LPAREN error PUNTO PUNTO error RPAREN NEWLINE sentenciaif NEWLINE repetircontenido NEWLINE END'''
    global sinresult
    sinresult += "\n Sentencia for incorrecta, rangos solo entre enteros"


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

def p_sentenciaelsif_error(p):
    '''sentenciaelsif : ELSIF error NEWLINE repetircontenido NEWLINE END
                      | ELSIF error NEWLINE repetircontenido NEWLINE sentenciaelsif'''
    global sinresult
    sinresult += "\n condicion no valida en sentencia elsif"


def p_sentenciawhile(p):
    '''sentenciawhile : WHILE condicion NEWLINE repetircontenido NEWLINE END
                      | WHILE condicion NEWLINE sentenciaif NEWLINE END'''
    global sinresult
    sinresult += "\n Sentencia while"

def p_sentenciawhile_error(p):
    '''sentenciawhile : WHILE error NEWLINE repetircontenido NEWLINE END
                      | WHILE error NEWLINE sentenciaif NEWLINE END'''
    global sinresult
    sinresult += "\n condicion no valida en sentencia while"

def p_sentenciadef(p):
    '''sentenciadef : DEF variables LPAREN parametros RPAREN NEWLINE repetircontenido NEWLINE END
                    | DEF variables LPAREN  RPAREN NEWLINE repetircontenido NEWLINE END'''
    global sinresult
    sinresult += "\n Sentencia def"


def p_estructurasControl(p):
    '''estructurasControl : sentenciaif
                           | sentenciawhile
                           | sentenciafor
                           | sentenciadef
                            '''

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
        print("Error sintactico en token %s" %  p.type)
        sinresult += "\n Error sintactico en token " + str(p.type)
        # Just discard the token and tell the parser it's okay.
    else:
        sinresult += "\n Error sintactico en EOF"
        print("Error sintactico en EOF")
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