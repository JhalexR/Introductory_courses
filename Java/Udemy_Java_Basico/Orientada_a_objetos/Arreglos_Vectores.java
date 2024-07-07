package Udemy_Java_Basico.Orientada_a_objetos;

import java.util.Scanner;

public class Arreglos_Vectores {

    private Scanner teclado;
	private int[] sueldo; // lo definimos como un atributo de clase ya que se va a utilizar en los dos métodos

    public void cargar(){

      teclado=new Scanner(System.in);
      sueldo=new int[5]; // creamos el array en java los arrays son objetos por eso se utiliza el operador new

      for(int f=0;f<5;f++){ // para almacenar todos los componentes necesitamos un bucle 
      	System.out.print("intoduce sueldo:");
      	sueldo[f]= teclado.nextInt();
      }
    }

    public void imprimir(){
		for(int f=0;f<5;f++){
			System.out.println(sueldo[f]);
		}
	}

    public static void main(String[] ar){
        Arreglos_Vectores usuario = new Arreglos_Vectores();
        usuario.cargar();
        usuario.imprimir();
   }
}