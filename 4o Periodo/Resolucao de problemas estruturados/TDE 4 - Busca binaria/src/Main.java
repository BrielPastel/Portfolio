public class Main {
    public static void main(String[] args) {
        int dados[] = {3, 5, 9, 18, 23, 25, 31};

        Recursao recursao = new Recursao();

        int resultado;
        resultado = recursao.busca_binaria(dados, 4, 0, 6);

        System.out.println(resultado);
    }
}