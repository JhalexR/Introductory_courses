package Udemy_Java_Basico.Orientada_a_objetos.Encapsulamiento;

public class Persona {

	private String nombre;
	private String apellido;
	private int edad;

	public Persona(){
		nombre= "Carlos";
		apellido="Blanco";
		edad=47;

	}

	// El método get al igual que el set, es un método público, pero el get se encarga de mostrar un valor a una propiedad 
	// o atributo de un objeto, el cual está encapsulado en la clase correspondiente, es decir, esta declarado con la palabra 
	// reservada private o protected.	
	public String getApellido(){ // desde la clase secundaria Trabajador se invoca este metodo para que muestre el apellido  
		return apellido;
	}

	// El método set es un método público, el cual se encarga de darle un valor a una propiedad o atributo de un objeto, 
	// el cual está encapsulado en la clase correspondiente, es decir, 
	// esta declarado con la palabra reservada private o protected.
	public void setApellido(String apellido){ // desde la clase secundaria Trabajador se invoca este metodo para que se modifique el apellido  
		this.apellido = apellido;  // this: es la palabra reservada para referirnos a las variables de la misma clase en la que se utiliza.
	}

	public int getEdad(){ // desde la clase secundaria Trabajador se invoca este metodo para que muestre la edad
		return edad;
	}

	public void setEdad(int edad){ // desde la clase secundaria Trabajador se invoca este metodo para que se modifique la edad
		this.edad = edad; // this: es la palabra reservada para referirnos a las variables de la misma clase en la que se utiliza.
	}

	public String getNombre(){ // desde la clase secundaria Trabajador se invoca este metodo para que muestre el nombre
		return nombre;
	}

	public void setNombre(String nombre){ // desde la clase secundaria Trabajador se invoca este metodo para que se modifique el nombre
		this.nombre = nombre; // this: es la palabra reservada para referirnos a las variables de la misma clase en la que se utiliza.
	}

}