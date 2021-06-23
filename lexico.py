import ply.lex as lex

reserved = {
    'if' : 'IF',
    'elsif' : 'ELSIF',
    'else' : 'ELSE',
    'for' : 'FOR',
    'puts': 'PUTS',
    'Begin':'BEGIN',
    'end':'END',
    'alias':'ALIAS',
    'and':'AND',
    'break':'BREAK',
    'case':'CASE',
    'class':'CLASS',
    'def':'DEF',
    'defined':'DEFINED',
    'do':'DO',
    'ensure':'ENSURE','false':'FALSE',
    'in':'IN','module':'MODULE',
    'next':'NEXT','nil':'NIL',
    'not':'NOT','or':'OR',
    'redo':'REDO','rescue':'RESCUE',
    'retry':'RETRY','return':'RETURN',
    'self':'SELF','super':'SUPER',
    'then':'THEN','true':'TRUE',
    'undef':'UNDEF','unless':'UNLESS',
    'until':'UNTIL','when':'WHEN',
    'while':'WHILE','yield':'YIELD',
    'gets':'GETS',
    'chomp':'CHOMP',
    'length':'LENGTH',
    'sample':'SAMPLE',
    'first':'FIRST',
    'add':'ADD',
    'merge':'MERGE',
    'size':'SIZE',
    'clear':'CLEAR',
    'fetch':'FETCH',
    'delete':'DELETE'
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
    'NUMERAL',
    'COMMA',
    'PUNTO',
    'FLECHA',
    'MOD',
    'EQUAL',
    'ID',
    'NEWLINE'
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
t_EQUAL = r'='
t_COMMA = r','
t_PUNTO = r'\.'
t_FLECHA = r'=>'
t_NUMERAL = r'\#'
t_ignore = ' \t'

def t_ID(t):
    r'[a-z_][a-z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

def t_STRING(t):
    r'(\'[a-zA-Z0-9_+\*\- :,]*\')|(\"[a-zA-Z0-9_+\*\- :,]*\")'
    t.type = reserved.get(t.value,'STRING')    # Check for reserved words
    return t

def t_error(t):
    print("illegal character '%s'" %t.value[0])
    t.lexer.skip(1)

def getTokens(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
# Build the lexer
lexer = lex.lex()
linea=" "
while linea!="":
    linea=input(">>")
    lexer.input(linea)
    getTokens(lexer)
# Tokenize
print("Succesfull")
