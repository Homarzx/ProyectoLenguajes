
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD ALIAS AND BEGIN BREAK CASE CHOMP CLASS CLEAR COMMA CONSTANT DEF DEFINED DELETE DIVIDE DO ELSE ELSIF END ENSURE EQUAL EQUALSX2 FALSE FETCH FIRST FLECHA FLOAT FOR GETS GLOBAL ID IF IN INT LBRACE LCOR LENGTH LPAREN MAYORQUE MENORQUE MERGE MINUS MOD MODULE NEWLINE NEXT NIL NOT NOTEQUALS NUMERAL OR PLUS PUNTO PUTS RBRACE RCOR REDO RESCUE RETRY RETURN RPAREN SAMPLE SELF SET SIZE STRING SUPER THEN TIMES TRUE UNDEF UNLESS UNTIL WHEN WHILE YIELDcuerpo : expression\n             | impresion\n             | asignacion\n             | leer\n             | funcionstruct\n             | sentenciaforimpresion : PUTS factor\n                    | PUTS comparacion\n                    | PUTS comparacion_bool\n                    | PUTS STRINGleer : GETS PUNTO CHOMPexpression : factor operadoresMat factorcomparacion : factor operadoresComp factorcomparacion_bool : booleanos operadoresBool booleanosoperadoresComp : MAYORQUE\n                    | MENORQUE\n                    | operadoresEqualsoperadoresMat : PLUS\n                    | MINUS\n                    | TIMES\n                    | DIVIDE\n                    | MODfactor : INT\n            | variables\n            | FLOATfactor : expressionbooleanos : TRUE\n        | FALSE\n    operadoresBool : AND\n                        | OR\n                        | operadoresEqualsoperadoresEquals : EQUALSX2\n                        | NOTEQUALSvariables : ID\n                | CONSTANT\n                | GLOBALasignacion : variables EQUAL factor\n                  | variables EQUAL STRING\n                  | variables EQUAL booleanos\n                  | variables EQUAL comparacion_bool\n                  | variables EQUAL structstruct : conjuntoconjunto : SET arr\n                | SET LCOR RCORvalor : INT\n             | ID\n             | STRING\n             | booleanos\n             | FLOATrepetirvalor : valor\n                    | valor COMMA repetirvalorarr : LCOR repetirvalor RCORfuncionstruct : funcionsconjuntofuncionsconjunto : variables PUNTO ADD LPAREN valor RPAREN\n                        | variables PUNTO ADD LPAREN arr RPAREN\n                        | variables PUNTO MERGE LPAREN variables RPAREN\n                        | variables PUNTO SIZE LPAREN RPAREN\n                        | variables PUNTO SIZEcontenido : impresion\n                 | asignacion\n                 | funcionstructrepetircontenido : contenido\n                        | contenido repetircontenidosentenciafor : FOR variables IN LPAREN INT PUNTO PUNTO INT RPAREN repetircontenido END'
    
