
public class Merge {
    public void fusao(Fila fila1, Fila fila2, Fila filaprincipal) {
        while (!fila1.vazia() && !fila2.vazia()) {
            if (fila1.get_primeiro() < fila2.get_primeiro()) {
                filaprincipal.insere(fila1.remove());
            } else if (fila1.get_primeiro() > fila2.get_primeiro()) {
                filaprincipal.insere(fila2.remove());
            }
        }
        if (!fila1.vazia()){
            while (!fila1.vazia()){
                filaprincipal.insere(fila1.remove());
            }
        }
        if (!fila2.vazia()){
            while (!fila2.vazia()){
                filaprincipal.insere(fila2.remove());
            }
        }
    }
}
