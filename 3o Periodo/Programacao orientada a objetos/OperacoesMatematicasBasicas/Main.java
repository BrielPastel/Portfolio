package OperacoesMatematicasBasicas;
import java.util.Scanner;

public class Main {
    public static void main(String args[]){
        Scanner teclado = new Scanner(System.in);

        System.out.print("Digite o primeiro operando: ");
        double a = teclado.nextDouble();

        System.out.print("Digite o segundo operando: ");
        double b = teclado.nextDouble();

        System.out.println("Operacoes disponíveis:");
        System.out.println("1. Adicao \n2. Subtracao \n3. Multiplicacao \n4. Divisao");
        System.out.print("Digite a sua escolha: ");
        int escolha = teclado.nextInt();

        switch (escolha) {
            case 1:

                System.out.println("Resultado: " + (a + b));
                break;

            case 2:

                System.out.println("Resultado: " + (a - b));
                break;
        
            case 3:

                System.out.println("Resultado: " + (a * b));
                break;

            case 4:

                System.out.println("Resultado: " + (a / b));
                break;

            default:
                System.out.println("Nenhuma opcao foi escolhida!");
                break;
        }

        teclado.close();
    }
}