_lr_action_items = {'PUTS':([0,12,14,15,16,17,18,25,26,27,28,29,30,32,33,38,49,50,51,52,53,54,58,61,62,63,69,81,83,85,86,87,92,95,96,97,98,],[9,-53,-23,-25,-34,-35,-36,-7,-8,-9,-10,-24,-26,-27,-28,-12,-37,-38,-39,-40,-41,-42,-58,-13,-14,-43,-44,-57,-52,-54,-55,-56,9,9,-59,-60,-61,]),'GETS':([0,],[11,]),'FOR':([0,],[13,]),'INT':([0,9,19,20,21,22,23,24,34,39,40,41,42,43,44,64,65,68,79,84,90,],[14,14,14,-18,-19,-20,-21,-22,14,14,-15,-16,-17,-32,-33,72,72,82,72,72,91,]),'FLOAT':([0,9,19,20,21,22,23,24,34,39,40,41,42,43,44,64,65,79,84,],[15,15,15,-18,-19,-20,-21,-22,15,15,-15,-16,-17,-32,-33,76,76,76,76,]),'ID':([0,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,38,39,40,41,42,43,44,49,50,51,52,53,54,58,61,62,63,64,65,66,69,79,81,83,84,85,86,87,92,95,96,97,98,],[16,16,-53,16,-23,-25,-34,-35,-36,16,-18,-19,-20,-21,-22,-7,-8,-9,-10,-24,-26,-27,-28,16,-12,16,-15,-16,-17,-32,-33,-37,-38,-39,-40,-41,-42,-58,-13,-14,-43,73,73,16,-44,73,-57,-52,73,-54,-55,-56,16,16,-59,-60,-61,]),'CONSTANT':([0,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,38,39,40,41,42,43,44,49,50,51,52,53,54,58,61,62,63,66,69,81,83,85,86,87,92,95,96,97,98,],[17,17,-53,17,-23,-25,-34,-35,-36,17,-18,-19,-20,-21,-22,-7,-8,-9,-10,-24,-26,-27,-28,17,-12,17,-15,-16,-17,-32,-33,-37,-38,-39,-40,-41,-42,-58,-13,-14,-43,17,-44,-57,-52,-54,-55,-56,17,17,-59,-60,-61,]),'GLOBAL':([0,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,38,39,40,41,42,43,44,49,50,51,52,53,54,58,61,62,63,66,69,81,83,85,86,87,92,95,96,97,98,],[18,18,-53,18,-23,-25,-34,-35,-36,18,-18,-19,-20,-21,-22,-7,-8,-9,-10,-24,-26,-27,-28,18,-12,18,-15,-16,-17,-32,-33,-37,-38,-39,-40,-41,-42,-58,-13,-14,-43,18,-44,-57,-52,-54,-55,-56,18,18,-59,-60,-61,]),'$end':([1,2,3,4,5,6,7,12,14,15,16,17,18,25,26,27,28,29,30,32,33,38,49,50,51,52,53,54,58,59,61,62,63,69,81,83,85,86,87,99,],[0,-1,-2,-3,-4,-5,-6,-53,-23,-25,-34,-35,-36,-7,-8,-9,-10,-24,-26,-27,-28,-12,-37,-38,-39,-40,-41,-42,-58,-11,-13,-14,-43,-44,-57,-52,-54,-55,-56,-64,]),'PLUS':([2,8,10,14,15,16,17,18,25,29,30,38,49,61,],[-26,20,-24,-23,-25,-34,-35,-36,20,-24,-26,20,20,20,]),'MINUS':([2,8,10,14,15,16,17,18,25,29,30,38,49,61,],[-26,21,-24,-23,-25,-34,-35,-36,21,-24,-26,21,21,21,]),'TIMES':([2,8,10,14,15,16,17,18,25,29,30,38,49,61,],[-26,22,-24,-23,-25,-34,-35,-36,22,-24,-26,22,22,22,]),'DIVIDE':([2,8,10,14,15,16,17,18,25,29,30,38,49,61,],[-26,23,-24,-23,-25,-34,-35,-36,23,-24,-26,23,23,23,]),'MOD':([2,8,10,14,15,16,17,18,25,29,30,38,49,61,],[-26,24,-24,-23,-25,-34,-35,-36,24,-24,-26,24,24,24,]),'STRING':([9,34,64,65,79,84,],[28,50,74,74,74,74,]),'TRUE':([9,34,43,44,45,46,47,48,64,65,79,84,],[32,32,-32,-33,32,-29,-30,-31,32,32,32,32,]),'FALSE':([9,34,43,44,45,46,47,48,64,65,79,84,],[33,33,-32,-33,33,-29,-30,-31,33,33,33,33,]),'EQUAL':([10,16,17,18,93,],[34,-34,-35,-36,34,]),'PUNTO':([10,11,16,17,18,82,88,93,],[35,36,-34,-35,-36,88,90,35,]),'END':([12,14,15,16,17,18,25,26,27,28,29,30,32,33,38,49,50,51,52,53,54,58,61,62,63,69,81,83,85,86,87,94,95,96,97,98,100,],[-53,-23,-25,-34,-35,-36,-7,-8,-9,-10,-24,-26,-27,-28,-12,-37,-38,-39,-40,-41,-42,-58,-13,-14,-43,-44,-57,-52,-54,-55,-56,99,-62,-59,-60,-61,-63,]),'MAYORQUE':([14,15,16,17,18,25,29,30,38,],[-23,-25,-34,-35,-36,40,-24,-26,-12,]),'MENORQUE':([14,15,16,17,18,25,29,30,38,],[-23,-25,-34,-35,-36,41,-24,-26,-12,]),'EQUALSX2':([14,15,16,17,18,25,29,30,31,32,33,38,51,],[-23,-25,-34,-35,-36,43,-24,-26,43,-27,-28,-12,43,]),'NOTEQUALS':([14,15,16,17,18,25,29,30,31,32,33,38,51,],[-23,-25,-34,-35,-36,44,-24,-26,44,-27,-28,-12,44,]),'IN':([16,17,18,37,],[-34,-35,-36,60,]),'RPAREN':([16,17,18,32,33,67,72,73,74,75,76,77,78,80,83,91,],[-34,-35,-36,-27,-28,81,-45,-46,-47,-48,-49,85,86,87,-52,92,]),'AND':([31,32,33,51,],[46,-27,-28,46,]),'OR':([31,32,33,51,],[47,-27,-28,47,]),'COMMA':([32,33,71,72,73,74,75,76,],[-27,-28,84,-45,-46,-47,-48,-49,]),'RCOR':([32,33,64,70,71,72,73,74,75,76,89,],[-27,-28,69,83,-50,-45,-46,-47,-48,-49,-51,]),'SET':([34,],[55,]),'ADD':([35,],[56,]),'MERGE':([35,],[57,]),'SIZE':([35,],[58,]),'CHOMP':([36,],[59,]),'LCOR':([55,65,],[64,79,]),'LPAREN':([56,57,58,60,],[65,66,67,68,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'cuerpo':([0,],[1,]),'expression':([0,9,19,34,39,],[2,30,30,30,30,]),'impresion':([0,92,95,],[3,96,96,]),'asignacion':([0,92,95,],[4,97,97,]),'leer':([0,],[5,]),'funcionstruct':([0,92,95,],[6,98,98,]),'sentenciafor':([0,],[7,]),'factor':([0,9,19,34,39,],[8,25,38,49,61,]),'variables':([0,9,13,19,34,39,66,92,95,],[10,29,37,29,29,29,80,93,93,]),'funcionsconjunto':([0,92,95,],[12,12,12,]),'operadoresMat':([8,25,38,49,61,],[19,19,19,19,19,]),'comparacion':([9,],[26,]),'comparacion_bool':([9,34,],[27,52,]),'booleanos':([9,34,45,64,65,79,84,],[31,51,62,75,75,75,75,]),'operadoresComp':([25,],[39,]),'operadoresEquals':([25,31,51,],[42,48,48,]),'operadoresBool':([31,51,],[45,45,]),'struct':([34,],[53,]),'conjunto':([34,],[54,]),'arr':([55,65,],[63,78,]),'repetirvalor':([64,79,84,],[70,70,89,]),'valor':([64,65,79,84,],[71,77,71,71,]),'repetircontenido':([92,95,],[94,100,]),'contenido':([92,95,],[95,95,]),}

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
  ('cuerpo -> leer','cuerpo',1,'p_cuerpo','sintactico.py',9),
  ('cuerpo -> funcionstruct','cuerpo',1,'p_cuerpo','sintactico.py',10),
  ('cuerpo -> sentenciafor','cuerpo',1,'p_cuerpo','sintactico.py',11),
  ('impresion -> PUTS factor','impresion',2,'p_impresion','sintactico.py',13),
  ('impresion -> PUTS comparacion','impresion',2,'p_impresion','sintactico.py',14),
  ('impresion -> PUTS comparacion_bool','impresion',2,'p_impresion','sintactico.py',15),
  ('impresion -> PUTS STRING','impresion',2,'p_impresion','sintactico.py',16),
  ('leer -> GETS PUNTO CHOMP','leer',3,'p_leer','sintactico.py',19),
  ('expression -> factor operadoresMat factor','expression',3,'p_expression_mat','sintactico.py',22),
  ('comparacion -> factor operadoresComp factor','comparacion',3,'p_comparacion','sintactico.py',28),
  ('comparacion_bool -> booleanos operadoresBool booleanos','comparacion_bool',3,'p_comparacion_bool','sintactico.py',31),
  ('operadoresComp -> MAYORQUE','operadoresComp',1,'p_operadoresComp','sintactico.py',34),
  ('operadoresComp -> MENORQUE','operadoresComp',1,'p_operadoresComp','sintactico.py',35),
  ('operadoresComp -> operadoresEquals','operadoresComp',1,'p_operadoresComp','sintactico.py',36),
  ('operadoresMat -> PLUS','operadoresMat',1,'p_operadoresMat','sintactico.py',39),
  ('operadoresMat -> MINUS','operadoresMat',1,'p_operadoresMat','sintactico.py',40),
  ('operadoresMat -> TIMES','operadoresMat',1,'p_operadoresMat','sintactico.py',41),
  ('operadoresMat -> DIVIDE','operadoresMat',1,'p_operadoresMat','sintactico.py',42),
  ('operadoresMat -> MOD','operadoresMat',1,'p_operadoresMat','sintactico.py',43),
  ('factor -> INT','factor',1,'p_factor_num','sintactico.py',46),
  ('factor -> variables','factor',1,'p_factor_num','sintactico.py',47),
  ('factor -> FLOAT','factor',1,'p_factor_num','sintactico.py',48),
  ('factor -> expression','factor',1,'p_factor_expr','sintactico.py',51),
  ('booleanos -> TRUE','booleanos',1,'p_booleanos','sintactico.py',54),
  ('booleanos -> FALSE','booleanos',1,'p_booleanos','sintactico.py',55),
  ('operadoresBool -> AND','operadoresBool',1,'p_operadoresBool','sintactico.py',59),
  ('operadoresBool -> OR','operadoresBool',1,'p_operadoresBool','sintactico.py',60),
  ('operadoresBool -> operadoresEquals','operadoresBool',1,'p_operadoresBool','sintactico.py',61),
  ('operadoresEquals -> EQUALSX2','operadoresEquals',1,'p_operadoresEqual','sintactico.py',63),
  ('operadoresEquals -> NOTEQUALS','operadoresEquals',1,'p_operadoresEqual','sintactico.py',64),
  ('variables -> ID','variables',1,'p_variables','sintactico.py',66),
  ('variables -> CONSTANT','variables',1,'p_variables','sintactico.py',67),
  ('variables -> GLOBAL','variables',1,'p_variables','sintactico.py',68),
  ('asignacion -> variables EQUAL factor','asignacion',3,'p_asignacion','sintactico.py',72),
  ('asignacion -> variables EQUAL STRING','asignacion',3,'p_asignacion','sintactico.py',73),
  ('asignacion -> variables EQUAL booleanos','asignacion',3,'p_asignacion','sintactico.py',74),
  ('asignacion -> variables EQUAL comparacion_bool','asignacion',3,'p_asignacion','sintactico.py',75),
  ('asignacion -> variables EQUAL struct','asignacion',3,'p_asignacion','sintactico.py',76),
  ('struct -> conjunto','struct',1,'p_struct','sintactico.py',80),
  ('conjunto -> SET arr','conjunto',2,'p_conjunto','sintactico.py',83),
  ('conjunto -> SET LCOR RCOR','conjunto',3,'p_conjunto','sintactico.py',84),
  ('valor -> INT','valor',1,'p_valor','sintactico.py',87),
  ('valor -> ID','valor',1,'p_valor','sintactico.py',88),
  ('valor -> STRING','valor',1,'p_valor','sintactico.py',89),
  ('valor -> booleanos','valor',1,'p_valor','sintactico.py',90),
  ('valor -> FLOAT','valor',1,'p_valor','sintactico.py',91),
  ('repetirvalor -> valor','repetirvalor',1,'p_repetirvalor','sintactico.py',94),
  ('repetirvalor -> valor COMMA repetirvalor','repetirvalor',3,'p_repetirvalor','sintactico.py',95),
  ('arr -> LCOR repetirvalor RCOR','arr',3,'p_arr','sintactico.py',99),
  ('funcionstruct -> funcionsconjunto','funcionstruct',1,'p_funcionstruct','sintactico.py',102),
  ('funcionsconjunto -> variables PUNTO ADD LPAREN valor RPAREN','funcionsconjunto',6,'p_funcionsconjunto','sintactico.py',105),
  ('funcionsconjunto -> variables PUNTO ADD LPAREN arr RPAREN','funcionsconjunto',6,'p_funcionsconjunto','sintactico.py',106),
  ('funcionsconjunto -> variables PUNTO MERGE LPAREN variables RPAREN','funcionsconjunto',6,'p_funcionsconjunto','sintactico.py',107),
  ('funcionsconjunto -> variables PUNTO SIZE LPAREN RPAREN','funcionsconjunto',5,'p_funcionsconjunto','sintactico.py',108),
  ('funcionsconjunto -> variables PUNTO SIZE','funcionsconjunto',3,'p_funcionsconjunto','sintactico.py',109),
  ('contenido -> impresion','contenido',1,'p_contenido','sintactico.py',112),
  ('contenido -> asignacion','contenido',1,'p_contenido','sintactico.py',113),
  ('contenido -> funcionstruct','contenido',1,'p_contenido','sintactico.py',114),
  ('repetircontenido -> contenido','repetircontenido',1,'p_repetircontenido','sintactico.py',116),
  ('repetircontenido -> contenido repetircontenido','repetircontenido',2,'p_repetircontenido','sintactico.py',117),
  ('sentenciafor -> FOR variables IN LPAREN INT PUNTO PUNTO INT RPAREN repetircontenido END','sentenciafor',11,'p_sentenciafor','sintactico.py',120),
]
