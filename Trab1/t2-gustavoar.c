#include <stdio.h>
#include <stdlib.h>

typedef struct cab
{
    struct no *primNo;
    int tamanho;
} No_cabeca;

typedef struct no
{
    int info;
    struct no *prox;
} No_lista;

typedef No_cabeca Lista;

void inic_vet(Lista vet_cab[], int tamanho)
{
    int i;

    for (i = 0; i < tamanho; i++)
    {
        vet_cab[i].primNo = NULL;
    }
}

void listaAdj(Lista vet_cab[], int tamanho)
{
	int i;
	No_lista *aux;

	printf("\n");

	for(i = 0; i < tamanho; i++)
	{
		aux = vet_cab[i].primNo;

		printf("%d | ", i);

		while(aux != NULL)
		{
			printf("%d ", aux->info);
			aux = aux->prox;
		}

		printf("\n");
	}
}

void insereInicio(Lista *p_l, int p)
{
    No_lista *aux = p_l->primNo;
    No_lista *novo = NULL;

    novo = malloc(sizeof(No_lista));
    if(novo == NULL)
    {
        printf("Bad Alloc!\n");
    }

    //Inicialização do novo vetor criado
    novo->prox = NULL;
    novo->info = p;


   	novo->prox = p_l->primNo;
    p_l->primNo = novo;
}

int main()
{
	Lista **adj;
	No_lista *adjacente;
	char *cor;
	int *distancia, *predecessor, *fila;
	int qtdPessoas, qtdRelacoes;
	int i,j;
	int temp;
	int atual;
	int maior = 0;
	int inicio, fim;

	scanf("%d %d", &qtdPessoas, &qtdRelacoes);

	while(qtdPessoas != 0 || qtdRelacoes != 0)
	{
		//inicializa tudo
		cor = malloc(qtdPessoas * sizeof(char));
		distancia = malloc(qtdPessoas * sizeof(int));
		predecessor = malloc(qtdPessoas * sizeof(int));
		fila = malloc(qtdPessoas * sizeof(int));
		adj = malloc(qtdPessoas * sizeof(Lista **));
		for(temp=0; temp < qtdPessoas; temp++)
		{
			adj[temp] = malloc(sizeof(Lista *));
		}

		inic_vet(*adj,qtdPessoas);

		i = 0;
		maior = 0;
		j = 0;
		atual = 0;
		temp = 0;
		inicio = fim = 0;

		//recebe as relações
		for(temp = 0; temp < qtdRelacoes; temp++)
		{
			scanf("%d %d", &i, &j);
			insereInicio((*adj+i), j);
			insereInicio((*adj+j), i);
		}

		//algoritmo de busca
		//inicializa as variáveis
		for(temp = 0; temp < qtdPessoas; temp++)
		{
			distancia[temp] = 1001;
			predecessor[temp] = -1;
			cor[temp] = 'b';
		}

		//preenche a raiz
		distancia[0] = 0;
		predecessor[0] = 0;
		cor[0] = 'c';

		fila[0] = 0;
		fim++;

		while(inicio != fim)
		{
			atual = fila[inicio];
			inicio++;
			adjacente = ((*adj)+atual)->primNo;

			while(adjacente != NULL)
			{
				if(cor[adjacente->info] == 'b')
				{
					distancia[adjacente->info] = distancia[atual] + 1;
					cor[adjacente->info] = 'c';
					predecessor[adjacente->info] = atual;
					fila[fim] = adjacente->info;
					fim++;
				}

				adjacente = adjacente->prox;
			}
			cor[atual] = 'p';
		}

		for(temp = 0; temp < qtdPessoas; temp++)
		{
			if(maior < distancia[temp])
			{
				maior = distancia[temp];
			}
		}

		if(maior == 1001)
		{
			printf("infinito\n");
		}
		else
		{
			printf("%d\n", maior);
		}

		scanf("%d %d\n", &qtdPessoas, &qtdRelacoes);
	}
}