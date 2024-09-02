public class ListaEncadeada {
    private Node Lista;
    public ListaEncadeada(){
        this.Lista = null;
    }

    public boolean vazia(){ return Lista == null; }

    public void inserePrimeiro(int info){
            Node novo = new Node(info);
            novo.setProximo(Lista);
            Lista = novo;
    }

    public void insereDepois(int anterior, int info){
        Node novo = new Node(info);
        Node atual = Lista;
        while (atual.getInfo() != anterior){
            atual = atual.getProximo();

        }
        novo.setProximo(atual.getProximo());
        atual.setProximo(novo);

    }

    public void imprime(){
            Node atual = Lista;
            while (atual != null){
                System.out.println(atual.getInfo());
                atual = atual.getProximo();
        }
    }
}
