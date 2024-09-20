public class TabelaHash {
    private int colisao;
    private ListaEncadeada[] tabela;

    public TabelaHash(int tamanho){
        this.colisao = 0;
        this.tabela = new ListaEncadeada[tamanho];
    }

    public void insere(int valor){
        int chave = funcaoHash(valor);
        if (tabela[chave] == null){
            tabela[chave] = new ListaEncadeada();
        }
        else {
            colisao += 1;
        }
        tabela[chave].insereOrdenado(valor);
    }

    public int funcaoHash(int chave){
        return chave % tabela.length;
    }

    public void imprimeHash(){
        for (int i = 0; i < tabela.length; i++){
            tabela[i].imprime();
        }
    }

    public boolean busca(int valor){
        int chave = funcaoHash(valor);
        if (tabela[chave] != null){
            return tabela[chave].busca(valor);
        }
        return false;
    }
}
