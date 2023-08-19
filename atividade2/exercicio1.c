#include <stdio.h>
#include <stdlib.h>




    int main(int argc, char* argv[]){

        int v[4] = {5, 7, 9, 6};
        int soma;

        //tem q ser dentro de um for
        //soma = v[0] + v[1] + v[2] + v[3];


        for(soma = 0; soma < sizeof(v)/sizeof(int); soma++){
            for(v; v < soma ; v++){
            printf("%d",soma);
            }
        }



        return 0;
    }