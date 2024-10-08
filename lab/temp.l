#include<stdio.h>
void yyerror(char *s);
#include "y.tab.h";

int yylval;

%%
[a-zA-Z] {return VARIABLE;}
[0-9]+ {yylval=atoi(yytext); return INTEGER;}
"+" {return "+"}
'*'   {return "*"};
'-'   {return "-"};
'/'   {return "/"};
%%

int yywrap(void){
    return 1;
}