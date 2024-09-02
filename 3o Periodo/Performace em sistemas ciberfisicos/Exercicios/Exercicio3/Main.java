package Exercicio3;

class Contador {
    private int valor = 0;

    public synchronized void incrementar() {
        valor++;
    }

    public synchronized void imprimir() {
        System.out.println("Valor do contador: " + valor);
    }
}

class ContadorThread extends Thread {
    private Contador contador;

    public ContadorThread(Contador contador) {
        this.contador = contador;
    }

    @Override
    public void run() {
        for (int i = 0; i < 10000; i++) {
            contador.incrementar();
        }
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        for (int i = 0; i < 3; i++) {
            Contador contador = new Contador();

            ContadorThread thread1 = new ContadorThread(contador);
            ContadorThread thread2 = new ContadorThread(contador);

            thread1.start();
            
            thread1.join();
            
            thread2.start();

            thread2.join();

            contador.imprimir();
        }
    }
}
