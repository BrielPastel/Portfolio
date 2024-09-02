public class Node {
    private Integer informacao;
    private Node proximo;
    public Node(int info){
        this.informacao = info;
        this.proximo = null;
    }
    public Integer getInfo(){
        return informacao;
    }

    public Node getProximo(){
        return proximo;
    }
    public void setProximo(Node prox){ proximo = prox; }


}
