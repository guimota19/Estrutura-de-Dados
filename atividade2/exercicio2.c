#include <stdio.h>

// Função para encontrar o menor e o maior elemento de um array
void menor_maior_array(int arr[], int tamanho, int *menor, int *maior) {
    *menor = arr[0];
    *maior = arr[0];
    
    int i;

    for (i = 1; i < tamanho; i++) {
        if (arr[i] < *menor) {
            *menor = arr[i];
        }
        if (arr[i] > *maior) {
            *maior = arr[i];
        }
    }
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

    int menor, maior;
    menor_maior_array(array, tamanho, &menor, &maior);
    printf("O menor elemento do array é: %d\n", menor);
    printf("O maior elemento do array é: %d\n", maior);

    return 0;
}
