
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEADD AND ARRAY BREAK CHOMP CLEAR COMMA CONSTANT DEF DEFINED DELETE DIVIDE ELSE ELSIF END EQUAL EQUALSX2 FALSE FETCH FIRST FLECHA FLOAT FOR GETS GLOBAL ID IF IN INT KEY LBRACE LCOR LENGTH LPAREN MAYORQUE MENORQUE MERGE MINUS MOD NEW NEWLINE NOTEQUALS NUMERAL OR PLUS PUNTO PUSH PUTS RBRACE RCOR RETURN RPAREN SAMPLE SEMICOLON SET SIZE STORE STRING TIMES TRUE WHILEcuerpo : expression\n             | impresion\n             | asignacion\n             | leer\n             | funcionstruct\n             | estructurasControl\n             | operaciones\n             | cuerpo NEWLINE cuerpoimpresion : PUTS factor\n                    | PUTS comparacion\n                    | PUTS comparacion_bool\n                    | PUTS STRING\n                    | PUTS variablesleer : PUTS STRING NEWLINE variables EQUAL GETS PUNTO CHOMPexpression : factor operadoresMat factorexpression : factor error factorexpression : factor operadoresMat erroroperacionstring : STRING PLUS STRING\n                     | STRING TIMES INT\n                     | STRING PLUS operacionstringoperacionstring : STRING error STRING\n                     | STRING error INT\n                     | STRING error operacionstringoperacionstring : STRING PLUS error\n                     | STRING TIMES erroroperaciones : operacionstring\n                    | comparacion_bool\n                    | comparacionb\n                    | comparacioncomparacioon : STRING operadoresEquals STRING\n                    | STRING operadoresComp STRINGcomparacioon : STRING operadoresEquals error\n                    | STRING operadoresComp errorcomparacioon : factor operadoresEquals factor\n                    | factor operadoresComp factorcomparacioon : factor operadoresEquals error\n                    | factor operadoresComp errorcomparacion : comparacioon\n                   | comparacioon operadoresBool comparacion comparacion_bool : booleanos operadoresEquals booleanoscomparacion_bool : booleanos operadoresEquals errorcomparacion_bool : booleanos error booleanoscomparacionb : booleanos operadoresBool booleanos\n                           | booleanos operadoresBool comparacionboperadoresComp : MAYORQUE\n                    | MENORQUE\n                    | operadoresEqualsoperadoresMat : PLUS\n                    | MINUS\n                    | TIMES\n                    | DIVIDE\n                    | MODfactor : INT\n            | FLOATfactor : expressionbooleanos : TRUE\n        | FALSE\n    operadoresBool : AND\n                        | ORoperadoresEquals : EQUALSX2\n                        | NOTEQUALSvariables : ID\n                | CONSTANT\n                | GLOBALasignacion : variables EQUAL factor\n                  | variables EQUAL STRING\n                  | variables EQUAL booleanos\n                  | variables EQUAL struct\n                  | variables EQUAL operacionesstruct : conjunto\n                | formacion\n                | hashconjunto : SET arr\n                | SET LCOR RCORvalor : INT\n             | STRING\n             | booleanos\n             | FLOATrepetirvalor : valor\n                    | valor COMMA repetirvalorarr : LCOR repetirvalor RCORfuncionstruct : funcionsconjunto\n                        | funcionsformacion\n                        | funcionsHashfuncionsconjunto : conjunto PUNTO ADD LPAREN valor RPAREN\n                        | conjunto PUNTO ADD LPAREN arr RPAREN\n                        | conjunto PUNTO MERGE LPAREN conjunto RPAREN\n                        | conjunto PUNTO SIZE LPAREN RPAREN\n                        | conjunto PUNTO SIZEcontenido : impresion\n                 | asignacion\n                 | funcionstructrepetircontenido : contenido\n                         | contenido SEMICOLON repetircontenidocondicion : comparacion\n                | comparacion_bool\n                | comparacionb\n                | booleanossentenciafor : FOR variables IN LPAREN INT PUNTO PUNTO INT RPAREN NEWLINE repetircontenido NEWLINE END\n                    | FOR variables IN LPAREN INT PUNTO PUNTO INT RPAREN NEWLINE sentenciaif NEWLINE END\n                    | FOR variables IN LPAREN INT PUNTO PUNTO INT RPAREN NEWLINE sentenciaif NEWLINE repetircontenido NEWLINE ENDsentenciaif : IF condicion NEWLINE repetircontenido NEWLINE END\n                   | IF condicion NEWLINE repetircontenido NEWLINE sentenciaelsifsentenciaif : IF error NEWLINE repetircontenido NEWLINE END\n                   | IF error NEWLINE repetircontenido NEWLINE sentenciaelsifsentenciaelsif : ELSIF condicion NEWLINE repetircontenido NEWLINE END\n                      | ELSIF condicion NEWLINE repetircontenido NEWLINE sentenciaelsifsentenciaelsif : ELSIF error NEWLINE repetircontenido NEWLINE END\n                      | ELSIF error NEWLINE repetircontenido NEWLINE sentenciaelsifsentenciawhile : WHILE condicion NEWLINE repetircontenido NEWLINE END\n                      | WHILE condicion NEWLINE sentenciaif NEWLINE ENDsentenciawhile : WHILE error NEWLINE repetircontenido NEWLINE END\n                      | WHILE error NEWLINE sentenciaif NEWLINE ENDestructurasControl : sentenciaif\n                           | sentenciawhile\n                           | sentenciaforformacion : LCOR repetirvalor RCOR\n                | LCOR RCOR\n                | ARRAY PUNTO NEW LPAREN INT RPAREN\n                | ARRAY PUNTO NEW LPAREN  RPARENfuncionsformacion : formacion PUNTO LENGTH LPAREN RPAREN\n                        | formacion PUNTO PUSH LPAREN repetirvalor RPAREN\n                        | formacion PUNTO SAMPLE LPAREN RPAREN\n                        | formacion PUNTO SAMPLE LPAREN INT RPAREN\n                        | formacion PUNTO FIRST\n                        | formacion PUNTO FIRST LPAREN RPARENhash : LBRACE hash_content RBRACEhash_elements : hash_element hash_more_elementshash_content : hash_element \n                    | hash_elementshash_element : clave FLECHA valuehash_more_elements : COMMA hash_element\n                            | COMMA hash_element hash_more_elementsclave : STRING\n            | INT\n            | FLOATvalue : valor\n            | structhash_add : hash PUNTO STORE LPAREN clave COMMA value RPARENhash_delete : hash PUNTO DELETE LPAREN clave RPARENhash_key : hash PUNTO KEY LPAREN value RPARENfuncionsHash : hash_add\n                    | hash_delete\n                    | hash_key'
    
