package Udemy_Java_Basico.Orientada_a_objetos.Polimorfismo_sobre_escritura_metodos;

public class Ejecucion {
	public static void main(String[] args) {
		Perro2 objeto = new Perro2();
		Gato objeto2 = new Gato();
		Caballo2 objeto3 = new Caballo2();
		objeto.sonido();
		objeto2.sonido();
		objeto3.sonido();
  
	}	
}