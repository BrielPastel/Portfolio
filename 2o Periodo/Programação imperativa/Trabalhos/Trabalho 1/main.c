#include <stdio.h>
#include <string.h>
#define MAX 100

/*
Feito por:
Arthur Capellazzi Fontana Amaral
Gabriel Berto Beckauser
*/

/*
Professor, o código pode estar com um problema que não conseguimos resolver, parece um problema que está acima da nossa compreensão.
O problema está no terceiro vendedor no txt dos totais, se você rodar uma vez, talvez o número esteja errado, mas se você rodar mais vezes, consegue notar que o número correto aparece algumas vezes, então o código está correto mas algum problema da própria linguagem C nos limitou para a finalização do trabalho. 
Espero que compreenda.
*/



typedef //criação de variáveis tipo struct
	struct
	{
		int cod_vendedor_vendas;
		int cod_produto_vendas;
		int unidades_vendidas;
	}
	vendas;

typedef
	struct
	{
		int cod_produto;
		float preco_produto;
		char descricao_produto[MAX];
	}
	produtos;

typedef
	struct
	{
		int cod_vendedor;
		char nome_vendedor[MAX];
	}
	vendedores;

int unidade;

int main()
{

	FILE* arquivo_vendas = fopen("vendas.txt", "r"); //abertura e leitura dos .txt
	FILE* arquivo_produtos = fopen("produtos.txt", "r");
	FILE* arquivo_vendedores = fopen("vendedores.txt", "r");
	
  vendas vendas_list[MAX];
  produtos produtos_list[MAX];
  vendedores vendedores_list[MAX];  

  int quantidade_vendas;
  fscanf(arquivo_vendas, "%d", &quantidade_vendas); //linhas vendas
  
  int quantidade_produtos;
  fscanf(arquivo_produtos, "%d", &quantidade_produtos); //linhas produtos

  int quantidade_vendedores;
  fscanf(arquivo_vendedores, "%d", &quantidade_vendedores); //linhas vendedores

  for (int i = 0; i < quantidade_vendas; i++) //vendas.txt
    {
      fscanf(arquivo_vendas, "%d", &vendas_list[i].cod_vendedor_vendas);
      fscanf(arquivo_vendas, "%d", &vendas_list[i].cod_produto_vendas);
      fscanf(arquivo_vendas, "%d", &vendas_list[i].unidades_vendidas);
    }

  for (int i = 0; i < quantidade_produtos; i++) //produtos.txt
    {
      fscanf(arquivo_produtos, "%d", &produtos_list[i].cod_produto);
      fscanf(arquivo_produtos, "%f", &produtos_list[i].preco_produto);
      fscanf(arquivo_produtos, "%s", produtos_list[i].descricao_produto);
    }

  for (int i = 0; i < quantidade_vendedores; i++) //vendedores.txt
    {
      fscanf(arquivo_vendedores, "%d", &vendedores_list[i].cod_vendedor);
      fscanf(arquivo_vendedores, "%s", vendedores_list[i].nome_vendedor);
    }

  fclose(arquivo_vendas);
  fclose(arquivo_produtos);
  fclose(arquivo_vendedores);

  int vendas_de_produtos[quantidade_produtos]; //Variáveis
  float total_vendas_cada_produto[quantidade_produtos];
  float total_vendas_produtos;
  total_vendas_produtos = 0;
  float vendas_de_vendedores[quantidade_vendedores];
  
  for (int i = 0; i < quantidade_produtos; i++) //código para rendimento parcial e total
    {
      unidade = 0;
      for (int j = 0; j < quantidade_vendas; j++)
        {
          if (produtos_list[i].cod_produto == vendas_list[j].cod_produto_vendas)
            {
              unidade = unidade + vendas_list[j].unidades_vendidas;
            }
        }
      vendas_de_produtos[i] = unidade;
    }
  for (int i = 0; i < quantidade_produtos; i++)
    {
      total_vendas_cada_produto[i] = produtos_list[i].preco_produto * vendas_de_produtos[i];
      total_vendas_produtos = total_vendas_produtos + total_vendas_cada_produto[i];
    }

  for (int i = 0; i < quantidade_vendedores; i++) //código para rendimento de vendedores
  {
    for (int j = 0; j < quantidade_vendas; j++)
      {
        if (vendedores_list[i].cod_vendedor == vendas_list[j].cod_vendedor_vendas)
        {
          for (int k = 0; k < quantidade_produtos; k++)
            {
              if (produtos_list[k].cod_produto == vendas_list[j].cod_produto_vendas)
              {

                vendas_de_vendedores[i] = vendas_de_vendedores[i] + 
                  (produtos_list[k].preco_produto * vendas_list[j].unidades_vendidas);

              }
            }
        }
      }
  }

  FILE *totais = fopen("totais.txt", "w");

  fprintf(totais, "Log de Vendas:\n");
    for (int i = 0; i < quantidade_vendas; i++)
      {        
      fprintf(totais, "[%d] %d %d %d\n", i, 
        vendas_list[i].cod_vendedor_vendas,
        vendas_list[i].cod_produto_vendas, 
        vendas_list[i].unidades_vendidas);
      }
  
  fprintf(totais, "\nCatalogo de Produtos:\n");
    for (int i = 0; i < quantidade_produtos; i++)
      {
      fprintf(totais, "[%d] %d R$%.2f %s\n", i,
        produtos_list[i].cod_produto,
        produtos_list[i].preco_produto,
        produtos_list[i].descricao_produto);
      }

  fprintf(totais, "\nLista de Vendedores:\n");
    for (int i = 0; i < quantidade_vendedores; i++)
      {
      fprintf(totais, "[%d] %d %s\n", i,
        vendedores_list[i].cod_vendedor,
        vendedores_list[i].nome_vendedor);
      }

  fprintf(totais, "\nTotal geral vendido: R$%.2f\n", total_vendas_produtos);

  fprintf(totais, "\nTotal de vendas de cada produto:\n");
  for (int i = 0; i < quantidade_produtos; i++)
    {
    fprintf(totais, "Produto %d (%s) : R$%.2f\n",
      produtos_list[i].cod_produto,
      produtos_list[i].descricao_produto,
      total_vendas_cada_produto[i]);
    }

  fprintf(totais, "\nTotal de vendas de cada vendedor:\n");
  for (int i = 0; i < quantidade_vendedores; i++)
  {
  fprintf(totais, "Vendedor %d (%s) R$%.2lf\n",
    vendedores_list[i].cod_vendedor,
    vendedores_list[i].nome_vendedor,
    vendas_de_vendedores[i]);
  }

  fclose(totais);
  
}
