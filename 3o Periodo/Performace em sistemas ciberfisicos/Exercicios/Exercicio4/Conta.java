package Exercicio4;

import java.util.Random;
import java.util.concurrent.locks.ReentrantLock;

public class Conta {
    private double saldo;
    private final ReentrantLock lock = new ReentrantLock();

    public void deposito(double valor) {
        lock.lock();
        try {
            saldo += valor;
            System.out.println("Depósito de: " + valor + " | Saldo atual: " + saldo);
        } finally {
            lock.unlock();
        }
    }

    public void saque(double valor) {
        lock.lock();
        try {
            if (saldo >= valor) {
                saldo -= valor;
                System.out.println("Saque de: " + valor + " | Saldo atual: " + saldo);
            } else {
                System.out.println("Tentativa de saque de: " + valor + " falhou | Saldo insuficiente: " + saldo);
            }
        } finally {
            lock.unlock();
        }
    }

    public double getSaldo() {
        lock.lock();
        try {
            return saldo;
        } finally {
            lock.unlock();
        }
    }

    public static void main(String[] args) {
        Conta conta = new Conta();

        // Criando e iniciando threads de depósito
        Thread deposito1 = new Thread(new Deposito(conta));
        Thread deposito2 = new Thread(new Deposito(conta));

        // Criando e iniciando threads de saque
        Thread saque1 = new Thread(new Saque(conta));
        Thread saque2 = new Thread(new Saque(conta));
        Thread saque3 = new Thread(new Saque(conta));

        deposito1.start();
        deposito2.start();
        saque1.start();
        saque2.start();
        saque3.start();
    }
}

class Deposito implements Runnable {
    private final Conta conta;
    private final Random rand = new Random();

    public Deposito(Conta conta) {
        this.conta = conta;
    }

    @Override
    public void run() {
        try {
            while (true) {
                double valor = 30 + (300 - 30) * rand.nextDouble();
                conta.deposito(valor);
                Thread.sleep(1000);
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}

class Saque implements Runnable {
    private final Conta conta;
    private final Random rand = new Random();

    public Saque(Conta conta) {
        this.conta = conta;
    }

    @Override
    public void run() {
        try {
            while (true) {
                double valor = 50 + (500 - 50) * rand.nextDouble();
                conta.saque(valor);
                Thread.sleep(1000);
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}
