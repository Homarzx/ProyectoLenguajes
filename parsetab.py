
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD ALIAS AND BEGIN BREAK CASE CHOMP CLASS CLEAR COMMA CONSTANT DEF DEFINED DELETE DIVIDE DO ELSE ELSIF END ENSURE EQUAL EQUALSX2 FALSE FETCH FIRST FLECHA FLOAT FOR GETS GLOBAL ID IF IN INT LBRACE LCOR LENGTH LPAREN MAYORQUE MENORQUE MERGE MINUS MOD MODULE NEWLINE NEXT NIL NOT NOTEQUALS NUMERAL OR PLUS PUNTO PUTS RBRACE RCOR REDO RESCUE RETRY RETURN RPAREN SAMPLE SELF SET SIZE STRING SUPER THEN TIMES TRUE UNDEF UNLESS UNTIL WHEN WHILE YIELDcuerpo : expression\n             | impresion\n             | asignacion\n             | funcionstructimpresion : PUTS factor\n                    | PUTS comparacion\n                    | PUTS comparacion_bool\n                    | PUTS STRINGexpression : factor operadoresMat factorcomparacion : factor operadoresComp factorcomparacion_bool : booleanos operadoresBool booleanosoperadoresComp : MAYORQUE\n                    | MENORQUE\n                    | operadoresEqualsoperadoresMat : PLUS\n                    | MINUS\n                    | TIMES\n                    | DIVIDE\n                    | MODfactor : INT\n            | variables\n            | FLOATfactor : expressionbooleanos : TRUE\n        | FALSE\n    operadoresBool : AND\n                        | OR\n                        | operadoresEqualsoperadoresEquals : EQUALSX2\n                        | NOTEQUALSvariables : ID\n                | CONSTANT\n                | GLOBALasignacion : variables EQUAL factor\n                  | variables EQUAL STRING\n                  | variables EQUAL booleanos\n                  | variables EQUAL comparacion_bool\n                  | variables EQUAL structstruct : conjuntoconjunto : SET arr\n                | SET LCOR RCORvalor : INT\n             | ID\n             | STRING\n             | booleanos\n             | FLOATrepetirvalor : valor\n                    | valor COMMA repetirvalorarr : LCOR repetirvalor RCORfuncionstruct : funcionsconjuntofuncionsconjunto : variables PUNTO ADD LPAREN valor RPAREN\n                        | variables PUNTO ADD LPAREN arr RPAREN\n                        | variables PUNTO MERGE LPAREN variables RPAREN\n                        | variables PUNTO SIZE LPAREN RPAREN\n                        | variables PUNTO SIZE'
    
