#linux:

$ lex calc.l

$ yacc -d calc.y

$ cc y.tab.c lex.yy.c -II -ly -1m

$./a. out


#windows
flex calc.l

bison -dy calc.y

gcc lex.yy.c y.tab.c -o calc.exe -ll


Enter the Expression: ( 5 +4) *3

Answer: 27
