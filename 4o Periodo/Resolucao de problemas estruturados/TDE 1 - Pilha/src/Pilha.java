public class Pilha {
    private int topo;
    private int MAX;
    private char dados[];

    public Pilha(int numero_max) {
        this.topo = -1;
        this.MAX = numero_max;
        this.dados = new char[MAX];
    }

    public char topo(){
        if (!vazia()){
            return dados[topo];
        }
        return '0';
    }

    public boolean vazia(){
        return topo <= -1;
    }

    public boolean cheia(){
        return topo >= MAX;
    }

    public void empilha(char elemento){
        if (cheia()){
            System.out.println("A pilha está cheia!");
        }
        else {
            topo += 1;
            dados[topo] = elemento;
            System.out.println("O elemento " + elemento + " foi empilhado.");
        }
    }

    public void desempilha(){
        if (vazia()){
            System.out.println("A pilha está vazia!");
        }
        else {
            topo -= 1;
            System.out.println("O elemento " + dados[topo + 1] + " foi desempilhado");
        }
    }

}
