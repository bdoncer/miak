grammar pseudoPython;


ASSIGN: '<-';
IF_TOKEN = 'if'
ELSE_TOKEN = 3
WHILE_TOKEN = 4
FOR_TOKEN = 5
RETURN_TOKEN = 6
AND_TOKEN = 7
OR_TOKEN = 8
SKIP = 9
NOT_TOKEN = 10
CURLY_BRACKET_BEGIN = 11
CURLY_BRACKET_END = 12
ROUND_BRACKET_BEGIN = 13
ROUND_BRACKET_END = 14
SQUARE_BRACKET_BEGIN = 15
SQUARE_BRACKET_END = 16
QUOTATION_MARK = 17
COMPARISON_OPERATORS = 18
MATH_OPERATORS = 19
COMMA = 20
BETWEEN = 21
WHITESPACE: [ \t\r\n] -> skip;
ERROR = 24
BOOLEAN = 25
ID = 26
NUMBER = 27
SEMICOLON = 28
FUNCTION = 29
STRING = 31



//TODO
program_all: ;

for_statement: for_token round_bracket_begin id assign (id | number) between (id | number) round_bracket_end curly_bracket_begin (statement | skip)+ curly_bracket_end;

while_statement: while_token round_bracket_begin expression round_bracket_end curly_bracket_begin (statement | skip)+ curly_bracket_end;

if_statement: if_token round_bracket_begin expression round_bracket_end curly_bracket_begin (statement | skip)+ curly_bracket_end (else_token  curly_bracket_begin  (statement | skip)+ curly_bracket_end)?;

return_statement: return_token variable_type semicolon;

function_def: function_token id round_bracket_begin (id(comma | id)*)? round_bracket_end curly_bracket_begin (statement)+  (return_statement)? curly_bracket_end;

array: square_bracket_begin variable_type (comma|variable_type)* square_bracket_end;

expression: (not? (variable_type | and_expression | or_expression | comparision_operators_expression | math_operators_expression));

statement: (for_statement | while_statement | if_statement | return_statement | declaration | function_call | function_definition);

and_expression: expression and_token expression;

or_expression: expression or_token expression;

comparision_operators_expression: expression comparision_operator expression;

math_operators_expression: expression math_operator expression;

declaration: id assign variable_type semicolon;

function_call:  id round_bracket_begin (variable_type (comma | variable_type)*)? round_bracket_end semicolon;

variable_type: (boolean | id | number | array | string | array_element);

array_element: id square_bracket_begin variable_type square_bracket_end;
