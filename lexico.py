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
    'do':'DO','else':'ELSE',
    'elsif':'ELSIF','end':'END',
    'ensure':'ENSURE','false':'FALSE',
    'for':'FOR','if':'IF',
    'in':'IN','module':'MODULE',
    'next':'NEXT','nil':'NIL',
    'not':'NOT','or':'OR',
    'redo':'REDO','rescue':'RESCUE',
    'retry':'RETRY','return':'RETURN',
    'self':'SELF','super':'SUPER',
    'then':'THEN','true':'TRUE',
    'undef':'UNDEF','unless':'UNLESS',
    'until':'UNTIL','when':'WHEN',
    'while':'WHILE','yield':'YIELD'
}

tokens = (
    'NUMBER',
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
    'IGUAL',
    'COMMA',
    'PUNTO',
    'FLECHA'
    'ID',
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

def t_ID(t):
    r'[a-z_][a-z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

