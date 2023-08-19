#include <stdio.h>
#include <stdlib.h>
 

int main(int argc, char* argv[]) {
 
 int n, i, check = 0;
 
    n = atoi(argv[1]);

    printf("Numero inserido: %d",n);

    for(i=2;i<n;i++){
        if(n % i == 0){
            check = 1;
            break;
        }
    }

    if(check==0){
        printf("\nO numero %d eh primo",n);
    } else {
        printf("\nO numero %d nao eh primo",n);
    }



/*
    estrutura do argv serve como scanf mais simplificado, colocar depois do .exe
    sempre usar com #include <stdlib.h>
*/
 
    return 0;
}









