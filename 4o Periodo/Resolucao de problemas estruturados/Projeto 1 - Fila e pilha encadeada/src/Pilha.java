public class Pilha {
    private ListaEncadeada dados;

    public Pilha() {
        this.dados = new ListaEncadeada();
    }

    public void empilha(Integer elemento){
        if (dados.vazia()){
            dados.inserePrimeiro(elemento);
            System.out.println("O elemento " + elemento + " foi empilhado.");
        } else {
            dados.insereUltimo(elemento);
            System.out.println("O elemento " + elemento + " foi empilhado.");
        }
    }

    public void desempilha(){
        if (dados.vazia()){
            System.out.println("A pilha está vazia!");
        } else {
            System.out.println("O elemento " + dados.getUltimo().getDado() + " foi desempilhado");
            dados.removeUltimo();
        }
    }

    public void imprime(){ dados.imprime(); }

}
