package Udemy_Java_Basico.Orientada_a_objetos.Interfaces_2.Herencia_Interfaces;

import java.util.Scanner;

// clase que va implementar la interfaz padre, pero a su vez tambien
// usará metodo de la clase hija, puede usar el metodo porque al implementar
// la clase padre puede usar las interfaces hijas 

// en esta clase se crean los atributos y se desarrollan los metodos que se van usar
// generalmente desde la clase que contenga el metodo main se crean los objetos que llamaran
// a los metodos de esta clase, en resumen creara los objetos tomando como plantilla esta clase

class SBI implements Empresa{ 
	  private Scanner teclado;
    private float sueldos;
    private float interes;
 
    // metodo de la interfaz "Empresa" que es la clase extendida o hija de la clase "Bank"
    public void datos(){
  	    Scanner teclado=new Scanner(System.in);
        sueldos=teclado.nextInt();    
  }	

   // metodos de la interfaz "Bank" que es la interfaz principal o padre
  public void visualizar(){
  	System.out.println("RESULTADO DE DATOS CLIENTE:" + sueldos);  
  }
  public float rateOfInterest(){
  	interes = (sueldos*9.15f)/100;
	return interes;
  }  
}
/*class PNB implements Bank{  
public float rateOfInterest(){
	return 9.7f;
}  
} */