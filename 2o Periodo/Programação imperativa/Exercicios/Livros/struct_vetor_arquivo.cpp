#include <stdio.h>

#define MAX 10

typedef
	struct
	{
		char titulo[80];
		int ano;
	}
	Livro;

int main(){
	
	FILE* arquivo = fopen("Livros.txt", "r");
	
	Livro livros[MAX];
	
	int quantidade;
	fscanf(arquivo, "%d", &quantidade);
	
	for (int i = 0; i < quantidade; i++)
	{
		fscanf(arquivo, "%s", livros[i].titulo);
		fscanf(arquivo, "%d", &(livros[i].ano));
	}
	
	fclose(arquivo);
	
	for (int i = 0; i < quantidade; i++)
	{
		printf("Livro: %s (%d).\n",
		livros[i].titulo, livros[i].ano);
	}
}
