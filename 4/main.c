#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n,i;
    scanf("%d",&n);
    int niz[n];
    for(i=0;i<n;i++){
        scanf("%d",niz+i);
    }
    int a;
    for(i=0;i<n;i++){
        if(i==0)
            a=*(niz+i);
        else if(a<=*(niz+i))
            a=*(niz+i);
    }
    printf("%d", a);
    return 0;
}
