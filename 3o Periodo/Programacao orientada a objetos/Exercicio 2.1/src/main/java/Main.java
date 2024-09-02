import java.util.Scanner;

public class Main {
  public static void main(String args[]) {
    Scanner raio = new Scanner(System.in);
    System.out.print("Digite o raio do círculo em metros: ");
    int k = raio.nextInt();
    double area = Math.PI * k * k;
    double perimetro = 2 * Math.PI * k;
    System.out.printf("Seu círculo tem %.2f", area);
    System.out.printf("m de área e %.2f", perimetro);
    System.out.printf("m de perímetro.");
    raio.close();
  }
}