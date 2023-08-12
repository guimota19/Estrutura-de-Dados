#include <stdio.h>

double calcular_dob(double n ){
    return n * 2;
}


int main(int argc, char* argv[]){
    int n = 11;
    int n2 = 0;
    float f1 = 1.5;
    double d1= 1.555555;
    char letra = 'j';


    if(n2){
        printf("0 e verdadeiro\n");
    }
    if(n){
        printf("-11 e verdadeiro\n");
    }
    printf("\n");
    for(n = 0; n < 10; n++){
        printf("%d", n);
    }
    printf("\n");

    n = 0;
    do{
        printf("%d", n);
        n++;
    } while (n < 10);

    printf("O dobro de %f eh %f", d1, calcular_dob(d1));













  
}




