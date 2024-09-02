package Exercicio1;


class JotaBrel extends Thread{
    private String nome;

    public JotaBrel(String nome) {
        this.nome = nome;
    }

    @Override
    public void run() {
        System.out.println("Bem vindo!");
        try {
            Thread.sleep(2000);
        }
        catch (InterruptedException e){
            e.printStackTrace();
        }
        System.out.println("Adeus!");

    }
}

public class Main {
    public static void main(String[] args) {
        JotaBrel threadBrel1 = new JotaBrel("JotaBrel");
        JotaBrel threadBrel2 = new JotaBrel("JotaPastel");

        threadBrel1.start();

        try {
            threadBrel1.join();
        }
        catch (InterruptedException e){
            e.printStackTrace();
        }

        threadBrel2.start();

        try {
            threadBrel2.join();
        }
        catch (InterruptedException e){
            e.printStackTrace();
        }

        System.out.println("Fim do programa!");
    }
}