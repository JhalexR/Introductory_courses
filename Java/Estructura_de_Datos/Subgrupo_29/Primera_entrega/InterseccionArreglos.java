package Estructura_de_Datos.Subgrupo_29.Primera_entrega;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class InterseccionArreglos {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Obtenemos los tamaños de los arreglos
        System.out.print("Ingrese el tamaño del arreglo A: ");
        int tamañoA = leerEntero(scanner);
        System.out.print("Ingrese el tamaño del arreglo B: ");
        int tamañoB = leerEntero(scanner);

        // Creamos los arreglos y llenarlos con valores
        List<Integer> arregloA = new ArrayList<>();
        List<Integer> arregloB = new ArrayList<>();
        llenarArreglo(scanner, arregloA, tamañoA);
        llenarArreglo(scanner, arregloB, tamañoB);

        // Encontrar la intersección
        List<Integer> interseccion = encontrarInterseccion(arregloA, arregloB);

        // Imprimir el resultado
        if (interseccion.isEmpty()) {
            System.out.println("No hay elementos en común entre los dos arreglos.");
        } else {
            System.out.println("La intersección de los arreglos es: " + interseccion);
        }
    }

    // Método para leer un entero válido del usuario
    private static int leerEntero(Scanner scanner) {
        while (!scanner.hasNextInt()) {
            System.out.println("Por favor, ingrese un número entero válido.");
            scanner.next();
        }
        return scanner.nextInt();
    }

    // Método para llenar un arreglo con valores enteros
    private static void llenarArreglo(Scanner scanner, List<Integer> arreglo, int tamaño) {
        for (int i = 0; i < tamaño; i++) {
            System.out.print("Ingrese el elemento " + (i + 1) + " del arreglo: ");
            arreglo.add(leerEntero(scanner));
        }
    }

    // Método para encontrar la intersección de dos arreglos
    private static List<Integer> encontrarInterseccion(List<Integer> arregloA, List<Integer> arregloB) {
        List<Integer> interseccion = new ArrayList<>();
        for (Integer elemento : arregloA) {
            if (arregloB.contains(elemento)) {
                interseccion.add(elemento);
            }
        }
        return interseccion;
    }
}