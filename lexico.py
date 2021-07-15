import ply.lex as lex

lexresult=""

reserved = {
    'if' : 'IF',
    'elsif' : 'ELSIF',
    'for' : 'FOR',
    'puts': 'PUTS',
    'end':'END',
    'and':'AND',
    'def':'DEF',
    'false':'FALSE',
    'in':'IN','or':'OR',
    'true':'TRUE',
    'while':'WHILE',
    'gets':'GETS',
    'chomp':'CHOMP',
    'length':'LENGTH',
    'sample':'SAMPLE',
    'first':'FIRST',
    'add':'ADD',
    'merge':'MERGE',
    'size':'SIZE',
    'delete':'DELETE',
    'new' : 'NEW',
    'push' : 'PUSH',
    'store' : 'STORE',
    'key' :'KEY'
}

tokens = (
    'INT',
    'FLOAT',
    'STRING',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LCOR',
    'RCOR',
    'MAYORQUE',
    'MENORQUE',
    'EQUALSX2',
    'NOTEQUALS',
    'COMMA',
    'PUNTO',
    'FLECHA',
    'MOD',
    'EQUAL',
    'ID',
    'NEWLINE',
    'SET',
    'ARRAY',
    'CONSTANT',
    'GLOBAL',
    'SEMICOLON',
 ) + tuple(reserved.values())

# Reglas de expresión regular para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_MOD = r'%'
t_LCOR = r'\['
t_RCOR = r'\]'
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_EQUALSX2 = r'=='
t_NOTEQUALS = r'!='
t_EQUAL = r'='
t_COMMA = r','
t_PUNTO = r'\.'
t_FLECHA = r'=>'
t_SEMICOLON = r'\;'
t_ignore = ' \t'


def t_SET (t) :
   r'Set'
   t.type = reserved.get(t.value, 'SET')  # Check for reserved words
   return t

def t_ARRAY (t) :
   r'Array'
   t.type = reserved.get(t.value, 'ARRAY')  # Check for reserved words
   return t


def t_ID(t):
    r'[a-z_][a-z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

def t_CONSTANT(t):
    r'[A-Z][A-Z0-9]*'
    t.type=reserved.get(t.value,'CONSTANT')
    return t

def t_GLOBAL(t):
    r'\$[a-z][a-z0-9_]*'
    t.type=reserved.get(t.value,'GLOBAL')
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

def t_STRING(t):
    r'(\'[a-zA-Z0-9_+\*\- :,]*\')|(\"[a-zA-Z0-9_+\*\- :,]*\")'
    t.type = reserved.get(t.value,'STRING')    # Check for reserved words
    return t

def t_COMMENT(t):
    r'\#.*'
    pass

def t_error(t):
    global lexresult
    print("Caracter Ilegal '%s'" %t.value[0])
    lexresult += "\nCaracter Ilegal " + t.value[0]
    t.lexer.skip(1)

def getTokensLexer(linea):
    global lexresult
    lexresult = ""
    lexer = lex.lex()
    lexer.input(linea)
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
        lexresult += "\n" + str(tok)
    return lexresult


# Build the lexer
lexer = lex.lex()