import os
import sys

import antlr4

from gen.pseudoPythonLexer import pseudoPythonLexer
from gen.pseudoPythonParser import pseudoPythonParser
from gen.pseudoPythonVisitor import pseudoPythonVisitor


def main():
    # if len(sys.argv) != 2 or not (input_file_name := sys.argv[1]):
    #     print("Incorrect arguments")
    #     return

    # with open(input_file_name, 'r') as file:
    #     data = antlr4.InputStream(file.read())

    data = antlr4.InputStream('''
x <- 1;
if (x = 1){
	y<-2;
} else {
	y<-3;
}
function my_print(x){
	for (i <- 1...x){
		print(i);
	}
	return true;
}
my_print(5);
arr <- [1,2,3];
arr[1] <- 5;
z <- arr[2];
''')

    lexer = pseudoPythonLexer(data)
    stream = antlr4.CommonTokenStream(lexer)
    parser = pseudoPythonParser(stream)
    tree = parser.program()
    visitor = pseudoPythonVisitor()
    visitor.visit(tree)

    print(visitor.code)

if __name__ == '__main__':
    main()