#include <stdio.h>
#include <string.h>

// Função para verificar se uma string existe em um array de strings
int busca_string(char *arr[], int tamanho, char *busca) {
	int i;
    for (i= 0; i < tamanho; i++) {
        if (strcmp(arr[i], busca) == 0) {
            return 1; // A string foi encontrada no array
        }
    }
    return 0; // A string não foi encontrada no array
}

int main() {

    setlocale(LC_ALL, “Portuguese”);

    int tamanho, i;
    printf("Digite o tamanho do array: ");
    scanf("%d", &tamanho);

    char *array[tamanho];
    printf("Digite as strings do array:\n");
    for (i= 0; i < tamanho; i++) {
        char temp[100]; // Tamanho máximo da string
        scanf("%s", temp);
        array[i] = strdup(temp);
    }

    char busca[100];
    printf("Digite a string de busca: ");
    scanf("%s", busca);

    int resultado = busca_string(array, tamanho, busca);
    printf("Resultado da busca: %d\n", resultado);

    // Libera a memória alocada para cada string no array
    for (i = 0; i < tamanho; i++) {
        free(array[i]);
    }

    return 0;
}
