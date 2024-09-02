import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Fila fila1 = new Fila(5);
        Fila fila2 = new Fila(5);
        Fila fila3 = new Fila(10);
        Scanner scanner = new Scanner(System.in);
        boolean programageral = true;
        boolean programa = true;

        while(programageral) {
            System.out.println("Opcao 1: Alterar fila1\n" +
                    "Opcao 2: Alterar fila2\n" +
                    "Opcao 3: Juntar filas 1 e 2\n" +
                    "Opcao 4: Imprimir fila3\n" +
                    "Opcao 5: Sair");
            char opcaogeral = scanner.next().charAt(0);
            programa = true;
            switch (opcaogeral) {
                case '1':
                    while(programa) {
                        System.out.println("Opcao 1: Inserir\n" +
                                "Opcao 2: Remover\n" +
                                "Opcao 3: Imprimir\n" +
                                "Opcao 4: Voltar");
                        char opcao = scanner.next().charAt(0);
                        switch (opcao) {
                            case '1':
                                System.out.print("\n");
                                System.out.println("Caracter para inserir: ");
                                int valor = scanner.nextInt();
                                fila1.insere(valor);
                                break;
                            case '2':
                                System.out.print("\n");
                                fila1.remove();
                                break;
                            case '3':
                                System.out.print("\n");
                                fila1.imprime();
                                break;
                            case '4':
                                System.out.print("\n");
                                programa = false;
                                break;
                            default:
                                System.out.print("\n");
                                System.out.println("Você não escolheu nenhuma opção!");
                        }
                    }
                    break;
                case '2':
                    while(programa) {
                        System.out.println("Opcao 1: Inserir\n" +
                                "Opcao 2: Remover\n" +
                                "Opcao 3: Imprimir\n" +
                                "Opcao 4: Voltar");
                        char opcao = scanner.next().charAt(0);
                        switch (opcao) {
                            case '1':
                                System.out.print("\n");
                                System.out.println("Caracter para inserir: ");
                                int valor = scanner.nextInt();
                                fila2.insere(valor);
                                break;
                            case '2':
                                System.out.print("\n");
                                fila2.remove();
                                break;
                            case '3':
                                System.out.print("\n");
                                fila2.imprime();
                                break;
                            case '4':
                                System.out.print("\n");
                                programa = false;
                                break;
                            default:
                                System.out.print("\n");
                                System.out.println("Você não escolheu nenhuma opção!");
                        }
                    }
                    break;
                case '3':
                    System.out.print("\n");
                    Merge merge = new Merge();
                    merge.fusao(fila1, fila2, fila3);
                    fila3.imprime();
                    break;
                case '4':
                    fila3.imprime();
                    break;
                case '5':
                    programageral = false;
                    break;
                default:
                    System.out.print("\n");
                    System.out.println("Você não escolheu nenhuma opção!");
            }
        }
    }
}