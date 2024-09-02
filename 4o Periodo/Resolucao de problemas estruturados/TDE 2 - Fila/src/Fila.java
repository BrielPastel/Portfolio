public class Fila {
    public int primeiro;
    public int ultimo;
    public int dados[];

    public Fila(int numero_max) {
        this.primeiro = 0;
        this.ultimo = -1;
        this.dados = new int[numero_max];
    }

    public boolean cheia(){
        if (primeiro == 0 && ultimo == dados.length - 1) {
            return true;
        } else if(ultimo == primeiro - 1 && primeiro != 0){
            return true;
        } else { return false; }
    }

    public boolean vazia(){ return primeiro == 0 && ultimo == -1; }

    public void insere(int elemento){
        if (cheia()){
            System.out.println("A fila está cheia!");
        }
        else {
            if (ultimo == dados.length - 1){
                ultimo = 0;
            } else {
                ultimo += 1;
            }
            dados[ultimo] = elemento;
            System.out.println("O elemento " + elemento + " entrou na fila.");
        }
    }

    public void remove(){
        if (vazia()){
            System.out.println("A fila está vazia!");
        }
        else {
            if (primeiro == ultimo){
                System.out.println("O elemento " + dados[primeiro] + " saiu da fila.");
                primeiro = 0;
                ultimo = -1;
            } else {
                if (primeiro >= 4){
                    System.out.println("O elemento " + dados[(primeiro)] + " saiu da fila.");
                    primeiro = 0;
                } else {
                    System.out.println("O elemento " + dados[primeiro] + " saiu da fila.");
                    primeiro += 1;
                }
            }
        }
    }

    public void imprime(){
        if (!vazia()) {
            if (ultimo >= primeiro){
                for (int i = primeiro; i != (ultimo + 1); i++){
                    System.out.print("| " + dados[i] + " ");
                }
            } else {
                for (int i = primeiro; i < dados.length; i++){
                    System.out.print("| " + dados[i] + " ");
                }
                for (int i = 0; i <= ultimo; i++){
                    System.out.print("| " + dados[i] + " ");
                }
            }
            System.out.println("|");
        } else {
            System.out.println("A fila está vazia!");
        }
    }
}