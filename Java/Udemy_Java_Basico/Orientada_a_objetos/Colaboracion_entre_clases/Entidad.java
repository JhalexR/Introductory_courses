package Udemy_Java_Basico.Orientada_a_objetos.Colaboracion_entre_clases;

//import libreria.Usuario;
//import Udemy_Java_Basico.Orientada_a_objetos.Colaboracion_entre_clases.Usuario;

public class Entidad {
    private Usuario usuario1,usuario2,usuario3; // se crea atributos objetos de la clase Usuario pero se crean en esta clase
    
    public Entidad() { // metodo constructor para inicializar atributos de la clase usuario
        usuario1=new Usuario("Javier Perez Aguirre"); // se invoca al metodo constructor de la clase Usuario para dar otro valor
        usuario2=new Usuario("Nadia Blanco Loeches"); // a los atributos objetos
        usuario3=new Usuario("Carlos Blanco Gómez"); 
    }

    public void manipular() {  // metodo para llamar dos metodos de la clase Usuario 
        usuario1.ingresar (2167); 
        usuario2.ingresar (34876);
        usuario3.ingresar (12534);
        usuario3.reintegro (546);
    }
    
    public void fondos ()  { // metodo que opera los datos para llamar a un metodo de la clase usuario que visualiza datos
        int t = usuario1.retornoDeCantidad () + usuario2.retornoDeCantidad () + usuario3.retornoDeCantidad ();
        System.out.println ("TOTAL DE EFECTIVO INGREGADO EN LA ENTIDAD ES:" + t);
        usuario1.visualizar();
        usuario2.visualizar();
        usuario3.visualizar();
    }

    public static void main(String[] ar) { // metodo main desde aca inicia el codigo por lo tanto no hay main en la clase usuario
        Entidad sucursal=new Entidad();
        sucursal.manipular();
        sucursal.fondos();
    }
}
