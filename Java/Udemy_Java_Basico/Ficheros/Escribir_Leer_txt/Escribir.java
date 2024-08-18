package Udemy_Java_Basico.Ficheros.Escribir_Leer_txt;
/*Clase que permite escribir en un archivo de texto*/
// importamos clases para manipulación ficheros
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Escribir {
	public static void main(String []args) throws IOException{
		// creamos en objeto scanner 
		Scanner teclado=new Scanner(System.in);
		// variable para almacenar los valores introducidos por teclado
		String contenido;
		try{
		// comentario para que el usuario sepa que tiene que introducir por teclado
		System.out.println("introduce un texto:");
		// varoles introducidos por teclado
		contenido=teclado.nextLine();
		/*Crear un objeto file se encarga de crear o abrir acceso a un arhivo que se especifica 
		en el constructor*/
		File archivo=new File("archivo.txt");
		// crea objeto fileWrite que será el que nos ayude  escribir sobre archivo
		FileWriter escribir=new FileWriter(archivo, true);
		//Escribimos en el archivo con el método write
		escribir.write(contenido);
		// cerramos la conexión
		escribir.close();
		// si existe un problema al escribir se crea una excepción
		}catch(Exception e){
			System.out.println("Error al escribir");
		}
		
		
	}

}
