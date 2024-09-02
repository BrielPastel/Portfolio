public class Merge {
    public void fusao(Fila fila1, Fila fila2, Fila filaprincipal) {
        while (!fila1.vazia() && !fila2.vazia()) {
            if (fila1.dados[fila1.primeiro] < fila2.dados[fila2.primeiro]) {
                filaprincipal.insere(fila1.dados[fila1.primeiro]);
                fila1.remove();
            } else if (fila1.dados[fila1.primeiro] > fila2.dados[fila2.primeiro]) {
                filaprincipal.insere(fila2.dados[fila2.primeiro]);
                fila2.remove();
            }
        }
        if (!fila1.vazia()){
            if (fila1.ultimo >= fila1.primeiro){
                for (int i = fila1.primeiro; i != (fila1.ultimo + 1); i++){
                    filaprincipal.insere(fila1.dados[i]);
                }
            } else {
                for (int i = fila1.primeiro; i < fila1.dados.length; i++){
                    filaprincipal.insere(fila1.dados[i]);
                }
                for (int i = 0; i <= fila1.ultimo; i++){
                    filaprincipal.insere(fila1.dados[i]);
                }
            }
        }
        if (!fila2.vazia()){
            if (fila2.ultimo >= fila2.primeiro){
                for (int i = fila2.primeiro; i != (fila2.ultimo + 1); i++){
                    filaprincipal.insere(fila2.dados[i]);
                }
            } else {
                for (int i = fila2.primeiro; i < fila2.dados.length; i++){
                    filaprincipal.insere(fila2.dados[i]);
                }
                for (int i = 0; i <= fila2.ultimo; i++){
                    filaprincipal.insere(fila2.dados[i]);
                }
            }
        }
    }
}