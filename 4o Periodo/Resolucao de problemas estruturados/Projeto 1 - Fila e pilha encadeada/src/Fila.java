
public class Fila {
    public ListaEncadeada dados;

    public Fila() {
        this.dados = new ListaEncadeada();
    }

    public void insere(int elemento){
        if (dados.vazia()){
            dados.inserePrimeiro(elemento);
        } else dados.insereUltimo(elemento);
    }

    public int remove(){
        if (dados.vazia()){
            System.out.println("A fila está vazia!");
            return -1;
        }
        else {
            Integer aux = get_primeiro();
            dados.removePrimeiro();
            return aux;
        }
    }

    public void imprime(){
        if (dados.vazia()) {
            System.out.println("A fila está vazia!");
        } else {
            dados.imprime();
        }
    }

    public boolean vazia(){ return dados.vazia(); }

    public Integer get_primeiro() { return dados.getPrimeiro(); }
}
