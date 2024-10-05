package Estructura_de_Datos.Subgrupo_29.Segunda_entrega;

/*  Author: 
    John Alexander Peñaloza Rojas    
    Modulo: Estructura de datos - Segundo semestre 2024
    Grupo: B01 - subgrupo: 29
    fecha: 23/09/2024
*/

import java.util.Scanner;

public class SortedBinaryTree {

    /* Atributos de la clase */
    NodeTree root;
    int intsequence[]; 
    protected int size;
    protected Scanner Dat;

    /* método constructor */
    public SortedBinaryTree() {
        root = null;
        System.out.print("Introduce la cantidad de números enteros a almacenar: ");
        Dat = new Scanner(System.in); // se solicita al usuario el tamaño total del arreglo
        size = Dat.nextInt();
        intsequence = new int[size];       
    }

    /* método con el cual se capturan los números dentro del arreglo */
    public void fill_out_array () { 
        System.out.println();       
        for(int f = 0; f < size; f++) {
            System.out.print("Escribe el número de la posición: "+(f+1)+" y presiona enter: ");
            intsequence[f] = Dat.nextInt();        
        } 
    }

    /* método con el cual se llena el árbol con los datos del arreglo */
    public void move_from_array_to_tree () {       
        for(int f = 0; f < size; f++) {
            insertNode(intsequence[f]);            
        }
    }

    /* Método para insertar un nuevo nodo en el árbol */
    public void insertNode(int number) {
        root = insertRecursiveNode(root, number);       
    }

    /* Método recursivo para insertar un nuevo valor en el árbol */
    private NodeTree insertRecursiveNode(NodeTree root, int number) {
        // Si el árbol está vacío, se crea un nuevo nodo
        if (root == null) {
            root = new NodeTree(number);
            return root;
        }

        // Si el valor es menor que el nodo actual, se inserta en el subárbol izquierdo
        if (number < root.number) {
            root.left = insertRecursiveNode(root.left, number);
        }
        // Si el valor es mayor que el nodo actual, se inserta en el subárbol derecho
        else if (number > root.number) {
            root.right = insertRecursiveNode(root.right, number);
        }

        return root;
    }

    /* Método para buscar un número en el árbol */
    public boolean search(int number) {
        return searchRecursive(root, number);
    }

    /* Método recursivo para buscar un número en el árbol */
    private boolean searchRecursive(NodeTree root, int number) {
        if (root == null) {
            return false; // El número no está en el árbol
        }
        if (number == root.number) {
            return true; // Número encontrado
        }
        if (number < root.number) {
            return searchRecursive(root.left, number); // Buscar en el subárbol izquierdo
        } else {
            return searchRecursive(root.right, number); // Buscar en el subárbol derecho
        }
    }

    /* método main para creación de objetos e invocar los métodos */
    public static void main(String[] args) {
        SortedBinaryTree tree_1 = new SortedBinaryTree();     
        tree_1.fill_out_array();
        tree_1.move_from_array_to_tree();
        
        // Preguntar al usuario el número a buscar
        Scanner sc = new Scanner(System.in);
        System.out.print("Introduce el número a buscar en el árbol: ");
        int numberToSearch = sc.nextInt();
        
        // Llamar al método de búsqueda y mostrar el resultado
        if (tree_1.search(numberToSearch)) {
            System.out.println("El número " + numberToSearch + " se encuentra en el árbol.");
        } else {
            System.out.println("El número " + numberToSearch + " NO se encuentra en el árbol.");
        }
        sc.close();
    }
}

/* Clase para representar un nodo del árbol */
class NodeTree {

    int number;
    NodeTree left, right;

    public NodeTree(int number) {
        this.number = number;
        left = right = null;
    }
}