public class ArvoreBinaria {
    private Node raiz;

    public ArvoreBinaria() {
        raiz = null;
    }

    public void inserir(int valor) {
        raiz = inserirRec(raiz, valor);
    }

    private Node inserirRec(Node node, int valor) {
        if (node == null) {
            return new Node(valor);
        }

        if (valor < node.valor) {
            node.esquerda = inserirRec(node.esquerda, valor);
        } else if (valor > node.valor) {
            node.direita = inserirRec(node.direita, valor);
        }

        return node;
    }

    public void preOrdem() {
        preOrdemRec(raiz);
        System.out.println();
    }

    private void preOrdemRec(Node node) {
        if (node != null) {
            System.out.print(node.valor + " ");
            preOrdemRec(node.esquerda);
            preOrdemRec(node.direita);
        }
    }

    public void inOrdem() {
        inOrdemRec(raiz);
        System.out.println();
    }

    private void inOrdemRec(Node node) {
        if (node != null) {
            inOrdemRec(node.esquerda);
            System.out.print(node.valor + " ");
            inOrdemRec(node.direita);
        }
    }

    public void posOrdem() {
        posOrdemRec(raiz);
        System.out.println();
    }

    private void posOrdemRec(Node node) {
        if (node != null) {
            posOrdemRec(node.esquerda);
            posOrdemRec(node.direita);
            System.out.print(node.valor + " ");
        }
    }

    public void removerMaior() {
        raiz = removerMaiorRec(raiz);
    }

    private Node removerMaiorRec(Node node) {
        if (node == null) {
            return null;
        }

        if (node.direita == null) {
            return node.esquerda;
        }

        node.direita = removerMaiorRec(node.direita);
        return node;
    }

    public void removerMenor() {
        raiz = removerMenorRec(raiz);
    }

    private Node removerMenorRec(Node node) {
        if (node == null) {
            return null;
        }

        if (node.esquerda == null) {
            return node.direita;
        }

        node.esquerda = removerMenorRec(node.esquerda);
        return node;
    }

    public void remover(int valor) {
        raiz = removerRec(raiz, valor);
    }

    private Node removerRec(Node node, int valor) {
        if (node == null) {
            return null;
        }

        if (valor < node.valor) {
            node.esquerda = removerRec(node.esquerda, valor);
        } else if (valor > node.valor) {
            node.direita = removerRec(node.direita, valor);
        } else {
            if (node.esquerda == null) {
                return node.direita;
            } else if (node.direita == null) {
                return node.esquerda;
            }

            node.valor = menorValor(node.direita);
            node.direita = removerRec(node.direita, node.valor);
        }

        return node;
    }

    private int menorValor(Node node) {
        int menorV = node.valor;
        while (node.esquerda != null) {
            menorV = node.esquerda.valor;
            node = node.esquerda;
        }
        return menorV;
    }
}