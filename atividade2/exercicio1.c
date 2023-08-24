#include <stdio.h>
#include <stdlib.h>

int soma_array(int arr[], int tamanho) {
    int i, soma = 0;
    for (i = 0; i < tamanho; i++) {
        soma += arr[i];
    }
    return soma;
}

int main() {

    setlocale(LC_ALL, “Portuguese”);
	
    int tamanho, i;
    
    printf("Digite o tamanho do array: ");
    scanf("%d", &tamanho);

    int array[tamanho];
    printf("Digite os elementos do array:\n");
    for (i = 0; i < tamanho; i++) {
        scanf("%d", &array[i]);
    }

    int resultado = soma_array(array, tamanho);
    printf("A soma dos elementos do array e: %d\n", resultado);

    return 0;
    }