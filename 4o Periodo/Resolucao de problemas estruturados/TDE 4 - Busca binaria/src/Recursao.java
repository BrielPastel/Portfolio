public class Recursao {

    public int busca_binaria(int dados[], int dado, int inicio, int fim){
        if (inicio == fim) {
            return -1;
        } else {
            int meio = (inicio + fim) / 2;
            if (dados[meio] == dado) {
                return dado;
            } else {
                if (dados[meio] > dado) {
                    fim = meio - 1;
                    return busca_binaria(dados, dado, fim, inicio);
                } else {
                    inicio = meio + 1;
                    return busca_binaria(dados, dado, fim, inicio);
                }
            }
        }
    }
}
