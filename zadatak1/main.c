#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    FILE* fp = fopen ("datoteka.txt", "w+");
    char niz[20];
    char kahraktehr;
    int b = 0, i;
    printf("Unesite niz karaktera: ");
    scanf("%s", niz);
    getchar();
    fprintf(fp, "%s", niz);
    printf("Unesite trazeni karakter: ");
    scanf("%c", &kahraktehr);
    fseek(fp,0,SEEK_SET);
    int n = strlen(niz);
    for(i = 0; i < n; i++){
        if (kahraktehr == fgetc(fp)){
            b++;
        }
    }

    printf("Karakter se pojavljuje %d puta", b);


    return 0;
}
