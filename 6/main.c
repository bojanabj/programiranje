#include <stdio.h>
#include <stdlib.h>

void km(int brk,int brv, int* m){
    int i,j;
    for(i=0;i<brk;i++){
        for(j=0;j<brv;j++)
            scanf("%d", m+i*(brv)+j);

    }
}

void ispm(int* z, int brk, int brv){
    int i,j;
    for(i=0;i<brk;i++){
        for(j=0;j<brv;j++){
            printf("%d ", *(z+i*brv+j));
        }

        printf("\n");
        }
}
void sabm(int* m,int* n, int* z, int brk, int brv){
    int i,j;
    for(i=0;i<brk;i++){
        for(j=0;j<brv;j++){
            *(z+i*brv+j)=*(m+i*brk+j)+*(n+i*brv+j);
        }
}
}

int main()
{
    int brk,brv;
    scanf("%d%d",&brk,&brv);
    int m[brk][brv], n[brk][brv], z[brk][brv];
    km(brk, brv, m);
    km(brk, brv, n);
    sabm(m, n, z, brk, brv);
    ispm(z, brk, brv);

    return 0;
}
