package Udemy_Java_Basico.Orientada_a_objetos;

import java.util.Scanner;

// al momento de la creación de un arreglo es generada una variable inmutable que contiene su tamaño. 

public class Matriz_Con_lenght {

    private Scanner teclado;
    private int[][] mat;	//creacion de matriz 
    

    public void cargar() {
        teclado=new Scanner(System.in);
        System.out.print("Cuantas fila tiene la matriz:");
        int filas=teclado.nextInt();
        System.out.print("Cuantas columnas tiene la matriz:");
        int columnas=teclado.nextInt();
        //Para acceder a dicha variable se debe escribir el nombre del arreglo seguido de un punto,
        // seguido de la palabra length: <nombre_arreglo>.length.
        mat=new int[filas][columnas];
        for(int f=0;f<mat.length;f++) {	//llenar las filas con la funcion lenght
            for(int c=0;c<mat[f].length;c++) {	//llenar las columnas con la funcion lenght
                System.out.print("Ingrese componente:");
                mat[f][c]=teclado.nextInt();
            }
        }
    }
    
    public void imprimir() {
        for(int f=0;f<mat.length;f++) {	//recorrer y mostrar contenido de las filas con el metodo lenght
            for(int c=0;c<mat[f].length;c++) {	//recorrer y mostrar contenido de las columnas con el metodo lenght
                System.out.print(mat[f][c]+" ");
            }
            System.out.println();
        }
    }
    
    public void imprimirUltimaFila() {
    	System.out.println("Ultima fila");
        
        // Cuando un arreglo ya tiene ingresados elementos,  se puede usar el metodo leght 
        //para ir elemento por elemento y asi hacer operaciones hasta su utimo elemento 
        //sin necesidad de capturar en otra variable la cantidad de elementos que tiene
        for(int c=0;c<mat[mat.length-1].length;c++) {
             System.out.print(mat[mat.length-1][c]+" ");//mostrar la ultima fila usando el metodo lenght
        }
    }
    
    public static void main(String[] ar) {
        Matriz_Con_lenght matriz2=new Matriz_Con_lenght ();	//creacion del objeto
        matriz2.cargar();
        matriz2.imprimir();
        matriz2.imprimirUltimaFila();
    }

}
