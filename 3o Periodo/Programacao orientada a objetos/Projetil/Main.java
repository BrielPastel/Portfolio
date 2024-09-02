package Projetil;
import java.util.Scanner;

public class Main {
    public static void main(String args[]){
        Scanner teclado = new Scanner(System.in);
        double g = 9.8;

        System.out.print("Digite o angulo de lancamento (em graus): ");
        double a = Math.toRadians(teclado.nextDouble());

        System.out.print("Digite a distancia em metros: ");
        double m = teclado.nextDouble();

        double V0 = Math.sqrt((m * g) / (2 * Math.sin(a) * Math.cos(a)));
        double t = (2 * V0 * Math.sin(a) / g);

        double tp = 0;

        while (tp <= t) {
            double x = (V0 * Math.cos(a)) * tp;
            double y = (V0 * Math.sin(a)) * tp - (g * Math.pow(tp, 2)) / 2;
            System.out.printf("t = %.2f : (%.2f, %.2f)\n", tp, x, y);
            tp += 0.1;
        }

        teclado.close();
    }
}
