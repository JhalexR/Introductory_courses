package Udemy_Java_Basico.Orientada_a_objetos.Interfaces_2.Interface_1;

// esta es la clase donde va a estar el metodo main 
// en esta clase se crean los objetos 
// que van a utilizar los metodos de la interfaz 

public class Test {
    public static void main(String args[]){  
        Circulo2 d=new Circulo2(); 
        Rectangulo c=new Rectangulo();
        d.draw();  
        c.draw();
      }
}