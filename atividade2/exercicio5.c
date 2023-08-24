#include <stdio.h>

// Função para multiplicar elementos de dois arrays
void multiplica_array(int arr1[], int arr2[], int resultado[], int tamanho) {
	int i;
    for (i = 0; i < tamanho; i++) {
        resultado[i] = arr1[i] * arr2[i];
    }
}

int main() {

    setlocale(LC_ALL, “Portuguese”);

    int tamanho, i;
    printf("Digite o tamanho dos arrays: ");
    scanf("%d", &tamanho);

    int array1[tamanho], array2[tamanho], resultado[tamanho];
    printf("Digite os elementos do primeiro array:\n");
    for (i = 0; i < tamanho; i++) {
        scanf("%d", &array1[i]);
    }
    printf("Digite os elementos do segundo array:\n");
    for (i = 0; i < tamanho; i++) {
        scanf("%d", &array2[i]);
    }

    multiplica_array(array1, array2, resultado, tamanho);

    printf("Resultado da multiplicação dos arrays:\n[");
    for (i = 0; i < tamanho; i++) {
        printf("%d", resultado[i]);
        if (i != tamanho - 1) {
            printf(", ");
        }
    }
    printf("]\n");

    return 0;
}
