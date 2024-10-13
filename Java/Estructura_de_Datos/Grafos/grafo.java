package Estructura_de_Datos.Grafos;

public class Grafo {

    private boolean A[][];

    public Grafo (int nodos){
        A = new boolean [nodos][nodos];
    }

    public void agregarArco(int i, int j){
        A[i][j]=true;
        A[j][i]=true;
    }

    public void eliminarArco(int i, int j){
        A[i][j]=false;
        A[j][i]=false;
    }

    public boolean existeArco(int i, int j){
        return A [i][j];
    }

    public static void main (String[] args) {
        Grafo grafo = new Grafo(5);
        grafo.agregarArco(1,2);
        grafo.agregarArco(1,3);

        System.out.println(grafo.existeArco(1,2));
        System.out.println(grafo.existeArco(3,1));
        System.out.println(grafo.existeArco(1,4));
        grafo.eliminarArco(1,3);
        System.out.println(grafo.existeArco(1,3));
    }

}