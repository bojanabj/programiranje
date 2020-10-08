#include <stdio.h>
#include <stdlib.h>

int jednaki(char *s1, char *s2){
    int i,br;
    if(strlen(s1)!=strlen(s2)){
        return 0;
    }else{
        br=strlen(s1);
        for(i=0;i<br;i++){
            if(s1[i]!=s2[i]){
                return 0;
            }
        }
    }
    return 1;
}

int main()
{
    char s1[20], s2[20];
    fflush(stdin);
    gets(s1);
    fflush(stdin);
    gets(s2);
    if(jednaki(s1, s2)==1)
        printf("jednaki");
    else
        printf("nisu jednaki");
    return 0;
}
