package Estructura_de_Datos.Subgrupo_29.Primera_entrega_Ejercicio_3;

/*Author: John Alexander Peñaloza Rojas
 * 
*/

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
        for(int f = 0;f < array_size; f++) 
            sequence[f] = null;
        chain_size = 0;
        prompter = 0;

    }


    public void fill_out_array () {

        System.out.println("Escribe una frase, y al finalizar presiona enter: ");
        for(int f = 0;f < array_size; f++)        
            sequence[f] = Dat.nextLine();
        
        

    }


    public void loop_array () {
        
        int chain_size, prompter, f;
        chain_size = prompter = f = 0;
        do  {
            if (sequence[f] != " ") {
                chain_size++;
                f++;
            } else if (chain_size > this.chain_size){
                this.chain_size = chain_size;
                this.prompter = prompter;
                chain_size = 0;
                f++;
                if (sequence[f] != " ")
                    prompter = f; 
                else 
                    f++;
            }
            else 
                f++;            
        } while (sequence[f] != null);

    }


    public void longest_word () {

        System.out.println("La palabra mas larga en el arreglo inicia en el indice: "+prompter);
        System.out.println("La palabra mas larga en el arreglo es: ");
        for(int f = prompter; f < chain_size; f++) 
            System.out.print(sequence[f]);

    }

    public static void main(String[] args) {

        String_of_char String_1 = new String_of_char();
        String_1.fill_out_array();
        String_1.loop_array();
        String_1.longest_word();        
        
    }
    
}
