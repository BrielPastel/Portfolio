public class Main {
    public static void main(String[] args) {

        ArvoreBinaria arvore = new ArvoreBinaria();

        arvore.inserir(10);
        arvore.inserir(1);
        arvore.inserir(16);
        arvore.inserir(23);
        arvore.inserir(5);
        arvore.inserir(19);
        arvore.inserir(28);

        arvore.inOrdem();

        arvore.removerMenor();

        arvore.inOrdem();

        arvore.removerMaior();

        arvore.inOrdem();

        arvore.remover(19);

        arvore.inOrdem();


    }
}