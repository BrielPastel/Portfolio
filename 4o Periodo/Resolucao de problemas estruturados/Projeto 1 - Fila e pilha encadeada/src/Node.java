public class Node {
    private Integer dado;
    private Node proximo;
    public Node(Integer dadoNode){
        this.dado = dadoNode;
        this.proximo = null;
    }

    public Integer getDado() {
        return dado;
    }

    public Node getProximo() {
        return proximo;
    }

    public void setDado(Integer dado) {
        this.dado = dado;
    }

    public void setProximo(Node proximo) {
        this.proximo = proximo;
    }
}
