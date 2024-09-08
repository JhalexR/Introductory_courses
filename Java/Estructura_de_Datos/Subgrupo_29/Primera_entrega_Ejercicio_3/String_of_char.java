package Estructura_de_Datos.Subgrupo_29.Primera_entrega_Ejercicio_3;

/*  Author: 
    John Alexander Peñaloza Rojas
    
    Modulo: Estructura de datos - Segundo semestre 2024
    Grupo: B01 - subgrupo: 29
    fecha: 05/09/2024
*/

import java.util.Scanner;

public class String_of_char {

    /* creacion de atributos */
    protected String sequence[];    
    protected int size;
    protected int prompter;
    protected Scanner Dat;


    /* metodo constructor */
    public String_of_char () {        
        // se inicializan los atributos de la clase
        System.out.print("Introduce la cantidad de palabras a almacenar: ");
        Dat = new Scanner(System.in); // se solicita al usuario el tamaño total del arreglo
        size = Dat.nextInt();
        sequence = new String[size];        
        prompter = 0;
    }

    /* metodo con el cual se capturan la(s) candena(s) dentro del arreglo */
    public void fill_out_array () { 
        System.out.println();       
        for(int f=0; f < size; f++) {
        System.out.print("Escribe la palabra numero: "+(f+1)+" y presiona enter: ");
        sequence[f] = Dat.next();        
        } 
    }

    /* metodo con el cual se busca la palabra mas larga en el arreglo */
    public void check_array () {
        int a = 0;        
        for(int f=0; f < size; f++)
            if (a < sequence[f].length()) {
                a = sequence[f].length();
                prompter = f;
            }
    }

    /* metodo para mostar la palabra mas larga asi como su posicion dentro del arreglo */
    public void longest_word () {
        System.out.println();
        System.out.println("La palabra mas larga en el arreglo esta en la posición: "+(prompter+1));
        System.out.print("La palabra mas larga en el arreglo es: ");
        System.out.print(sequence[prompter]);
    }

    /* metodo main para creacion de objetos e invocar los metodos */
    public static void main(String[] args) {
        String_of_char String_1 = new String_of_char();
        String_1.fill_out_array();
        String_1.check_array();
        String_1.longest_word();                
    }    
}