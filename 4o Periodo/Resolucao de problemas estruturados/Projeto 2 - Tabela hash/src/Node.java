public class Node {
    private int dado;
    private Node proximo;
    public Node(int dadoNode){
        this.dado = dadoNode;
        this.proximo = null;
    }

    public int getDado() {
        return dado;
    }

    public Node getProximo() {
        return proximo;
    }

    public void setDado(int dado) {
        this.dado = dado;
    }

    public void setProximo(Node proximo) {
        this.proximo = proximo;
    }
}
