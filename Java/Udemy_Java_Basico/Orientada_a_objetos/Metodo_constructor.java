package Udemy_Java_Basico.Orientada_a_objetos;

import java.util.Scanner;

// En java se puede crear un metodo que se va a ejecutar primero y cuya principal funcion es crear atributos

public class Metodo_constructor {

    private Scanner s;
    private String[] Constructor1;
    
    //metodo constructor se ejecuta automaticamente y solo una vez
    public Metodo_constructor(){ //metodo constructor lleva el mismo nombre de la clase, No debe retornar valores
    
        s=new Scanner(System.in);   //Crea los atributos de la clase s del tipo Scanner
        Constructor1=new String[5]; //y Constructor1 array de tipo string
        for(int f=0;f<5;f++) {
            System.out.print("Introduce nombre del metodo constructor:");
            Constructor1[f]=s.next();
        }   
    }
    
    public void visualizar() {
        for(int f=0;f<5;f++) {
            System.out.println(Constructor1[f]);
        }
    }
    
    public static void main(String[] ar) {
        Metodo_constructor Constructor=new Metodo_constructor(); //creacion de objeto
        Constructor.visualizar(); //aunque no se hallamado desde el main al metodo constructor
                                  //se ejecuta primero y automaticamente sin llamarlo desde el main
    }

}
