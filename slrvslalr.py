from ply.lex  import lex
from ply.yacc import yacc

tokens = ('ID','EQ','TIMES')

t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_EQ = r'\='
t_TIMES = r'\*'

lexer = lex()

def p_s(p):
    '''
    s : l EQ r
      | r
    '''

def p_l(p):
    '''
    l : TIMES r
      | ID
    '''

def p_r(p):
    '''
    r : l
    '''

parserLALR = yacc(method='LALR', tabmodule='lalrparse',debugfile='lalrparse.out')
parserLALR = yacc(method='SLR', tabmodule='slrparse',debugfile='slrparse.out')