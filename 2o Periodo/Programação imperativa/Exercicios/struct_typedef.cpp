#include <stdio.h>

// define uma estrutura anônima
// e a nomeia como Livro:

typedef
	struct
	{
		char titulo[80];
		int ano;
	}
	Filme;

int main()
{
	Filme x;
	
	printf("Digite um titulo (sem espacos): ");
	scanf("%s", x.titulo);
	
	printf("Digite um ano: ");
	scanf("%d", &(x.ano));
	
	printf("Filme: %s (%d).\n", x.titulo, x.ano);
	
	return 0;
}
