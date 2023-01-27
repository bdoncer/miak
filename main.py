import antlr4
import os
import sys

from gen.pseudoPythonLexer import pseudoPythonLexer
from gen.pseudoPythonParser import pseudoPythonParser
from gen.pseudoPythonVisitor import pseudoPythonVisitor


def main():
    pseudocode = '''
x <- 1;
if (x = 1){
	y<-2;
} else {
	y<-3;
}
function my_print(x){
	for (i <- 1...5){
		print(i);
	}
	return true;
}
my_print(5);
arr <- [1,2,3];
arr[1] <- 5;
z <- arr[2];
'''
    data = antlr4.InputStream(pseudocode)

    lexer = pseudoPythonLexer(data)
    stream = antlr4.CommonTokenStream(lexer)
    parser = pseudoPythonParser(stream)
    tree = parser.program()
    visitor = pseudoPythonVisitor()
    visitor.visit(tree)

    with open('code.py', 'w') as file:
        file.write(visitor.code)


if __name__ == '__main__':
    main()
