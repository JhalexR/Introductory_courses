package Estructura_de_Datos.Subgrupo_29.Primera_entrega_Ejercicio_3;

/*  Authors: 
    John Alexander Peñaloza Rojas
    
    Modulo: Estructura de datos - Segundo semestre 2024
    Grupo: B01 - subgrupo: 29
    fecha: 05/09/2024
*/

import java.util.Scanner;

public class String_of_char {

    // creacion de atributos 
    protected String sequence[];    
    protected int array_size;
    protected int chain_size;
    protected int prompter;
    protected Scanner Dat;


    /* metodo constructor */
    public String_of_char () {
        
        // se inicializan los atributos de la clase
        System.out.print("Introduce el tamaño del arreglo: ");
        Dat = new Scanner(System.in); // se solicita al usuario el tamaño total del arreglo
        array_size = Dat.nextInt();
        sequence = new String[array_size];
        chain_size = 0;
        prompter = 0;

    }

    public void mostrar_1 (){
        for(int f = 0; f < array_size; f++) {
            System.out.print(sequence[f]);
            System.out.print(f);
        }
    }

    // metodo con el cual se capturan la(s) palabra(s) dentro del arreglo
    public void fill_out_array () {
        
        
        for(int f=0; f < sequence.length; f++) 
        System.out.println("Escribe la cadena numero: "+f+" y al finalizar presiona enter: ");
        sequence[f] = Dat.nextLine();        
               
    }

    public void mostrar_2 (){
        for(int f = 0; f < array_size; f++) {
            System.out.print(sequence[f]);
            System.out.print(f);
        }
    }


    // metodo con el cual se busca en el arreglo donde inicia la palabra mas larga 
    public void loop_array () {
        
        int chain_size, prompter, f; // variables del metodo se llaman igual que los atributos para facilitar entender su funcion
        chain_size = prompter = f = 0;
        do  {
            if (sequence[f] != " ") {
                chain_size++;
                f++;
            } else if (chain_size > this.chain_size){ // en esta parte del ciclo se captura el indice y tamaño de la palabra mas larga
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

    // metodo para mostar la palabra mas larga asi como su posicion de inicio dentro del arreglo
    public void longest_word () {

        System.out.println("La palabra mas larga en el arreglo inicia en la posición: "+prompter);
        System.out.println("La palabra mas larga en el arreglo es: ");
        for(int f = prompter; f < chain_size; f++) 
            System.out.print(sequence[f]);

    }

    // metodo main para creacion de objetos e invocar los metodos
    public static void main(String[] args) {

        String_of_char String_1 = new String_of_char();
        String_1.mostrar_1();
        String_1.fill_out_array();
        String_1.mostrar_2();
        String_1.loop_array();
        String_1.longest_word();        
        
    }
    
}
