package Circulo;
import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner teclado = new Scanner(System.in);

        System.out.print("Digite o raio do circulo: ");
        double r = teclado.nextInt();
        
        double area = Math.PI * Math.pow(r, 2);
        double perimetro = Math.PI * 2 * r;

        String a = String.format("%.2f", area);
        System.out.println("A área do círculo é: " + a);
        String p = String.format("%.2f", perimetro);
        System.out.println("O perímetro do círculo é: " + p);

        teclado.close();
}}