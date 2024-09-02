#include <stdio.h>
#include <string.h>

//define a estrutura Livro:

struct Livro
{
	char titulo[80];
	int ano;
};

int main()
{
	struct Livro x;
	
	strcpy(x.titulo, "Cem Anos de Solidao");
	x.ano = 1967;
	
	printf("Livro: %s (%d).\n", x.titulo, x.ano);
	
	struct Livro y = { "Ensaio sobre a Cegueira", 1995};
	
	printf("Livro: %s (%d).\n", y.titulo, y.ano);
	
	y.ano = 2005;
	//y.titulo = "As Intermitencias da Morte";
	strcpy(y.titulo, "As Intermitencias da Morte");
	
	printf("Livro: %s (%d).\n", y.titulo, y.ano);
	
	return 0;
}
