package Udemy_Java_Basico.Palabras_reservadas.Static_sintaxis;


public class egStatic {
    static int x = 60; // variable "static" solo se inicializa una vez pertenece a la clase
    static void fun() { // metodo "static" 
        System.out.println("Within Static");
    }
// metodo main
public static void main(String[] args) {
  egStatic.fun();  // se accede directamente con la clase al metodo "fun" sin necesidad de crear objeto
  System.out.println(egStatic.x); // se accede directamente al valor de "x" sin necesidad de crear objeto
  egStatic S1 = new egStatic(); // creacion de primer objeto
  egStatic S2 = new egStatic(); // creacion de segundo objeto
  System.out.println(S1.x); // uso de primer objeto se puede acceder a la variable "static" con un objeto pero no es necesario
  S2.fun(); // uso de segundo objeto se puede acceder al metodod "static" con un objeto pero no es necesario
}
}