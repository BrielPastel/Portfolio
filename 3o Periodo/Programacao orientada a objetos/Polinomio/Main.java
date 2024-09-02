package Polinomio;
import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner teclado = new Scanner(System.in);

        System.out.print("Digite o valor de a: ");
        int a = teclado.nextInt();
        System.out.print("Digite o valor de b: ");
        int b = teclado.nextInt();
        System.out.print("Digite o valor de c: ");
        int c = teclado.nextInt();
        System.out.print("Digite o valor de x: ");
        double x = teclado.nextDouble();

        double y = a * Math.pow(x, 2) + b * x + c;
        System.out.println("O resultado é: " + y);

        teclado.close();
    }
}
