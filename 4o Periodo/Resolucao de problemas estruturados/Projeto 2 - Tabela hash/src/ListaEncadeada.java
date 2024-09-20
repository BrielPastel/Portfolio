public class ListaEncadeada {
    private Node Lista;
    public ListaEncadeada(){
        this.Lista = null;
    }

    public boolean vazia(){ return Lista == null; }

    public void inserePrimeiro(int info){
        Node novo = new Node(info);
        novo.setProximo(this.Lista);
        this.Lista = novo;
    }

    public int getPrimeiro(){
        return Lista.getDado();
    }

    public void insereDepois(Node node, int info){
        if (!vazia()) {
            Node novoNode = new Node(info);
            novoNode.setProximo(node.getProximo());
            node.setProximo(novoNode);
        } else inserePrimeiro(info);
    }

    public void insereDepois(int antigo, int info){
        Node noAntigo = getNode(antigo);
        insereDepois(noAntigo,info);
    }

    public Node getNode(int valor){
        Node atual = this.Lista;
        while(atual != null)
        {
            if(atual.getDado() == valor)
                return atual;
            atual = atual.getProximo();
        }
        return null;
    }


    public Node getUltimo(){
        Node atual = this.Lista;
        while(atual != null)
        {
            if(atual.getProximo() == null)
                return atual;
            atual = atual.getProximo();
        }
        return null;
    }

    public void insereUltimo(int info){
        if (!vazia()){
            Node novoNode = new Node(info);
            Node ultimoAntigo = getUltimo();
            ultimoAntigo.setProximo(novoNode);
        }
    }

    public void insereOrdenado(int info) {
        if (Lista == null || Lista.getDado() >= info) {
            inserePrimeiro(info);
            return;
        }

        Node novoNode = new Node(info);

        Node atual = this.Lista;
        Node anterior = null;
        while (atual != null && atual.getDado() < info) {
            anterior = atual;
            atual = atual.getProximo();
        }

        if (anterior == null){
            System.out.println("O numero nao se encaixa");
            return;
        }

        novoNode.setProximo(anterior.getProximo());
        anterior.setProximo(novoNode);
    }

    public void imprime() {
        Node atual = this.Lista;
        while (atual != null) {
            System.out.print(atual.getDado() + " | ");
            atual = atual.getProximo();
        }
        System.out.println();
    }

    public Node removePrimeiro(){
        if (!vazia()) {
            Node aux = this.Lista;
            this.Lista = Lista.getProximo();
            System.out.println("O elemento " + aux.getDado() + " foi removido");
            return aux;
        } else return null;
    }

    public Node removeUltimo() {
        if (vazia()) {
            System.out.println("A lista está vazia. Nada para remover.");
            return null;
        }

        if (Lista.getProximo() == null) {
            Node unico = Lista;
            Lista = null;
            System.out.println("O elemento " + unico.getDado() + " foi removido");
            return unico;
        }

        Node atual = Lista;
        Node anterior = null;
        while (atual.getProximo() != null) {
            anterior = atual;
            atual = atual.getProximo();
        }

        anterior.setProximo(null);
        System.out.println("O elemento " + atual.getDado() + " foi removido");
        return atual;
    }

    public Node remove(int info){
        if (!vazia()){
            Node aux = getNode(info);
            Node atual = this.Lista;
            Node anterior = null;
            while (atual != aux){
                System.out.println(atual.getDado());
                anterior = atual;
                atual = atual.getProximo();
            }

            if (anterior == null){
                System.out.println("O numero nao existe");
                return null;
            }

            anterior.setProximo(atual.getProximo());
            System.out.println("O elemento " + atual.getDado() + " foi removido");
        }
        return null;
    }

    public boolean busca(int valor){
        Node atual = this.Lista;
        while (atual != null) {
            if (atual.getDado() == valor){
                return true;
            }
            atual = atual.getProximo();
        }
        return false;
    }

}
