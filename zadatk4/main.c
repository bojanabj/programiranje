#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *fp1 = fopen("f1ulaz.txt", "w+");
    FILE *fp2 = fopen("f2ulaz.txt", "w+");
    FILE *fp3 = fopen("f3.txt", "w+");
    char c;

    if (fp1 == NULL || fp2 == NULL || fp3 == NULL) {
        puts("Neuspesno otvaranje fajlova.");
        exit(0);
    }

    while ((c = fgetc(fp1)) != EOF
        fputc(c, fp3);

    while ((c = fgetc(fp2)) != EOF)
        fputc(c, fp3);

    printf("Fajl 1 i 2 su spojeni u fajl 3");

    fclose(fp1);
    fclose(fp2);
    fclose(fp3);
    return 0;
}
