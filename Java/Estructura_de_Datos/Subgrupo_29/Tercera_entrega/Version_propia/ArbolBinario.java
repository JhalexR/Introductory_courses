/*  Author: 
    John Alexander Peñaloza Rojas    
    Modulo: Estructura de datos - Segundo semestre 2024
    Grupo: B01 - subgrupo: 29
    fecha: 05/10/2024
*/

package Estructura_de_Datos.Subgrupo_29.Tercera_entrega.Version_propia;

// Clase Árbol Binario
public class ArbolBinario {
    Nodo raiz;

    // Método para encontrar el sucesor de un valor en el árbol
    public int encontrarSucesor(int valor) {
        Nodo sucesor = null;
        Nodo actual = raiz;

        while (actual != null) {
            if (actual.valor > valor) {
                sucesor = actual;
                actual = actual.izquierdo;
            } else {
                actual = actual.derecho;
            }
        }

        if (sucesor != null) {
            return sucesor.valor;
        } else {
            return -1; // No se encontró sucesor
        }
    }

    // Método para insertar un nodo en el árbol
    public void insertar(int valor) {
        Nodo nuevoNodo = new Nodo(valor);

        if (raiz == null) {
            raiz = nuevoNodo;
        } else {
            Nodo actual = raiz;

            while (true) {
                if (valor < actual.valor) {
                    if (actual.izquierdo == null) {
                        actual.izquierdo = nuevoNodo;
                        break;
                    }
                    actual = actual.izquierdo;
                } else {
                    if (actual.derecho == null) {
                        actual.derecho = nuevoNodo;
                        break;
                    }
                    actual = actual.derecho;
                }
            }
        }
    }

    // Método para imprimir el árbol
    public void imprimirArbol() {
        imprimirArbol(raiz);
    }

    private void imprimirArbol(Nodo nodo) {
        if (nodo != null) {
            imprimirArbol(nodo.izquierdo);
            System.out.print(nodo.valor + " ");
            imprimirArbol(nodo.derecho);
        }
    }
}