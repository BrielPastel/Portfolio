
public class Main {
    public static void main(String[] args) {
        Fila fila1 = new Fila();
        Fila fila2 = new Fila();
        Fila filafusao = new Fila();

        fila1.insere(1);
        fila1.insere(7);
        fila1.insere(12);
        fila1.insere(20);

        fila2.insere(4);
        fila2.insere(5);
        fila2.insere(13);
        fila2.insere(14);
        fila2.insere(15);
        fila2.insere(16);


        fila1.imprime();
        fila2.imprime();

        Merge merge = new Merge();
        merge.fusao(fila1, fila2, filafusao);

        filafusao.imprime();


    }
}

