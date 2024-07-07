package Udemy_Java_Basico.Orientada_a_objetos;

import java.util.Scanner;
import java.util.Arrays;  // utilizamos la clase Arrays

public class Arreglos_ordenar_ascendente {

    private Scanner teclado;
	private int[] sueldo; // lo definimos como un atributo de clase ya que se va a utilizar en los dos métodos

    public void cargar(){
        teclado=new Scanner(System.in);
        sueldo=new int[5]; // creamos el array en java los arrays son objetos por eso se utiliza el operador new
        for(int f=0;f<sueldo.length;f++){ // para almacenar todos los componentes necesitamos un bucle 
            System.out.print("intoduce sueldo:");
            sueldo[f]= teclado.nextInt();
        }
      }
      public void ordenar(){
          Arrays.sort(sueldo);  // *****utilizamos el método sort *******
      }
      public void imprimir(){
          for(int f=0;f<sueldo.length;f++){
              System.out.println(sueldo[f]);
          }
      }

    public static void main(String[] ar){
        Arreglos_ordenar_ascendente usuario = new Arreglos_ordenar_ascendente();
        usuario.cargar();
        usuario.ordenar();
        usuario.imprimir();
   }

}
