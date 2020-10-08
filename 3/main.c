#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int fja(char *str, char c){
    int i,br,a=0;
    br=strlen(str);
    for(i=0;i<br;i++){
        if(c==str[i]){
          a++;
        }
    }return a;
}
int main()
{
    char c, str[20];
    scanf("%c",&c);
    scanf("%s",&str);
    printf("%d", fja(str, c));
    return 0;
}
