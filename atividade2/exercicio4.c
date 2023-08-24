#include <stdio.h>

// Função para contar a quantidade de ocorrências de um número em um array
int conta_int_array(int arr[], int tamanho, int busca) {
    int contador = 0;
    int i;
    for (i = 0; i < tamanho; i++) {
        if (arr[i] == busca) {
            contador++;
        }
    }
    return contador;
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

    int busca;
    printf("Digite o numero de busca: ");
    scanf("%d", &busca);

    int resultado = conta_int_array(array, tamanho, busca);
    printf("Quantidade de ocorrencias: %d\n", resultado);

    return 0;
}
