import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ListaEncadeada lista1 = new ListaEncadeada();
        lista1.inserePrimeiro(10);
        lista1.inserePrimeiro(20);
        lista1.inserePrimeiro(15);
        lista1.insereDepois(20, 25);
        lista1.imprime();

    }
}

