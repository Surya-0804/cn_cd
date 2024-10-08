%{
#include <stdio.h>
#include <stdlib.h>
void yyerror(char *s);   // Error handling function declaration.
int yylex(void);         // Tokenizer function (from Lex).
int sym[26];             // Array to store variable values (single-letter variables like 'a', 'b').
%}

%token INTEGER VARIABLE  // Token definitions, for numbers and variables.

%left '+'                // Left-associative operators.
%left '*'

%%
PROG:
    PROG STMT           // Program is a sequence of statements.
    | STMT              // A program can also be just a single statement.
    ;

STMT:
    VARIABLE '=' EXPR    { sym[$1 - 'a'] = $3; }  // Assign result of expression to a variable.
    | EXPR               { printf("Result: %d\n", $1); }  // Print the result of the expression.
    ;

EXPR:
    INTEGER              { $$ = $1; }  // Return the value of an integer.
    | VARIABLE           { $$ = sym[$1 - 'a']; }  // Get the value of a variable.
    | EXPR '+' EXPR      { $$ = $1 + $3; }  // Addition.
    | EXPR '*' EXPR      { $$ = $1 * $3; }  // Multiplication.
    | '-' EXPR           { $$ = -$2; }  // Negation (e.g., -3).
    ;
%%

void yyerror(char *s) {
    fprintf(stderr, "Error: %s\n", s);  // Print error messages.
}

int main(void) {
    printf("Enter the Expression:\n");
    yyparse();  // Start parsing the input.
    return 0;
}
