package Udemy_Java_Basico.Orientada_a_objetos.Clases_abstractas;

public class ComprobarInteres{
	public static void main(String args[]){
		Bancos b; // creacion de objeto de la clase bancos 
		b = new BBV(); // al objeto se lo asigna de la clase BBV para poder invocar su metodos obtener TipoInteres
		System.out.println("Tarifa del interés es:" + b.obtenerTipoInteres() + "%"); // usar metodo tipo TipoInteres de la clase BBV
		b = new Santander(); // al objeto se lo asigna de la clase Santander para poder invocar su metodos obtener TipoInteres
		System.out.println("Tarifa del interés es:" + b.obtenerTipoInteres() + "%"); // usar metodo tipo TipoInteres de la clase Santander
	}
}