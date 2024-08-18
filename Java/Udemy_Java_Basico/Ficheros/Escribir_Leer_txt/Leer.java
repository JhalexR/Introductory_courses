package Udemy_Java_Basico.Ficheros.Escribir_Leer_txt;
/*Clase que permite leer un archivo de texto*/
// importamos clases para lectura de ficheros
import java.io.FileReader;
import java.io.BufferedReader;


public class Leer {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// creamos n string que va a contener todo el texto del archivo
		String texto="";
		try{
			// creamos el objeto FileReader que obtiene lo que tenga el archivo 
			FileReader lector= new FileReader("archivo.txt");
			//en contenido del lector se guarda en un bufferedReader
			BufferedReader contenido=new BufferedReader(lector);
			// con el siguiente ciclo extraemos todo el contenido del objeto "contenido" y lo mostramos
			while((texto=contenido.readLine())!=null){
				System.out.println(texto);
            // cerramos objeto "contenido"
            contenido.close();
			}
				
			}catch(Exception e){
				System.out.println("Error al leer");
			}
		}
	}
	
