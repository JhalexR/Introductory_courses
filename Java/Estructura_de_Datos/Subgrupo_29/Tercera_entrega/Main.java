package Estructura_de_Datos.Subgrupo_29.Tercera_entrega;
// Implemente un método que, dado un árbol binario ordenado y un valor, retorne el sucesor del valor en el árbol. Calcule la complejidad temporal del método

class Nodo {
    int valor;
    Nodo izquierda;
    Nodo derecha;

    public Nodo(int valor) {
        this.valor = valor;
        this.izquierda = null;
        this.derecha = null;
    }
}

class ArbolBinarioBusqueda {
    Nodo raiz;

    public ArbolBinarioBusqueda() {
        this.raiz = null;
    }

    public void insertar(int valor) {
        raiz = insertarRec(raiz, valor);
    }

    private Nodo insertarRec(Nodo nodo, int valor) {
        if (nodo == null) {
            nodo = new Nodo(valor);
            return nodo;
        }
        if (valor < nodo.valor) {
            nodo.izquierda = insertarRec(nodo.izquierda, valor);
        } else if (valor > nodo.valor) {
            nodo.derecha = insertarRec(nodo.derecha, valor);
        }
        return nodo;
    }

    public Nodo encontrarSucesor(int valor) {
        Nodo actual = buscarNodo(raiz, valor);
        if (actual == null) {
            return null; // Valor no encontrado
        }

        if (actual.derecha != null) {
            return encontrarMin(actual.derecha);
        }

        Nodo sucesor = null;
        Nodo ancestro = raiz;

        while (ancestro != null) {
            if (valor < ancestro.valor) {
                sucesor = ancestro;
                ancestro = ancestro.izquierda;
            } else if (valor > ancestro.valor) {
                ancestro = ancestro.derecha;
            } else {
                break;
            }
        }
        return sucesor;
    }

    private Nodo encontrarMin(Nodo nodo) {
        while (nodo.izquierda != null) {
            nodo = nodo.izquierda;
        }
        return nodo;
    }

    private Nodo buscarNodo(Nodo nodo, int valor) {
        if (nodo == null || nodo.valor == valor) {
            return nodo;
        }
        if (valor < nodo.valor) {
            return buscarNodo(nodo.izquierda, valor);
        }
        return buscarNodo(nodo.derecha, valor);
    }

    public void inOrder() {
        inOrderRec(raiz);
    }

    private void inOrderRec(Nodo nodo) {
        if (nodo != null) {
            inOrderRec(nodo.izquierda);
            System.out.print(nodo.valor + " ");
            inOrderRec(nodo.derecha);
        }
    }

    // Método para verificar si el árbol es equilibrado
    private class Resultado {
        boolean equilibrado;
        int altura;

        Resultado(boolean equilibrado, int altura) {
            this.equilibrado = equilibrado;
            this.altura = altura;
        }
    }

    private Resultado esEquilibradoRec(Nodo nodo) {
        if (nodo == null) {
            return new Resultado(true, 0);
        }

        Resultado izquierda = esEquilibradoRec(nodo.izquierda);
        Resultado derecha = esEquilibradoRec(nodo.derecha);

        boolean equilibrado = izquierda.equilibrado && derecha.equilibrado &&
                              Math.abs(izquierda.altura - derecha.altura) <= 1;

        int altura = 1 + Math.max(izquierda.altura, derecha.altura);

        return new Resultado(equilibrado, altura);
    }

    public boolean esEquilibrado() {
        return esEquilibradoRec(raiz).equilibrado;
    }
}

public class Main {
    public static void main(String[] args) {
        ArbolBinarioBusqueda arbol = new ArbolBinarioBusqueda();
        // INSERTAR VALORES DEL ARBOL
        arbol.insertar(25);
        arbol.insertar(15);
        arbol.insertar(32);
        arbol.insertar(7);
        arbol.insertar(19);
        arbol.insertar(29);
        arbol.insertar(39);
        arbol.insertar(43);

        System.out.println("Árbol en orden:");
        arbol.inOrder();

        // Comprobar si el árbol es equilibrado
        if (arbol.esEquilibrado()) {
            System.out.println("\nEl árbol es equilibrado.");
        } else {
            System.out.println("\nEl árbol no es equilibrado.");
        }

        // INSERTAR VALOR A BUSCAR EN EL ARBOL
        int valorBuscado = 25;
        Nodo sucesor = arbol.encontrarSucesor(valorBuscado);
        if (sucesor != null) {
            System.out.println("\nEl sucesor de " + valorBuscado + " es: " + sucesor.valor);
        } else {
            System.out.println("\nEl sucesor de " + valorBuscado + " no se encontró.");
        }
    }
}
