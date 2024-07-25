package Udemy_Java_Basico.Orientada_a_objetos.Encapsulamiento;

// esta es la clase secundaria

// Extends indica la herencia entre una clase secundaria y una principal. 
// Extends En Java es una palabra clave que se escribe con la clase secundaria 
// durante la declaración de la clase seguida del nombre de la clase principal.
public class Trabajador extends Persona{ 
	//private String nombre2;	

	public static void main(String[] ar) {
       // Persona usuario=new Persona("Carlos", "Blanco", 47);
        Trabajador usuario2 = new Trabajador();
        // Comprobamos que se introducieron los datos el los atributos de la clase Persona()
        System.out.println(" Los datos de los atributos orignales desde la clase Persona son: "+usuario2.getNombre()+"---"+usuario2.getApellido()+"---"+usuario2.getEdad());
        // modificamos el atributo nombre que pertenece a la clase Persona() desde la clase Trabajador() gracias al método set
        usuario2.setNombre("Nadia");
        // visualizamos como sea modificado
        System.out.println("el nombre encapsulado modificado desde la clase Trabador con el método setters es:"+usuario2.getNombre());
        // modificamos el atributo apellido que pertenece a la clase Persona() desde la clase Trabajador() racias a método set
        usuario2.setApellido("Loeches");
        System.out.println("el apellido encapsulado modificado desde la clase Trabajador con el método setters es:"+usuario2.getApellido());
        usuario2.setEdad(14);
        System.out.println("la edad encapsulado modificada desde la clase Trabajador con el método setters es:"+usuario2.getEdad());
        // Ahora podemos modificar el atributos desde una clase a a le no pertenecer
                
    }	

}