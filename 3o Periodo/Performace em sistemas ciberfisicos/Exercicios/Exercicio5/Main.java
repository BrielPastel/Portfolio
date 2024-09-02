package Exercicio5;

import java.util.Random;
import java.util.concurrent.locks.ReentrantLock;

class Contador {
    private int valor;
    private final ReentrantLock lock = new ReentrantLock();

    public synchronized void incrementa() {
        lock.lock();
        try {
            valor++;
            System.out.println(Thread.currentThread().getName() + " incrementou. Valor: " + valor);
        } finally {
            lock.unlock();
        }
    }

    public synchronized void decrementa() {
        lock.lock();
        try {
            valor--;
            System.out.println(Thread.currentThread().getName() + " decrementou. Valor: " + valor);
        } finally {
            lock.unlock();
        }
    }

    public int getValor() {
        return valor;
    }
}

class MinhaThread extends Thread {
    private final Contador contador;
    private final Random rand = new Random();

    public MinhaThread(Contador contador) {
        this.contador = contador;
    }

    @Override
    public void run() {
        try {
            for (int i = 0; i < 100; i++) {
                contador.incrementa();
                Thread.sleep(10); // Dorme por um tempo aleatório até 100 ms
            }
            for (int i = 0; i < 100; i++) {
                contador.decrementa();
                Thread.sleep(10); // Dorme por um tempo aleatório até 100 ms
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Contador contador = new Contador();
        Thread[] threads = new Thread[4];

        // Criando e iniciando 4 threads
        for (int i = 0; i < 4; i++) {
            threads[i] = new MinhaThread(contador);
            threads[i].start();
            try {
                threads.wait();
            } catch (Exception e) {
                Thread.currentThread().interrupt();
            }
        }

        // Aguardando a execução das threads
        for (int i = 0; i < 4; i++) {
            try {
                threads.notifyAll();
                threads[i].join();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }

        // Exibindo o valor final do contador
        System.out.println("Valor final do contador: " + contador.getValor());
    }
}
