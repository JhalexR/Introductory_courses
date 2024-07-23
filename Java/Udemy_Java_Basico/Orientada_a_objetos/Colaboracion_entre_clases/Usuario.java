package Udemy_Java_Basico.Orientada_a_objetos.Colaboracion_entre_clases;

//import libreria.Entidad;
//import Udemy_Java_Basico.Orientada_a_objetos.Colaboracion_entre_clases.Entidad;

public class Usuario {
    
    private String nombreCliente;
    private int cantidad;
    
    public Usuario(String nom) {
        nombreCliente=nom;
        cantidad=0;
    }
    
    public void ingresar(int m) {
        cantidad=cantidad+m;
    }
    
    public void reintegro(int m) {
        cantidad=cantidad-m;
    }
    
    public int retornoDeCantidad() {
        return cantidad;
    }
    
    public void visualizar() {
        System.out.println(nombreCliente+" INGRESADO EN CUENTA: "+cantidad);
    }
}
