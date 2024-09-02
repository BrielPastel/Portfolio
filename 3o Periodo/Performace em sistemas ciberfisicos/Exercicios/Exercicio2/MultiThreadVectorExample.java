package Exercicio2;

import java.util.Random;

public class MultiThreadVectorExample {
    private static final int VECTOR_SIZE = 200_000_000;
    private static final double THRESHOLD_LOWER = 0.25;
    private static final double THRESHOLD_UPPER = 0.75;

    public static void main(String[] args) {
        // Definindo o vetor
        double[] vetor = new double[VECTOR_SIZE];

        // Definindo o número de threads a serem testadas
        int[] numThreads = { 1, 2, 3, 4 };

        for (int numThread : numThreads) {
            long inicio = System.currentTimeMillis();

            // Criando threads
            Contador[] threads = new Contador[numThread];
            int elementosPorThread = VECTOR_SIZE / numThread;

            for (int i = 0; i < numThread; i++) {
                int inicioThread = i * elementosPorThread;
                int fimThread = (i == numThread - 1) ? VECTOR_SIZE : (i + 1) * elementosPorThread;
                threads[i] = new Contador(vetor, inicioThread, fimThread);
                threads[i].start();
            }

            // Aguardando todas as threads completarem
            try {
                for (Contador thread : threads) {
                    thread.join();
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            long fim = System.currentTimeMillis();
            long duracao = fim - inicio;

            // Contando valores maiores que 0.25 e menores que 0.75
            int count = 0;
            for (double value : vetor) {
                if (value > THRESHOLD_LOWER && value < THRESHOLD_UPPER) {
                    count++;
                }
            }

            // Exibindo resultados
            System.out.println("Com " + numThread + " threads:");
            System.out.println("Tempo de execução: " + duracao + " ms");
            System.out.println("Quantidade de valores entre 0.25 e 0.75: " + count);
            System.out.println();
        }
    }

    // Classe interna para contar os valores em uma faixa específica do vetor
    static class Contador extends Thread {
        private final double[] vetor;
        private final int inicio;
        private final int fim;

        Contador(double[] vetor, int inicio, int fim) {
            this.vetor = vetor;
            this.inicio = inicio;
            this.fim = fim;
        }

        @Override
        public void run() {
            Random rand = new Random();

            for (int i = inicio; i < fim; i++) {
                vetor[i] = rand.nextDouble();
            }

            // Exibindo mensagem após inicialização do vetor
            if (inicio == 0) {
                System.out.println("Encerrou inicialização");
            }
        }
    }
}
