package Estructura_de_Datos.Subgrupo_29.Segunda_entrega;

class Nodo {
	//Se define el arbol binario con raiz, izq y der
    int valor;
    Nodo izquierda;
    Nodo derecha;

    public Nodo(int valor) {
        this.valor = valor;
        this.izquierda = null;
        this.derecha = null;
    }
}
// clase del arbol binario
public class ArbolBinario {

    public static int contarNodos(Nodo raiz) {
        // nodo null es igual a cero
        if (raiz == null) {
            return 0;
        }
        // Sumar 1 por el nodo actual y contar nodos en subárboles izquierdo y derecho
        return 1 + contarNodos(raiz.izquierda) + contarNodos(raiz.derecha);
    }

    public static void main(String[] args) {
        // Creación de un árbol binario con 9 nodos repartidos en los subarboles y contando raiz
        Nodo raiz = new Nodo(1);
        raiz.izquierda = new Nodo(2);
        raiz.derecha = new Nodo(3);
        raiz.izquierda.izquierda = new Nodo(4);
        raiz.izquierda.derecha = new Nodo(5);
        raiz.derecha.izquierda = new Nodo(6);
        raiz.derecha.derecha = new Nodo(7);
        raiz.izquierda.izquierda.izquierda = new Nodo(8);
        raiz.izquierda.izquierda.derecha = new Nodo(9);

        // Total de nodos
        int cantidadNodos = contarNodos(raiz);
        System.out.println("Cantidad de nodos en el árbol: " + cantidadNodos);
    }
}