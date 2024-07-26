package Udemy_Java_Basico.Orientada_a_objetos.Herencia;	

public class Proceso {

	public static void main(String[] args) {
		Adicion usuario1=new Adicion();
		usuario1.introducirValor1();
		usuario1.introducirValor2();
		usuario1.resultado();
		System.out.println("la suma de los dos elementos es:");
		usuario1.mostrarResultado();
		Reducir usuario2=new Reducir();
		usuario2.introducirValor1();
	    usuario2.introducirValor2();
		usuario2.resultado();
		System.out.println("la resta de los dos elementos es:");
		usuario2.mostrarResultado();
		
	}
}