package Udemy_Java_Basico.Orientada_a_objetos;

import java.util.Scanner;

public class Matrices {

    private Scanner teclado;
    private int[][] mat;      //creacion de matriz 
    
    //metodo para llenar la matriz con datos 
    public void cargar() {
        teclado=new Scanner(System.in);
        mat=new int[3][5];
        for(int f=0;f<3;f++) {      //con este ciclo for se llenan las filas
            for(int c=0;c<5;c++) {   //con este ciclo for se llenan las columnas
                System.out.print("Ingrese componente:");   //la fila se mantiene mientras aumentan las columnas
                mat[f][c]=teclado.nextInt();                 //para llenar primero la informacion de toda la fila
            }
        }
    }
    
    public void imprimir() {
        for(int f=0;f<3;f++) {      //con este ciclo for se recorre las filas
            for(int c=0;c<5;c++) {  //con este ciclo for se recorre las columnas
                System.out.print(mat[f][c]+" ");  //al igual que en el paso de llenado primero se recorre la fila
            }
            System.out.println();    //cuando se termina la fila hay salto de linea para la otra fila
        }
    }
    
    public static void main(String[] ar) {
        Matrices matriz1=new Matrices(); //creacion del objeto
        matriz1.cargar();                //invocar metodos cargar
        matriz1.imprimir();		    //invocar metodos imprimir
    }

}
