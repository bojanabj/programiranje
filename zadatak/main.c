#include <stdio.h>
#include <stdlib.h>

int main(){

    char podatki[30];
    FILE *fp;

    fp=fopen("podatki.txt","w+");

    if(fp==NULL){
        printf("Greska.");
        return 1;
    }
    printf("Unesite ime, prezime i broj u dnevniku:\n");
    fgets(podatki,sizeof(podatki),stdin);
    fprintf(fp,"%s",podatki);
    fclose(fp);

    return 0;
}
