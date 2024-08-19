package Udemy_Java_Basico.Palabras_reservadas.Final_sintaxis.Atributo_Final;

import java.util.*;
import java.lang.*;
import java.io.*;

// clase principal
class stud {
 final int val; // se usa la palabra reservada "final" para evitar que despues de inicializar la variable pueda ser modificada
 stud() {  // metodo constructor
  val = 60; // variable inicializada
 }
 void method() {
  // se muestra el valor del atributo, si antes de este metodo existiera otro metodo 
  // tratando de modificar el valor no lo permitiria o se generaria un error
  System.out.println(val); 
 }
 public static void main(String args[]) {
  stud S1 = new  stud(); // creacion instancia de la clase para llamar al metodo
  S1.method(); // lamar metodo con el objeto creado
 }
}