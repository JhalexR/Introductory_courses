package Estructura_de_Datos.Subgrupo_29.Tercera_entrega.Version_propia;

// Clase principal
public class Main {
    public static void main(String[] args) {
        ArbolBinario arbol = new ArbolBinario();

        // Insertar nodos en el árbol
        arbol.insertar(8);
        arbol.insertar(3);
        arbol.insertar(10);
        arbol.insertar(1);
        arbol.insertar(6);
        arbol.insertar(14);
        arbol.insertar(4);
        arbol.insertar(7);
        arbol.insertar(13);

        // Imprimir el árbol
        System.out.println("Árbol binario:");
        arbol.imprimirArbol();

        // Encontrar el sucesor de un valor
        int valor = 6;
        int sucesor = arbol.encontrarSucesor(valor);

        if (sucesor != -1) {
            System.out.println("El sucesor de " + valor + " es " + sucesor);
        } else {
            System.out.println("No se encontró sucesor para " + valor);
        }
    }
}