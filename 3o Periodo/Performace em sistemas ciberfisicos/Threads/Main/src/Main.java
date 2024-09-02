import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

// Trabalho feito por Arthur Capellazzi Fontana Amaral e Gabriel Berto Beckauser

class Arquivo_Thread extends Thread {
    private int inicio;
    private int fim;
    private File[] lista_arquivos;
    private int[] contagem_caracter;

    public Arquivo_Thread(int inicio, int fim, File[] lista_arquivos, int[] contagem_caracter) {
        this.inicio = inicio;
        this.fim = fim;
        this.lista_arquivos = lista_arquivos;
        this.contagem_caracter = contagem_caracter;
    }

    public void run() {
        for (int i = inicio; i <= fim; i++) {
            File arquivo_atual = lista_arquivos[i];
            if (arquivo_atual.exists() && arquivo_atual.isFile() && arquivo_atual.getName().endsWith(".txt")) {
                contar_caracteres(arquivo_atual);
            }
        }
    }

    private void contar_caracteres(File arquivo_atual) {
        try (BufferedReader leitor_arquivo = new BufferedReader(new FileReader(arquivo_atual))) {
            int caractere_lido;
            while ((caractere_lido = leitor_arquivo.read()) != -1) {
                if (caractere_lido >= 0 && caractere_lido <= 255) {
                    synchronized (contagem_caracter) {
                        contagem_caracter[caractere_lido]++;
                    }
                }
            }
        } catch (IOException erro_leitura) {
            erro_leitura.printStackTrace();
        }
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        long tempo_inicio = System.currentTimeMillis();
        String diretorio_caminho = "todosArquivos";
        File diretorio_principal = new File(diretorio_caminho);
        File[] arquivos_encontrados = diretorio_principal.listFiles();
        int numero_threads = 10;
        int[] contagem_total_caracteres = new int[256];
        ArrayList<Arquivo_Thread> lista_threads = new ArrayList<>();
        int arquivos_por_thread = arquivos_encontrados.length / numero_threads;

        for (int i = 0; i < numero_threads; i++) {
            int intervalo_inicial = i * arquivos_por_thread;
            int intervalo_final = (i == numero_threads - 1) ? arquivos_encontrados.length - 1 : intervalo_inicial + arquivos_por_thread - 1;
            Arquivo_Thread thread_atual = new Arquivo_Thread(intervalo_inicial, intervalo_final, arquivos_encontrados, contagem_total_caracteres);
            lista_threads.add(thread_atual);
            thread_atual.start();
        }

        for (Arquivo_Thread thread_atual : lista_threads) {
            thread_atual.join();
        }

        exibir_contagem_caracteres(contagem_total_caracteres);
        long tempo_fim = System.currentTimeMillis();
        long duracao_execucao = tempo_fim - tempo_inicio;
        System.out.println("Tempo de execução: " + duracao_execucao + "ms");
    }

    private static void exibir_contagem_caracteres(int[] contagem_total_caracteres) {
        for (int i = 0; i < contagem_total_caracteres.length; i++) {
            if (contagem_total_caracteres[i] > 0) {
                System.out.println("Caractér " + (char) i + " = " + contagem_total_caracteres[i]);
            }
        }
    }
}