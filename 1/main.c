#include <stdio.h>
#include <stdlib.h>

int main()
{
    int brk, i, j;
    double a;
    printf("Unesite dimenzije matrice: ");
    scanf("%d", &brk);
    double m[brk][brk];
    for(i=0;i<brk;i++){
        for(j=0;j<brk;j++){
            scanf("%lf",&m[i][j]);
        }
    }

    for(i=0;i<brk;i++){
        for(j=0;j<brk;j++){
           a=m[i][j];
           m[i][j]=m[j][i];
           m[j][i]=a;
                }
    }
    for(i=0;i<brk;i++){
        for(j=0;j<brk;j++){
            printf("%.2lf ",m[j][i]);
        }printf("\n");
    }
    return 0;
}
