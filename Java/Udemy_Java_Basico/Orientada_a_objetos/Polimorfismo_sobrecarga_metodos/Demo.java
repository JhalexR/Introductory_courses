package Udemy_Java_Basico.Orientada_a_objetos.Polimorfismo_sobrecarga_metodos;

public class Demo {
     public Static void main(String[] args) { 
           Lectura objeto = new Lectura();
           // Se invoca el mismo metodo y se usa el que coincida con el tipo 
           // y cantidad de argumentos
           objeto.print(10);   
           objeto.print(“arte”);
           objeto.print(“hola”, 34);
      }
}   