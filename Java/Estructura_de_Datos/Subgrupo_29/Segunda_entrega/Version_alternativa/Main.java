package Estructura_de_Datos.Subgrupo_29.Segunda_entrega.Version_alternativa;

import java.util.Scanner;

// Clase que representa un nodo del árbol binario
class Nodo {
    int valor;
    Nodo izquierdo;
    Nodo derecho;

    public Nodo(int valor) {
        this.valor = valor;
        this.izquierdo = null;
        this.derecho = null;
    }
}

// Clase que representa el árbol binario
class ArbolBinario {
    Nodo raiz;

    public ArbolBinario() {
        this.raiz = null;
    }

    // Método para agregar un nodo al árbol
    public void agregarNodo(int valor) {
        Nodo nuevoNodo = new Nodo(valor);
        if (raiz == null) {
            raiz = nuevoNodo;
        } else {
            agregarNodoRecursivo(raiz, nuevoNodo);
        }
    }

    // Método recursivo para agregar un nodo al árbol
    private void agregarNodoRecursivo(Nodo actual, Nodo nuevoNodo) {
        if (nuevoNodo.valor < actual.valor) {
            if (actual.izquierdo == null) {
                actual.izquierdo = nuevoNodo;
            } else {
                agregarNodoRecursivo(actual.izquierdo, nuevoNodo);
            }
        } else {
            if (actual.derecho == null) {
                actual.derecho = nuevoNodo;
            } else {
                agregarNodoRecursivo(actual.derecho, nuevoNodo);
            }
        }
    }

    // Método para buscar un valor en el árbol
    public boolean buscarValor(int valor) {
        return buscarValorRecursivo(raiz, valor);
    }

    // Método recursivo para buscar un valor en el árbol
    private boolean buscarValorRecursivo(Nodo actual, int valor) {
        if (actual == null) {
            return false;
        }
        if (valor == actual.valor) {
            return true;
        }
        if (valor < actual.valor) {
            return buscarValorRecursivo(actual.izquierdo, valor);
        } else {
            return buscarValorRecursivo(actual.derecho, valor);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArbolBinario arbol = new ArbolBinario();

        System.out.print("Ingrese el tamaño del arreglo: ");
        int tamaño = scanner.nextInt();

        System.out.println("Ingrese los valores del arreglo:");
        for (int i = 0; i < tamaño; i++) {
            int valor = scanner.nextInt();
            arbol.agregarNodo(valor);
        }

        System.out.print("Ingrese el valor a buscar: ");
        int valorABuscar = scanner.nextInt();

        if (arbol.buscarValor(valorABuscar)) {
            System.out.println("El valor se encuentra en el árbol");
        } else {
            System.out.println("El valor no se encuentra en el árbol");
        }
        scanner.close();
    }
}