_lr_action_items = {'PUTS':([0,45,150,151,152,153,210,251,252,260,268,],[10,10,181,181,181,181,181,181,181,181,181,]),'INT':([0,10,34,35,39,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,67,68,71,75,76,90,92,159,166,167,169,173,174,181,187,190,191,192,193,201,232,242,248,],[24,24,24,24,96,107,24,24,24,24,24,-48,-49,-50,-51,-52,-60,-61,-45,-46,121,124,24,-58,-59,24,96,96,107,96,96,96,207,24,217,218,107,107,96,96,24,96,253,]),'FLOAT':([0,10,34,35,39,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,71,75,76,90,92,159,166,167,169,173,181,191,192,193,201,232,242,],[25,25,25,25,99,108,25,25,25,25,25,-48,-49,-50,-51,-52,-60,-61,-45,-46,25,-58,-59,25,99,99,108,99,99,99,25,108,108,99,99,25,99,]),'ID':([0,10,36,45,117,150,151,152,153,181,210,251,252,260,268,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'CONSTANT':([0,10,36,45,117,150,151,152,153,181,210,251,252,260,268,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'GLOBAL':([0,10,36,45,117,150,151,152,153,181,210,251,252,260,268,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'IF':([0,45,152,153,260,],[34,34,34,34,34,]),'WHILE':([0,45,],[35,35,]),'FOR':([0,45,],[36,36,]),'STRING':([0,10,34,35,39,44,45,55,56,57,58,66,68,69,70,71,75,76,90,92,159,166,167,169,173,181,191,192,193,201,232,242,],[13,62,85,85,97,106,13,-60,-61,-45,-46,118,123,126,128,131,-58,-59,85,97,97,106,97,97,97,211,106,106,97,97,85,97,]),'SET':([0,45,71,150,151,152,153,167,170,193,210,242,251,252,260,268,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'LCOR':([0,38,45,71,150,151,152,153,167,169,193,210,242,251,252,260,268,],[39,92,39,39,39,39,39,39,39,201,39,39,39,39,39,39,39,]),'ARRAY':([0,45,71,150,151,152,153,167,193,210,242,251,252,260,268,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'TRUE':([0,10,34,35,39,45,55,56,71,72,73,74,75,76,92,159,167,169,173,181,193,201,232,242,],[42,42,42,42,42,42,-60,-61,42,42,42,42,-58,-59,42,42,42,42,42,42,42,42,42,42,]),'FALSE':([0,10,34,35,39,45,55,56,71,72,73,74,75,76,92,159,167,169,173,181,193,201,232,242,],[43,43,43,43,43,43,-60,-61,43,43,43,43,-58,-59,43,43,43,43,43,43,43,43,43,43,]),'LBRACE':([0,45,71,150,151,152,153,167,193,210,242,251,252,260,268,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'$end':([1,2,3,4,5,6,7,8,11,12,16,17,18,19,20,21,22,23,24,25,26,27,28,31,32,33,37,42,43,59,60,61,62,63,64,91,94,109,110,111,112,113,114,115,116,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,145,149,155,156,158,164,188,203,204,206,208,219,225,226,227,228,229,230,231,234,235,236,237,238,239,241,243,244,250,254,261,262,263,264,269,270,273,],[0,-1,-2,-3,-4,-5,-6,-7,-29,-27,-82,-83,-84,-114,-115,-116,-26,-28,-53,-54,-62,-63,-64,-142,-143,-144,-38,-56,-57,-9,-10,-11,-12,-13,-55,-73,-118,-8,-15,-17,-16,-34,-36,-35,-37,-18,-20,-24,-19,-25,-21,-22,-23,-30,-32,-31,-33,-65,-66,-67,-68,-69,-70,-71,-72,-40,-41,-42,-43,-44,-89,-125,-39,-74,-117,-127,-81,-88,-121,-123,-126,-120,-85,-86,-87,-122,-124,-102,-103,-104,-105,-110,-111,-112,-113,-119,-140,-141,-14,-139,-106,-107,-108,-109,-99,-100,-101,]),'NEWLINE':([1,2,3,4,5,6,7,8,11,12,16,17,18,19,20,21,22,23,24,25,26,27,28,31,32,33,37,42,43,59,60,61,62,63,64,79,80,81,82,83,84,87,88,91,94,109,110,111,112,113,114,115,116,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,145,149,155,156,158,164,176,177,178,179,180,182,183,184,185,186,188,203,204,206,208,211,219,225,226,227,228,229,230,231,233,234,235,236,237,238,239,241,243,244,246,247,250,254,255,256,257,261,262,263,264,265,266,269,270,271,273,],[45,-1,-2,-3,-4,-5,-6,-7,-29,-27,-82,-83,-84,-114,-115,-116,-26,-28,-53,-54,-62,-63,-64,-142,-143,-144,-38,-56,-57,-9,-10,-11,117,-13,-55,150,151,-95,-96,-97,-98,152,153,-73,-118,45,-15,-17,-16,-34,-36,-35,-37,-18,-20,-24,-19,-25,-21,-22,-23,-30,-32,-31,-33,-65,-66,-67,-68,-69,-70,-71,-72,-40,-41,-42,-43,-44,-89,-125,-39,-74,-117,-127,209,-93,-90,-91,-92,212,213,214,215,216,-81,-88,-121,-123,-126,-12,-120,-85,-86,-87,-122,-124,-102,-103,-94,-104,-105,-110,-111,-112,-113,-119,-140,-141,251,252,-14,-139,258,259,260,-106,-107,-108,-109,267,268,-99,-100,272,-101,]),'error':([2,9,13,15,24,25,34,35,42,43,46,48,49,50,51,52,53,54,55,56,57,58,59,64,65,66,67,69,70,72,84,86,110,111,112,113,115,118,123,130,131,132,232,],[-55,47,68,73,-53,-54,80,88,-56,-57,111,114,116,-48,-49,-50,-51,-52,-60,-61,-45,-46,47,-55,73,120,122,127,129,139,73,47,47,-17,47,47,47,68,68,47,68,73,247,]),'PLUS':([2,9,13,24,25,59,64,86,110,111,112,113,115,118,123,130,131,],[-55,50,66,-53,-54,50,-55,50,50,-17,50,50,50,66,66,50,66,]),'MINUS':([2,9,24,25,59,64,86,110,111,112,113,115,130,],[-55,51,-53,-54,51,-55,51,51,-17,51,51,51,51,]),'TIMES':([2,9,13,24,25,59,64,86,110,111,112,113,115,118,123,130,131,],[-55,52,67,-53,-54,52,-55,52,52,-17,52,52,52,67,67,52,67,]),'DIVIDE':([2,9,24,25,59,64,86,110,111,112,113,115,130,],[-55,53,-53,-54,53,-55,53,53,-17,53,53,53,53,]),'MOD':([2,9,24,25,59,64,86,110,111,112,113,115,130,],[-55,54,-53,-54,54,-55,54,54,-17,54,54,54,54,]),'EQUALSX2':([2,9,13,15,24,25,42,43,59,62,64,65,84,85,86,110,111,112,130,131,132,211,],[-55,55,55,55,-53,-54,-56,-57,55,55,-55,55,55,55,55,-15,-17,-16,55,55,55,55,]),'NOTEQUALS':([2,9,13,15,24,25,42,43,59,62,64,65,84,85,86,110,111,112,130,131,132,211,],[-55,56,56,56,-53,-54,-56,-57,56,56,-55,56,56,56,56,-15,-17,-16,56,56,56,56,]),'MAYORQUE':([2,9,13,24,25,59,62,64,85,86,110,111,112,130,131,211,],[-55,57,57,-53,-54,57,57,-55,57,57,-15,-17,-16,57,57,57,]),'MENORQUE':([2,9,13,24,25,59,62,64,85,86,110,111,112,130,131,211,],[-55,58,58,-53,-54,58,58,-55,58,58,-15,-17,-16,58,58,58,]),'SEMICOLON':([11,12,16,17,18,22,23,24,25,26,27,28,31,32,33,37,42,43,59,60,61,63,64,91,94,110,111,112,113,114,115,116,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,145,149,155,156,158,164,177,178,179,180,188,203,204,206,208,211,219,225,226,227,228,229,241,243,244,254,],[-29,-27,-82,-83,-84,-26,-28,-53,-54,-62,-63,-64,-142,-143,-144,-38,-56,-57,-9,-10,-11,-13,-55,-73,-118,-15,-17,-16,-34,-36,-35,-37,-18,-20,-24,-19,-25,-21,-22,-23,-30,-32,-31,-33,-65,-66,-67,-68,-69,-70,-71,-72,-40,-41,-42,-43,-44,-89,-125,-39,-74,-117,-127,210,-90,-91,-92,-81,-88,-121,-123,-126,-12,-120,-85,-86,-87,-122,-124,-119,-140,-141,-139,]),'EQUAL':([14,26,27,28,168,],[71,-62,-63,-64,198,]),'AND':([15,24,25,37,42,43,64,84,110,111,112,113,114,115,116,126,127,128,129,132,141,],[75,-53,-54,75,-56,-57,-55,75,-15,-17,-16,-34,-36,-35,-37,-30,-32,-31,-33,75,75,]),'OR':([15,24,25,37,42,43,64,84,110,111,112,113,114,115,116,126,127,128,129,132,141,],[76,-53,-54,76,-56,-57,-55,76,-15,-17,-16,-34,-36,-35,-37,-30,-32,-31,-33,76,76,]),'IN':([26,27,28,89,],[-62,-63,-64,154,]),'PUNTO':([29,30,40,41,91,94,156,158,164,188,217,219,224,240,241,],[77,78,100,101,-73,-118,-74,-117,-127,-81,240,-120,245,248,-119,]),'RCOR':([39,42,43,92,93,95,96,97,98,99,157,189,],[94,-56,-57,156,158,-79,-75,-76,-77,-78,188,-80,]),'COMMA':([42,43,91,94,95,96,97,98,99,103,106,107,108,135,136,137,156,158,164,188,194,195,196,197,219,220,241,],[-56,-57,-73,-118,159,-75,-76,-77,-78,166,-134,-135,-136,-70,-71,-72,-74,-117,-127,-81,166,-131,-137,-138,-120,242,-119,]),'RPAREN':([42,43,91,94,95,96,97,98,99,106,107,108,135,136,137,156,158,164,171,172,174,175,188,189,190,196,197,199,200,202,205,207,218,219,221,222,241,249,253,],[-56,-57,-73,-118,-79,-75,-76,-77,-78,-134,-135,-136,-70,-71,-72,-74,-117,-127,203,204,206,208,-81,-80,219,-137,-138,225,226,227,228,229,241,-120,243,244,-119,254,257,]),'RBRACE':([42,43,91,94,96,97,98,99,102,103,104,135,136,137,156,158,164,165,188,194,195,196,197,219,223,241,],[-56,-57,-73,-118,-75,-76,-77,-78,164,-129,-130,-70,-71,-72,-74,-117,-127,-128,-81,-132,-131,-137,-138,-120,-133,-119,]),'ADD':([77,],[143,]),'MERGE':([77,],[144,]),'SIZE':([77,],[145,]),'LENGTH':([78,],[146,]),'PUSH':([78,],[147,]),'SAMPLE':([78,],[148,]),'FIRST':([78,],[149,]),'NEW':([100,],[160,]),'STORE':([101,],[161,]),'DELETE':([101,],[162,]),'KEY':([101,],[163,]),'FLECHA':([105,106,107,108,],[167,-134,-135,-136,]),'LPAREN':([143,144,145,146,147,148,149,154,160,161,162,163,],[169,170,171,172,173,174,175,187,190,191,192,193,]),'GETS':([198,],[224,]),'END':([209,212,213,214,215,216,258,259,267,268,272,],[230,234,236,237,238,239,261,263,269,270,273,]),'ELSIF':([209,212,258,259,],[232,232,232,232,]),'CHOMP':([245,],[250,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'cuerpo':([0,45,],[1,109,]),'expression':([0,10,34,35,45,46,47,48,49,71,90,181,232,],[2,64,64,64,2,64,64,64,64,64,64,64,64,]),'impresion':([0,45,150,151,152,153,210,251,252,260,268,],[3,3,178,178,178,178,178,178,178,178,178,]),'asignacion':([0,45,150,151,152,153,210,251,252,260,268,],[4,4,179,179,179,179,179,179,179,179,179,]),'leer':([0,45,],[5,5,]),'funcionstruct':([0,45,150,151,152,153,210,251,252,260,268,],[6,6,180,180,180,180,180,180,180,180,180,]),'estructurasControl':([0,45,],[7,7,]),'operaciones':([0,45,71,],[8,8,134,]),'factor':([0,10,34,35,45,46,47,48,49,71,90,181,232,],[9,59,86,86,9,110,112,113,115,130,86,59,86,]),'comparacion':([0,10,34,35,45,71,90,181,232,],[11,60,81,81,11,11,155,60,81,]),'comparacion_bool':([0,10,34,35,45,71,181,232,],[12,61,82,82,12,12,61,82,]),'variables':([0,10,36,45,117,150,151,152,153,181,210,251,252,260,268,],[14,63,89,14,168,14,14,14,14,63,14,14,14,14,14,]),'booleanos':([0,10,34,35,39,45,71,72,73,74,92,159,167,169,173,181,193,201,232,242,],[15,65,84,84,98,15,132,138,140,141,98,98,98,98,98,65,98,98,84,98,]),'funcionsconjunto':([0,45,150,151,152,153,210,251,252,260,268,],[16,16,16,16,16,16,16,16,16,16,16,]),'funcionsformacion':([0,45,150,151,152,153,210,251,252,260,268,],[17,17,17,17,17,17,17,17,17,17,17,]),'funcionsHash':([0,45,150,151,152,153,210,251,252,260,268,],[18,18,18,18,18,18,18,18,18,18,18,]),'sentenciaif':([0,45,152,153,260,],[19,19,184,186,266,]),'sentenciawhile':([0,45,],[20,20,]),'sentenciafor':([0,45,],[21,21,]),'operacionstring':([0,45,66,68,71,],[22,22,119,125,22,]),'comparacionb':([0,34,35,45,71,74,232,],[23,83,83,23,23,142,83,]),'conjunto':([0,45,71,150,151,152,153,167,170,193,210,242,251,252,260,268,],[29,29,135,29,29,29,29,135,202,135,29,135,29,29,29,29,]),'formacion':([0,45,71,150,151,152,153,167,193,210,242,251,252,260,268,],[30,30,136,30,30,30,30,136,136,30,136,30,30,30,30,]),'hash_add':([0,45,150,151,152,153,210,251,252,260,268,],[31,31,31,31,31,31,31,31,31,31,31,]),'hash_delete':([0,45,150,151,152,153,210,251,252,260,268,],[32,32,32,32,32,32,32,32,32,32,32,]),'hash_key':([0,45,150,151,152,153,210,251,252,260,268,],[33,33,33,33,33,33,33,33,33,33,33,]),'comparacioon':([0,10,34,35,45,71,90,181,232,],[37,37,37,37,37,37,37,37,37,]),'hash':([0,45,71,150,151,152,153,167,193,210,242,251,252,260,268,],[41,41,137,41,41,41,41,137,137,41,137,41,41,41,41,]),'operadoresMat':([9,59,86,110,112,113,115,130,],[46,46,46,46,46,46,46,46,]),'operadoresEquals':([9,13,15,59,62,65,84,85,86,130,131,132,211,],[48,69,72,48,69,72,72,69,48,48,69,72,69,]),'operadoresComp':([9,13,59,62,85,86,130,131,211,],[49,70,49,70,70,49,49,70,70,]),'operadoresBool':([15,37,84,132,141,],[74,90,74,74,74,]),'condicion':([34,35,232,],[79,87,246,]),'arr':([38,169,],[91,200,]),'repetirvalor':([39,92,159,173,201,],[93,157,189,205,157,]),'valor':([39,92,159,167,169,173,193,201,242,],[95,95,95,196,199,95,196,95,196,]),'hash_content':([44,],[102,]),'hash_element':([44,166,],[103,194,]),'hash_elements':([44,],[104,]),'clave':([44,166,191,192,],[105,105,220,221,]),'struct':([71,167,193,242,],[133,197,197,197,]),'hash_more_elements':([103,194,],[165,223,]),'repetircontenido':([150,151,152,153,210,251,252,260,268,],[176,182,183,185,233,255,256,265,271,]),'contenido':([150,151,152,153,210,251,252,260,268,],[177,177,177,177,177,177,177,177,177,]),'value':([167,193,242,],[195,222,249,]),'sentenciaelsif':([209,212,258,259,],[231,235,262,264,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> cuerpo","S'",1,None,None,None),
  ('cuerpo -> expression','cuerpo',1,'p_cuerpo','sintactico.py',13),
  ('cuerpo -> impresion','cuerpo',1,'p_cuerpo','sintactico.py',14),
  ('cuerpo -> asignacion','cuerpo',1,'p_cuerpo','sintactico.py',15),
  ('cuerpo -> leer','cuerpo',1,'p_cuerpo','sintactico.py',16),
  ('cuerpo -> funcionstruct','cuerpo',1,'p_cuerpo','sintactico.py',17),
  ('cuerpo -> estructurasControl','cuerpo',1,'p_cuerpo','sintactico.py',18),
  ('cuerpo -> operaciones','cuerpo',1,'p_cuerpo','sintactico.py',19),
  ('cuerpo -> cuerpo NEWLINE cuerpo','cuerpo',3,'p_cuerpo','sintactico.py',20),
  ('impresion -> PUTS factor','impresion',2,'p_impresion','sintactico.py',26),
  ('impresion -> PUTS comparacion','impresion',2,'p_impresion','sintactico.py',27),
  ('impresion -> PUTS comparacion_bool','impresion',2,'p_impresion','sintactico.py',28),
  ('impresion -> PUTS STRING','impresion',2,'p_impresion','sintactico.py',29),
  ('impresion -> PUTS variables','impresion',2,'p_impresion','sintactico.py',30),
  ('leer -> PUTS STRING NEWLINE variables EQUAL GETS PUNTO CHOMP','leer',8,'p_leer','sintactico.py',36),
  ('expression -> factor operadoresMat factor','expression',3,'p_expression_mat','sintactico.py',41),
  ('expression -> factor error factor','expression',3,'p_expression_mat_error','sintactico.py',46),
  ('expression -> factor operadoresMat error','expression',3,'p_expression_mat_error_factors','sintactico.py',51),
  ('operacionstring -> STRING PLUS STRING','operacionstring',3,'p_operacionstring','sintactico.py',56),
  ('operacionstring -> STRING TIMES INT','operacionstring',3,'p_operacionstring','sintactico.py',57),
  ('operacionstring -> STRING PLUS operacionstring','operacionstring',3,'p_operacionstring','sintactico.py',58),
  ('operacionstring -> STRING error STRING','operacionstring',3,'p_operacionstring_error','sintactico.py',60),
  ('operacionstring -> STRING error INT','operacionstring',3,'p_operacionstring_error','sintactico.py',61),
  ('operacionstring -> STRING error operacionstring','operacionstring',3,'p_operacionstring_error','sintactico.py',62),
  ('operacionstring -> STRING PLUS error','operacionstring',3,'p_operacionstring_error_element','sintactico.py',67),
  ('operacionstring -> STRING TIMES error','operacionstring',3,'p_operacionstring_error_element','sintactico.py',68),
  ('operaciones -> operacionstring','operaciones',1,'p_operaciones','sintactico.py',73),
  ('operaciones -> comparacion_bool','operaciones',1,'p_operaciones','sintactico.py',74),
  ('operaciones -> comparacionb','operaciones',1,'p_operaciones','sintactico.py',75),
  ('operaciones -> comparacion','operaciones',1,'p_operaciones','sintactico.py',76),
  ('comparacioon -> STRING operadoresEquals STRING','comparacioon',3,'p_comparacion_strings','sintactico.py',79),
  ('comparacioon -> STRING operadoresComp STRING','comparacioon',3,'p_comparacion_strings','sintactico.py',80),
  ('comparacioon -> STRING operadoresEquals error','comparacioon',3,'p_comparacion_strigs_error','sintactico.py',85),
  ('comparacioon -> STRING operadoresComp error','comparacioon',3,'p_comparacion_strigs_error','sintactico.py',86),
  ('comparacioon -> factor operadoresEquals factor','comparacioon',3,'p_comparacion_numeros','sintactico.py',91),
  ('comparacioon -> factor operadoresComp factor','comparacioon',3,'p_comparacion_numeros','sintactico.py',92),
  ('comparacioon -> factor operadoresEquals error','comparacioon',3,'p_comparacion_numeros_error','sintactico.py',97),
  ('comparacioon -> factor operadoresComp error','comparacioon',3,'p_comparacion_numeros_error','sintactico.py',98),
  ('comparacion -> comparacioon','comparacion',1,'p_comparacion','sintactico.py',103),
  ('comparacion -> comparacioon operadoresBool comparacion','comparacion',3,'p_comparacion','sintactico.py',104),
  ('comparacion_bool -> booleanos operadoresEquals booleanos','comparacion_bool',3,'p_comparacion_bool','sintactico.py',107),
  ('comparacion_bool -> booleanos operadoresEquals error','comparacion_bool',3,'p_comparacion_bool_type_error','sintactico.py',112),
  ('comparacion_bool -> booleanos error booleanos','comparacion_bool',3,'p_comparacion_bool_operand_error','sintactico.py',117),
  ('comparacionb -> booleanos operadoresBool booleanos','comparacionb',3,'p_comparacionb','sintactico.py',122),
  ('comparacionb -> booleanos operadoresBool comparacionb','comparacionb',3,'p_comparacionb','sintactico.py',123),
  ('operadoresComp -> MAYORQUE','operadoresComp',1,'p_operadoresComp','sintactico.py',128),
  ('operadoresComp -> MENORQUE','operadoresComp',1,'p_operadoresComp','sintactico.py',129),
  ('operadoresComp -> operadoresEquals','operadoresComp',1,'p_operadoresComp','sintactico.py',130),
  ('operadoresMat -> PLUS','operadoresMat',1,'p_operadoresMat','sintactico.py',133),
  ('operadoresMat -> MINUS','operadoresMat',1,'p_operadoresMat','sintactico.py',134),
  ('operadoresMat -> TIMES','operadoresMat',1,'p_operadoresMat','sintactico.py',135),
  ('operadoresMat -> DIVIDE','operadoresMat',1,'p_operadoresMat','sintactico.py',136),
  ('operadoresMat -> MOD','operadoresMat',1,'p_operadoresMat','sintactico.py',137),
  ('factor -> INT','factor',1,'p_factor_num','sintactico.py',140),
  ('factor -> FLOAT','factor',1,'p_factor_num','sintactico.py',141),
  ('factor -> expression','factor',1,'p_factor_expr','sintactico.py',144),
  ('booleanos -> TRUE','booleanos',1,'p_booleanos','sintactico.py',147),
  ('booleanos -> FALSE','booleanos',1,'p_booleanos','sintactico.py',148),
  ('operadoresBool -> AND','operadoresBool',1,'p_operadoresBool','sintactico.py',152),
  ('operadoresBool -> OR','operadoresBool',1,'p_operadoresBool','sintactico.py',153),
  ('operadoresEquals -> EQUALSX2','operadoresEquals',1,'p_operadoresEqual','sintactico.py',155),
  ('operadoresEquals -> NOTEQUALS','operadoresEquals',1,'p_operadoresEqual','sintactico.py',156),
  ('variables -> ID','variables',1,'p_variables','sintactico.py',158),
  ('variables -> CONSTANT','variables',1,'p_variables','sintactico.py',159),
  ('variables -> GLOBAL','variables',1,'p_variables','sintactico.py',160),
  ('asignacion -> variables EQUAL factor','asignacion',3,'p_asignacion','sintactico.py',164),
  ('asignacion -> variables EQUAL STRING','asignacion',3,'p_asignacion','sintactico.py',165),
  ('asignacion -> variables EQUAL booleanos','asignacion',3,'p_asignacion','sintactico.py',166),
  ('asignacion -> variables EQUAL struct','asignacion',3,'p_asignacion','sintactico.py',167),
  ('asignacion -> variables EQUAL operaciones','asignacion',3,'p_asignacion','sintactico.py',168),
  ('struct -> conjunto','struct',1,'p_struct','sintactico.py',175),
  ('struct -> formacion','struct',1,'p_struct','sintactico.py',176),
  ('struct -> hash','struct',1,'p_struct','sintactico.py',177),
  ('conjunto -> SET arr','conjunto',2,'p_conjunto','sintactico.py',180),
  ('conjunto -> SET LCOR RCOR','conjunto',3,'p_conjunto','sintactico.py',181),
  ('valor -> INT','valor',1,'p_valor','sintactico.py',186),
  ('valor -> STRING','valor',1,'p_valor','sintactico.py',187),
  ('valor -> booleanos','valor',1,'p_valor','sintactico.py',188),
  ('valor -> FLOAT','valor',1,'p_valor','sintactico.py',189),
  ('repetirvalor -> valor','repetirvalor',1,'p_repetirvalor','sintactico.py',192),
  ('repetirvalor -> valor COMMA repetirvalor','repetirvalor',3,'p_repetirvalor','sintactico.py',193),
  ('arr -> LCOR repetirvalor RCOR','arr',3,'p_arr','sintactico.py',198),
  ('funcionstruct -> funcionsconjunto','funcionstruct',1,'p_funcionstruct','sintactico.py',201),
  ('funcionstruct -> funcionsformacion','funcionstruct',1,'p_funcionstruct','sintactico.py',202),
  ('funcionstruct -> funcionsHash','funcionstruct',1,'p_funcionstruct','sintactico.py',203),
  ('funcionsconjunto -> conjunto PUNTO ADD LPAREN valor RPAREN','funcionsconjunto',6,'p_funcionsconjunto','sintactico.py',206),
  ('funcionsconjunto -> conjunto PUNTO ADD LPAREN arr RPAREN','funcionsconjunto',6,'p_funcionsconjunto','sintactico.py',207),
  ('funcionsconjunto -> conjunto PUNTO MERGE LPAREN conjunto RPAREN','funcionsconjunto',6,'p_funcionsconjunto','sintactico.py',208),
  ('funcionsconjunto -> conjunto PUNTO SIZE LPAREN RPAREN','funcionsconjunto',5,'p_funcionsconjunto','sintactico.py',209),
  ('funcionsconjunto -> conjunto PUNTO SIZE','funcionsconjunto',3,'p_funcionsconjunto','sintactico.py',210),
  ('contenido -> impresion','contenido',1,'p_contenido','sintactico.py',215),
  ('contenido -> asignacion','contenido',1,'p_contenido','sintactico.py',216),
  ('contenido -> funcionstruct','contenido',1,'p_contenido','sintactico.py',217),
  ('repetircontenido -> contenido','repetircontenido',1,'p_repetircontenido','sintactico.py',220),
  ('repetircontenido -> contenido SEMICOLON repetircontenido','repetircontenido',3,'p_repetircontenido','sintactico.py',221),
  ('condicion -> comparacion','condicion',1,'p_condicion','sintactico.py',224),
  ('condicion -> comparacion_bool','condicion',1,'p_condicion','sintactico.py',225),
  ('condicion -> comparacionb','condicion',1,'p_condicion','sintactico.py',226),
  ('condicion -> booleanos','condicion',1,'p_condicion','sintactico.py',227),
  ('sentenciafor -> FOR variables IN LPAREN INT PUNTO PUNTO INT RPAREN NEWLINE repetircontenido NEWLINE END','sentenciafor',13,'p_sentenciafor','sintactico.py',230),
  ('sentenciafor -> FOR variables IN LPAREN INT PUNTO PUNTO INT RPAREN NEWLINE sentenciaif NEWLINE END','sentenciafor',13,'p_sentenciafor','sintactico.py',231),
  ('sentenciafor -> FOR variables IN LPAREN INT PUNTO PUNTO INT RPAREN NEWLINE sentenciaif NEWLINE repetircontenido NEWLINE END','sentenciafor',15,'p_sentenciafor','sintactico.py',232),
  ('sentenciaif -> IF condicion NEWLINE repetircontenido NEWLINE END','sentenciaif',6,'p_sentenciaif','sintactico.py',237),
  ('sentenciaif -> IF condicion NEWLINE repetircontenido NEWLINE sentenciaelsif','sentenciaif',6,'p_sentenciaif','sintactico.py',238),
  ('sentenciaif -> IF error NEWLINE repetircontenido NEWLINE END','sentenciaif',6,'p_sentenciaif_error','sintactico.py',244),
  ('sentenciaif -> IF error NEWLINE repetircontenido NEWLINE sentenciaelsif','sentenciaif',6,'p_sentenciaif_error','sintactico.py',245),
  ('sentenciaelsif -> ELSIF condicion NEWLINE repetircontenido NEWLINE END','sentenciaelsif',6,'p_sentenciaelsif','sintactico.py',252),
  ('sentenciaelsif -> ELSIF condicion NEWLINE repetircontenido NEWLINE sentenciaelsif','sentenciaelsif',6,'p_sentenciaelsif','sintactico.py',253),
  ('sentenciaelsif -> ELSIF error NEWLINE repetircontenido NEWLINE END','sentenciaelsif',6,'p_sentenciaelsif_error','sintactico.py',258),
  ('sentenciaelsif -> ELSIF error NEWLINE repetircontenido NEWLINE sentenciaelsif','sentenciaelsif',6,'p_sentenciaelsif_error','sintactico.py',259),
  ('sentenciawhile -> WHILE condicion NEWLINE repetircontenido NEWLINE END','sentenciawhile',6,'p_sentenciawhile','sintactico.py',265),
  ('sentenciawhile -> WHILE condicion NEWLINE sentenciaif NEWLINE END','sentenciawhile',6,'p_sentenciawhile','sintactico.py',266),
  ('sentenciawhile -> WHILE error NEWLINE repetircontenido NEWLINE END','sentenciawhile',6,'p_sentenciawhile_error','sintactico.py',271),
  ('sentenciawhile -> WHILE error NEWLINE sentenciaif NEWLINE END','sentenciawhile',6,'p_sentenciawhile_error','sintactico.py',272),
  ('estructurasControl -> sentenciaif','estructurasControl',1,'p_estructurasControl','sintactico.py',278),
  ('estructurasControl -> sentenciawhile','estructurasControl',1,'p_estructurasControl','sintactico.py',279),
  ('estructurasControl -> sentenciafor','estructurasControl',1,'p_estructurasControl','sintactico.py',280),
  ('formacion -> LCOR repetirvalor RCOR','formacion',3,'p_formacion','sintactico.py',283),
  ('formacion -> LCOR RCOR','formacion',2,'p_formacion','sintactico.py',284),
  ('formacion -> ARRAY PUNTO NEW LPAREN INT RPAREN','formacion',6,'p_formacion','sintactico.py',285),
  ('formacion -> ARRAY PUNTO NEW LPAREN RPAREN','formacion',5,'p_formacion','sintactico.py',286),
  ('funcionsformacion -> formacion PUNTO LENGTH LPAREN RPAREN','funcionsformacion',5,'p_funcionsformacion','sintactico.py',291),
  ('funcionsformacion -> formacion PUNTO PUSH LPAREN repetirvalor RPAREN','funcionsformacion',6,'p_funcionsformacion','sintactico.py',292),
  ('funcionsformacion -> formacion PUNTO SAMPLE LPAREN RPAREN','funcionsformacion',5,'p_funcionsformacion','sintactico.py',293),
  ('funcionsformacion -> formacion PUNTO SAMPLE LPAREN INT RPAREN','funcionsformacion',6,'p_funcionsformacion','sintactico.py',294),
  ('funcionsformacion -> formacion PUNTO FIRST','funcionsformacion',3,'p_funcionsformacion','sintactico.py',295),
  ('funcionsformacion -> formacion PUNTO FIRST LPAREN RPAREN','funcionsformacion',5,'p_funcionsformacion','sintactico.py',296),
  ('hash -> LBRACE hash_content RBRACE','hash',3,'p_hash','sintactico.py',301),
  ('hash_elements -> hash_element hash_more_elements','hash_elements',2,'p_hash_elements','sintactico.py',306),
  ('hash_content -> hash_element','hash_content',1,'p_hash_content','sintactico.py',309),
  ('hash_content -> hash_elements','hash_content',1,'p_hash_content','sintactico.py',310),
  ('hash_element -> clave FLECHA value','hash_element',3,'p_hash_element','sintactico.py',313),
  ('hash_more_elements -> COMMA hash_element','hash_more_elements',2,'p_hash_more_elements','sintactico.py',316),
  ('hash_more_elements -> COMMA hash_element hash_more_elements','hash_more_elements',3,'p_hash_more_elements','sintactico.py',317),
  ('clave -> STRING','clave',1,'p_clave','sintactico.py',319),
  ('clave -> INT','clave',1,'p_clave','sintactico.py',320),
  ('clave -> FLOAT','clave',1,'p_clave','sintactico.py',321),
  ('value -> valor','value',1,'p_value','sintactico.py',323),
  ('value -> struct','value',1,'p_value','sintactico.py',324),
  ('hash_add -> hash PUNTO STORE LPAREN clave COMMA value RPAREN','hash_add',8,'p_hash_store','sintactico.py',327),
  ('hash_delete -> hash PUNTO DELETE LPAREN clave RPAREN','hash_delete',6,'p_hash_delete','sintactico.py',330),
  ('hash_key -> hash PUNTO KEY LPAREN value RPAREN','hash_key',6,'p_hash_key','sintactico.py',333),
  ('funcionsHash -> hash_add','funcionsHash',1,'p_funcionsHash','sintactico.py',336),
  ('funcionsHash -> hash_delete','funcionsHash',1,'p_funcionsHash','sintactico.py',337),
  ('funcionsHash -> hash_key','funcionsHash',1,'p_funcionsHash','sintactico.py',338),
]
