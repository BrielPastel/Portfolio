import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Pilha pilha = new Pilha(5);
        Scanner scanner = new Scanner(System.in);

        System.out.print("Expressão: ");
        String expressao = scanner.nextLine();

        for (int i = 0; i < expressao.length(); i++) {
            char c = expressao.charAt(i);
            if (c == '(' || c == '[' || c == '{') {
                pilha.empilha(c);
            } else if (c == ')' || c == ']' || c == '}') {
                if (pilha.topo() == '(' && c == ')') {
                    pilha.desempilha();
                } else if (pilha.topo() == '[' && c == ']') {
                    pilha.desempilha();
                } else if (pilha.topo() == '{' && c == '}') {
                    pilha.desempilha();
                } else {
                    System.out.println("A expressao ta errada.");
                    return;
                }
            }
        }
        if (pilha.vazia()) {
            System.out.println("A expressao ta certa.");
        } else if (!pilha.vazia()) {
            System.out.println("A expressao ta errada.");
        }


    }
}

