#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n,i;
    scanf("%d", &n);
    int niz[n];
    for(i=0;i<n;i++){
        scanf("%d", niz+i);
    }
    for(i=0;i<n;i++){
        if(*(niz+i)%3==0)
            printf("%d ", *(niz+i));
    }
    return 0;
}