_lr_action_items = {'PUTS':([0,],[7,]),'INT':([0,7,15,16,17,18,19,20,30,33,34,35,36,37,38,56,57,70,74,],[10,10,10,-15,-16,-17,-18,-19,10,10,-12,-13,-14,-29,-30,63,63,63,63,]),'FLOAT':([0,7,15,16,17,18,19,20,30,33,34,35,36,37,38,56,57,70,74,],[11,11,11,-15,-16,-17,-18,-19,11,11,-12,-13,-14,-29,-30,67,67,67,67,]),'ID':([0,7,15,16,17,18,19,20,30,33,34,35,36,37,38,56,57,58,70,74,],[12,12,12,-15,-16,-17,-18,-19,12,12,-12,-13,-14,-29,-30,64,64,12,64,64,]),'CONSTANT':([0,7,15,16,17,18,19,20,30,33,34,35,36,37,38,58,],[13,13,13,-15,-16,-17,-18,-19,13,13,-12,-13,-14,-29,-30,13,]),'GLOBAL':([0,7,15,16,17,18,19,20,30,33,34,35,36,37,38,58,],[14,14,14,-15,-16,-17,-18,-19,14,14,-12,-13,-14,-29,-30,14,]),'$end':([1,2,3,4,5,9,10,11,12,13,14,21,22,23,24,25,26,28,29,32,43,44,45,46,47,48,52,53,54,55,60,72,73,75,76,77,],[0,-1,-2,-3,-4,-50,-20,-22,-31,-32,-33,-5,-6,-7,-8,-21,-23,-24,-25,-9,-34,-35,-36,-37,-38,-39,-55,-10,-11,-40,-41,-54,-49,-51,-52,-53,]),'PLUS':([2,6,8,10,11,12,13,14,21,25,26,32,43,53,],[-23,16,-21,-20,-22,-31,-32,-33,16,-21,-23,16,16,16,]),'MINUS':([2,6,8,10,11,12,13,14,21,25,26,32,43,53,],[-23,17,-21,-20,-22,-31,-32,-33,17,-21,-23,17,17,17,]),'TIMES':([2,6,8,10,11,12,13,14,21,25,26,32,43,53,],[-23,18,-21,-20,-22,-31,-32,-33,18,-21,-23,18,18,18,]),'DIVIDE':([2,6,8,10,11,12,13,14,21,25,26,32,43,53,],[-23,19,-21,-20,-22,-31,-32,-33,19,-21,-23,19,19,19,]),'MOD':([2,6,8,10,11,12,13,14,21,25,26,32,43,53,],[-23,20,-21,-20,-22,-31,-32,-33,20,-21,-23,20,20,20,]),'STRING':([7,30,56,57,70,74,],[24,44,65,65,65,65,]),'TRUE':([7,30,37,38,39,40,41,42,56,57,70,74,],[28,28,-29,-30,28,-26,-27,-28,28,28,28,28,]),'FALSE':([7,30,37,38,39,40,41,42,56,57,70,74,],[29,29,-29,-30,29,-26,-27,-28,29,29,29,29,]),'EQUAL':([8,12,13,14,],[30,-31,-32,-33,]),'PUNTO':([8,12,13,14,],[31,-31,-32,-33,]),'MAYORQUE':([10,11,12,13,14,21,25,26,32,],[-20,-22,-31,-32,-33,34,-21,-23,-9,]),'MENORQUE':([10,11,12,13,14,21,25,26,32,],[-20,-22,-31,-32,-33,35,-21,-23,-9,]),'EQUALSX2':([10,11,12,13,14,21,25,26,27,28,29,32,45,],[-20,-22,-31,-32,-33,37,-21,-23,37,-24,-25,-9,37,]),'NOTEQUALS':([10,11,12,13,14,21,25,26,27,28,29,32,45,],[-20,-22,-31,-32,-33,38,-21,-23,38,-24,-25,-9,38,]),'RPAREN':([12,13,14,28,29,59,63,64,65,66,67,68,69,71,73,],[-31,-32,-33,-24,-25,72,-42,-43,-44,-45,-46,75,76,77,-49,]),'AND':([27,28,29,45,],[40,-24,-25,40,]),'OR':([27,28,29,45,],[41,-24,-25,41,]),'COMMA':([28,29,62,63,64,65,66,67,],[-24,-25,74,-42,-43,-44,-45,-46,]),'RCOR':([28,29,56,61,62,63,64,65,66,67,78,],[-24,-25,60,73,-47,-42,-43,-44,-45,-46,-48,]),'SET':([30,],[49,]),'ADD':([31,],[50,]),'MERGE':([31,],[51,]),'SIZE':([31,],[52,]),'LCOR':([49,57,],[56,70,]),'LPAREN':([50,51,52,],[57,58,59,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'cuerpo':([0,],[1,]),'expression':([0,7,15,30,33,],[2,26,26,26,26,]),'impresion':([0,],[3,]),'asignacion':([0,],[4,]),'funcionstruct':([0,],[5,]),'factor':([0,7,15,30,33,],[6,21,32,43,53,]),'variables':([0,7,15,30,33,58,],[8,25,25,25,25,71,]),'funcionsconjunto':([0,],[9,]),'operadoresMat':([6,21,32,43,53,],[15,15,15,15,15,]),'comparacion':([7,],[22,]),'comparacion_bool':([7,30,],[23,46,]),'booleanos':([7,30,39,56,57,70,74,],[27,45,54,66,66,66,66,]),'operadoresComp':([21,],[33,]),'operadoresEquals':([21,27,45,],[36,42,42,]),'operadoresBool':([27,45,],[39,39,]),'struct':([30,],[47,]),'conjunto':([30,],[48,]),'arr':([49,57,],[55,69,]),'repetirvalor':([56,70,74,],[61,61,78,]),'valor':([56,57,70,74,],[62,68,62,62,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> cuerpo","S'",1,None,None,None),
  ('cuerpo -> expression','cuerpo',1,'p_cuerpo','sintactico.py',6),
  ('cuerpo -> impresion','cuerpo',1,'p_cuerpo','sintactico.py',7),
  ('cuerpo -> asignacion','cuerpo',1,'p_cuerpo','sintactico.py',8),
  ('cuerpo -> funcionstruct','cuerpo',1,'p_cuerpo','sintactico.py',9),
  ('impresion -> PUTS factor','impresion',2,'p_impresion','sintactico.py',11),
  ('impresion -> PUTS comparacion','impresion',2,'p_impresion','sintactico.py',12),
  ('impresion -> PUTS comparacion_bool','impresion',2,'p_impresion','sintactico.py',13),
  ('impresion -> PUTS STRING','impresion',2,'p_impresion','sintactico.py',14),
  ('expression -> factor operadoresMat factor','expression',3,'p_expression_mat','sintactico.py',17),
  ('comparacion -> factor operadoresComp factor','comparacion',3,'p_comparacion','sintactico.py',23),
  ('comparacion_bool -> booleanos operadoresBool booleanos','comparacion_bool',3,'p_comparacion_bool','sintactico.py',26),
  ('operadoresComp -> MAYORQUE','operadoresComp',1,'p_operadoresComp','sintactico.py',29),
  ('operadoresComp -> MENORQUE','operadoresComp',1,'p_operadoresComp','sintactico.py',30),
  ('operadoresComp -> operadoresEquals','operadoresComp',1,'p_operadoresComp','sintactico.py',31),
  ('operadoresMat -> PLUS','operadoresMat',1,'p_operadoresMat','sintactico.py',34),
  ('operadoresMat -> MINUS','operadoresMat',1,'p_operadoresMat','sintactico.py',35),
  ('operadoresMat -> TIMES','operadoresMat',1,'p_operadoresMat','sintactico.py',36),
  ('operadoresMat -> DIVIDE','operadoresMat',1,'p_operadoresMat','sintactico.py',37),
  ('operadoresMat -> MOD','operadoresMat',1,'p_operadoresMat','sintactico.py',38),
  ('factor -> INT','factor',1,'p_factor_num','sintactico.py',41),
  ('factor -> variables','factor',1,'p_factor_num','sintactico.py',42),
  ('factor -> FLOAT','factor',1,'p_factor_num','sintactico.py',43),
  ('factor -> expression','factor',1,'p_factor_expr','sintactico.py',46),
  ('booleanos -> TRUE','booleanos',1,'p_booleanos','sintactico.py',49),
  ('booleanos -> FALSE','booleanos',1,'p_booleanos','sintactico.py',50),
  ('operadoresBool -> AND','operadoresBool',1,'p_operadoresBool','sintactico.py',54),
  ('operadoresBool -> OR','operadoresBool',1,'p_operadoresBool','sintactico.py',55),
  ('operadoresBool -> operadoresEquals','operadoresBool',1,'p_operadoresBool','sintactico.py',56),
  ('operadoresEquals -> EQUALSX2','operadoresEquals',1,'p_operadoresEqual','sintactico.py',58),
  ('operadoresEquals -> NOTEQUALS','operadoresEquals',1,'p_operadoresEqual','sintactico.py',59),
  ('variables -> ID','variables',1,'p_variables','sintactico.py',61),
  ('variables -> CONSTANT','variables',1,'p_variables','sintactico.py',62),
  ('variables -> GLOBAL','variables',1,'p_variables','sintactico.py',63),
  ('asignacion -> variables EQUAL factor','asignacion',3,'p_asignacion','sintactico.py',67),
  ('asignacion -> variables EQUAL STRING','asignacion',3,'p_asignacion','sintactico.py',68),
  ('asignacion -> variables EQUAL booleanos','asignacion',3,'p_asignacion','sintactico.py',69),
  ('asignacion -> variables EQUAL comparacion_bool','asignacion',3,'p_asignacion','sintactico.py',70),
  ('asignacion -> variables EQUAL struct','asignacion',3,'p_asignacion','sintactico.py',71),
  ('struct -> conjunto','struct',1,'p_struct','sintactico.py',75),
  ('conjunto -> SET arr','conjunto',2,'p_conjunto','sintactico.py',78),
  ('conjunto -> SET LCOR RCOR','conjunto',3,'p_conjunto','sintactico.py',79),
  ('valor -> INT','valor',1,'p_valor','sintactico.py',82),
  ('valor -> ID','valor',1,'p_valor','sintactico.py',83),
  ('valor -> STRING','valor',1,'p_valor','sintactico.py',84),
  ('valor -> booleanos','valor',1,'p_valor','sintactico.py',85),
  ('valor -> FLOAT','valor',1,'p_valor','sintactico.py',86),
  ('repetirvalor -> valor','repetirvalor',1,'p_repetirvalor','sintactico.py',89),
  ('repetirvalor -> valor COMMA repetirvalor','repetirvalor',3,'p_repetirvalor','sintactico.py',90),
  ('arr -> LCOR repetirvalor RCOR','arr',3,'p_arr','sintactico.py',94),
  ('funcionstruct -> funcionsconjunto','funcionstruct',1,'p_funcionstruct','sintactico.py',97),
  ('funcionsconjunto -> variables PUNTO ADD LPAREN valor RPAREN','funcionsconjunto',6,'p_funcionsconjunto','sintactico.py',100),
  ('funcionsconjunto -> variables PUNTO ADD LPAREN arr RPAREN','funcionsconjunto',6,'p_funcionsconjunto','sintactico.py',101),
  ('funcionsconjunto -> variables PUNTO MERGE LPAREN variables RPAREN','funcionsconjunto',6,'p_funcionsconjunto','sintactico.py',102),
  ('funcionsconjunto -> variables PUNTO SIZE LPAREN RPAREN','funcionsconjunto',5,'p_funcionsconjunto','sintactico.py',103),
  ('funcionsconjunto -> variables PUNTO SIZE','funcionsconjunto',3,'p_funcionsconjunto','sintactico.py',104),
]
