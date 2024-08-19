package Udemy_Java_Basico.Palabras_reservadas.This_sintaxis;

class Emp {
 int e_id; // atributo de la clase 
 String name; // atributo de la clase 

 Emp(int e_id, String name) { // en el metodo constructor se crean dos variables del mismo nombre que los atributos de clase
  this.e_id = e_id; // se usa la palabra reservada "this" junto con el nombre de atributo para indicar al compilador que se hace referencia
  this.name = name; // al atributo y no a la variable enviada en los argumentos del metodo
 }
 void show() {
  System.out.println(e_id + " " + name);
 }
 public static void main(String args[]) {
  Emp e1 = new Emp(1006, "Karlos"); // creacion de primer objeto 
  Emp e2 = new Emp(1008, "Ray"); // creacion de segundo objeto 
  e1.show(); 
  e2.show();
 }
}