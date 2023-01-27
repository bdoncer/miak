grammar pseudoPython;


ASSIGN: '<-';
IF_TOKEN: 'if';
ELSE_TOKEN: 'else';
WHILE_TOKEN: 'while';
FOR_TOKEN: 'for';
RETURN_TOKEN: 'return';
AND_TOKEN: 'and';
OR_TOKEN: 'or';
SKIP_TOKEN: 'skip';
NOT_TOKEN: 'not';
FUNCTION_TOKEN: 'function';
CURLY_BRACKET_BEGIN: '{';
CURLY_BRACKET_END: '}';
ROUND_BRACKET_BEGIN: '(';
ROUND_BRACKET_END: ')';
SQUARE_BRACKET_BEGIN: '[';
SQUARE_BRACKET_END: ']';
COMPARISON_OPERATORS: '=' | '>=' | '<=' | '<' | '>' | '!=';
MATH_OPERATORS: '+' | '-' | '*' | '/' | '%' | '^';
COMMA: ',';
BETWEEN: '...';
WHITESPACE: [ \t\r\n] -> skip;
//ERROR = 24
BOOLEAN: 'true' | 'false';
ID: ([a-zA-Z] | '_') ([a-zA-Z0-9] | '_')*;
NUMBER: ('-')?[0-9]+;
SEMICOLON: ';';
STRING: '"'[a-zA-Z0-9 \t\r\n]+'"';




program: start* EOF;

start: statement;

for_statement: FOR_TOKEN ROUND_BRACKET_BEGIN ID ASSIGN (ID | NUMBER) BETWEEN (ID | NUMBER) ROUND_BRACKET_END CURLY_BRACKET_BEGIN (statement | SKIP_TOKEN)+ CURLY_BRACKET_END;

while_statement: WHILE_TOKEN ROUND_BRACKET_BEGIN expression ROUND_BRACKET_END CURLY_BRACKET_BEGIN (statement | SKIP_TOKEN)+ CURLY_BRACKET_END;

if_statement: IF_TOKEN ROUND_BRACKET_BEGIN expression ROUND_BRACKET_END CURLY_BRACKET_BEGIN (statement | SKIP_TOKEN)+ CURLY_BRACKET_END (ELSE_TOKEN  CURLY_BRACKET_BEGIN  (statement | SKIP_TOKEN)+ CURLY_BRACKET_END)?;

return_statement: RETURN_TOKEN variable_type SEMICOLON;

function_definition: FUNCTION_TOKEN ID ROUND_BRACKET_BEGIN (ID(COMMA | ID)*)? ROUND_BRACKET_END CURLY_BRACKET_BEGIN (statement)+  (return_statement)? CURLY_BRACKET_END;

array: SQUARE_BRACKET_BEGIN variable_type (COMMA|variable_type)* SQUARE_BRACKET_END;

//expression: (NOT_TOKEN? (variable_type | and_expression | or_expression | comparision_operators_expression | math_operators_expression));
expression: (NOT_TOKEN? variable_type (AND_TOKEN | OR_TOKEN | COMPARISON_OPERATORS | MATH_OPERATORS) (variable_type | expression));

statement: (for_statement | while_statement | if_statement | return_statement | declaration | function_call | function_definition);

//and_expression: expression AND_TOKEN expression;
//
//or_expression: expression OR_TOKEN expression;
//
//comparision_operators_expression: expression COMPARISON_OPERATORS expression;
//
//math_operators_expression: expression MATH_OPERATORS expression;

declaration: ID (SQUARE_BRACKET_BEGIN NUMBER SQUARE_BRACKET_END)? ASSIGN variable_type SEMICOLON;

function_call:  ID ROUND_BRACKET_BEGIN (variable_type (COMMA | variable_type)*)? ROUND_BRACKET_END SEMICOLON;

variable_type: (BOOLEAN | ID | NUMBER | array | STRING | array_element);

array_element: ID SQUARE_BRACKET_BEGIN variable_type SQUARE_BRACKET_END;
