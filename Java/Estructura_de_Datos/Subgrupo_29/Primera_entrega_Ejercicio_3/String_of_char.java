package Estructura_de_Datos.Subgrupo_29.Primera_entrega_Ejercicio_3;

import java.util.Scanner;

public class String_of_char {

    protected String sequence[];    
    protected int array_size;
    protected int chain_size;
    protected int prompter;
    protected Scanner Dat;

    public String_of_char(){
        
        System.out.print("Introduce el tamaño del arreglo: ");
        Dat = new Scanner(System.in); 
        array_size = Dat.nextInt();
        sequence = new String[array_size-1];
        for(int f=0;f<array_size;f++) 
            sequence[f] = null;
        chain_size = 0;
        prompter = 0;

    }

    public void fill_out_array (){

        System.out.println("Escribe una frase, al finalizar presiona enter: ");
        for(int f=0;f<array_size;f++)        
            sequence[f] = Dat.nextLine();
            
    }


    public static void main(String[] args) {
        
    }
    
}
