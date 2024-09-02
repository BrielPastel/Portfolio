import sys
import random
from Memoria import MemoriaPrincipal
from Memoria import MemoriaSecundaria
from Memoria import testaMapeamento

tabMapeamento = [-1, -1, -1, -1, -1, -1, -1, -1]
tabHistorico = []
numeroHistorico = 0

# Parametros:
#    memoriaPrincipal: memoria Cache, a pagina solicitada deve estar na memoriaPrincipal
#    memoriaSecundaria: memoria secundaria que possui todas as paginas
#    endereco: endereco da pagina requisitada
# Retorno
#    endereco que a pagina requisitada se encontra na memoriaPrincipal
# Altere a funcao para fazer uso da tecnica de mapeamento associativo
def mapeamentoAssociativo(memoriaPrincipal: MemoriaPrincipal, memoriaSecundaria: MemoriaSecundaria, endereco: int) -> int:
    #quantidade de paginas em cada memoria =)
    qtPaginasMemoriaPrincipal = memoriaPrincipal.qtPaginas
    qtPaginasMemoriaSecundaria = memoriaSecundaria.qtPaginas

    paginaRequisitada = endereco >> 2
    byteRequisitado = endereco & 3

    # descobrir se eu ja mapeei a pagina, se sim retornar o endereco da primario
    for i in range(len(tabMapeamento)):
        if tabMapeamento[i] == paginaRequisitada:
            return i

    # caso nao tenha mapeado
    pagina = memoriaSecundaria.getPagina(paginaRequisitada)
    # procurar espaco vazio na cache, e mapear

    for i in range(len(tabMapeamento)):
        if tabMapeamento[i] == -1:
            memoriaPrincipal.setPagina(pagina, i)
            tabMapeamento[i] = paginaRequisitada
            return i

    # se nao tiver espaco vazio, remover alguem e mapear
        
    memoriaPrincipal.setPagina(pagina, 0)
    tabMapeamento[0] = paginaRequisitada



    #retorna endereco
    return 0

#Utilize esta funcao caso precise inicializar alguma variavel para o mapeamento =)
def inicializaMapeamento(memoriaPrincipal: MemoriaPrincipal, memoriaSecundaria: MemoriaSecundaria):
    #quantidade de paginas em cada memoria =)
    qtPaginasMemoriaPrincipal = memoriaPrincipal.qtPaginas
    qtPaginasMemoriaSecundaria = memoriaSecundaria.qtPaginas


if __name__ == '_main_':

    #executa funcao de mapeamento com 30 enderecos em modo Debug
    testaMapeamento(nEnderecos=30, 
                               nPaginasMemoriaPrincipal=8, 
                               nPaginasMemoriaSecundaria=16, 
                               debug=True, 
                               funcaoMapeamento=mapeamentoAssociativo,
                               funcaoInicializacaoMapeamento=inicializaMapeamento)

    #executa a funcao sem modo debug
    testaMapeamento(nEnderecos=30000, 
                               nPaginasMemoriaPrincipal=1024, 
                               nPaginasMemoriaSecundaria=4096, 
                               debug=False, 
                               funcaoMapeamento=mapeamentoAssociativo, 
                               funcaoInicializacaoMapeamento=inicializaMapeamento)