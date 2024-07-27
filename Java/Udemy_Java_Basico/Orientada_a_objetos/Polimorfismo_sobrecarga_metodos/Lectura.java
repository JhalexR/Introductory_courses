package Udemy_Java_Basico.Orientada_a_objetos.Polimorfismo_sobrecarga_metodos;

// el polimorfismo se puede realizar por sobre carga de métodos como en este jemplo
public class  Lectura {
   // Los metodos se llaman igual se invocan desde la otra clase dependiendo
   // de la cantidad y pipo de datos de los argumentos
   public void print (String s){
       System.out.println(“primer método con sólo un string- “ + s);
    }
    public void print (int i){
       System.out.println(“primer método con sólo un entero- “ + i);
    }
     public void print (String s, int i){
       System.out.println(“primer método con un string y un entero “ + s);
    }
}