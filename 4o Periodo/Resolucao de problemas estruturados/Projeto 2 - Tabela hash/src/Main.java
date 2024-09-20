import java.util.Scanner;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        boolean programa = true;
        int escolha;
        int numeroDeValores = 1000000;

        Scanner scanner = new Scanner(System.in);

        System.out.println("Tamanho da tabela: ");
        int tamanho = scanner.nextInt();

        TabelaHash tabelahash = new TabelaHash(tamanho);

        for (int i = 0; i < numeroDeValores; i++) {
            Random random = new Random();
            int numero = random.nextInt(1000000);
            tabelahash.insere(numero);
        }
        tabelahash.imprimeHash();
        while (programa){
            System.out.println("Busca: ");
            escolha = scanner.nextInt();
            if (escolha != -1) {
                if (tabelahash.busca(escolha)){
                    System.out.println("O numero existe!");
                } else {
                    System.out.println("O numero nao existe!");
                }
            } else {
                programa = false;
                System.out.println("Desligando!");
            }
        }

    }
}

