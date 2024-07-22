package Udemy_Java_Basico.Orientada_a_objetos;

// la clase string en java nos permite hacer operaciones entre varibales de 
// tipo string como compararlas, contarlas, extraer
// equals -> retorna true o false al comprar dos string teniendo en cuenta mayusculas y minusculas
// equalsIgnoreCase -> retorna true o false al comprar dos string sin tener en cuenta mayusculas y minusculas
// compareTo -> compara dos string alfabeticamente
// charAt -> extrae un char de un string a partir de una posicion
// legth -> retorna la cantidad de caracteres del string
// substring -> retorna un substring a partir de una posicion
// indexof -> retorna -1 si un string no esta contenido en otro
// toUpperCase -> convierte todos los caracteres del string en mayusculas
// toLowerCase -> convierte todos los caracteres del string en minusculas

import java.util.Scanner;

public class Metodos_clase_string {
        private Scanner teclado=new Scanner(System.in);
        private String cad1;
        private String cad2;
    
    public Metodos_clase_string()
    {
        System.out.print("Ingrese la primer cadena:");
        cad1=teclado.nextLine();
        System.out.print("Ingrese la segunda cadena:");
        cad2=teclado.nextLine();
    }
    
    public void visualizar() {
         if (cad1.equals(cad2)==true) { // equals -> retorna true o false al comprar dos string teniendo en cuenta mayusculas y minusculas
            System.out.println(cad1+" es exactamente igual a "+cad2);
        } else {
            System.out.println(cad1+" no es exactamente igual a "+cad2);        
        }
        if (cad1.equalsIgnoreCase(cad2)==true) { // equalsIgnoreCase -> retorna true o false al comprar dos string sin tener en cuenta mayusculas y minusculas
            System.out.println(cad1+" es igual a "+cad2+" sin tener en cuenta mayúsculas/minúsculas");
        } else {
            System.out.println(cad1+" no es igual a "+cad2+" sin tener en cuenta mayúsculas/minúsculas");        
        }
        if (cad1.compareTo(cad2)==0) { // compareTo -> compara dos string alfabeticamente
            System.out.println(cad1+" es exactamente igual a "+cad2);
        } else {
            if (cad1.compareTo(cad2)>0) {
                System.out.println(cad1+ " es mayor alfabéticamente que "+cad2);
            } else {
                System.out.println(cad2+ " es mayor alfabéticamente que "+cad1);            
            }
        }        
        char carac1=cad1.charAt(0);  // charAt -> extrae un char de un string a partir de una posicion
        System.out.println("El primer caracter de "+cad1+" es "+carac1);
        int largo=cad1.length(); // legth -> retorna la cantidad de caracteres del string
        System.out.println("El largo del String "+cad1+" es "+largo);
        String cad3=cad1.substring(0,3); // substring -> retorna un substring a partir de una posicion
        System.out.println("Los primeros tres caracteres de "+cad1+" son "+cad3);
        int posi=cad1.indexOf(cad2); // indexof -> retorna -1 si un string no esta contenido en otro
        if (posi==-1) {
            System.out.println(cad2+" no está contenido en "+cad1);
        } else {
            System.out.println(cad2+" está contenido en "+cad1+" a partir de la posición "+posi);
        }
        System.out.println(cad1+ " convertido a mayúsculas es "+cad1.toUpperCase()); // toUpperCase -> convierte todos los caracteres del string en mayusculas
        System.out.println(cad1+ " convertido a minúsculas es "+cad1.toLowerCase()); // toLowerCase -> convierte todos los caracteres del string en minusculas       
    }
    
    public static void main(String[] ar) {
        Metodos_clase_string op=new Metodos_clase_string();
        op.visualizar();
    }
}



