package Udemy_Java_Basico.Orientada_a_objetos.Interfaces_2.Herencia_Interfaces;

// clase que contendra el metodo main donde se crean los objetos 

class TipoInteres{  

public static void main(String[] args){  
//Bank b=new SBI();  
//System.out.println("ROI: "+b.rateOfInterest()); 
SBI usuario = new SBI(); // creacion de objeto 
usuario.datos(); // metodo de la interfaz hija o extendida "Empresa"
usuario.visualizar(); // metodo de la interfaz padre o principal
//usuario.rateOfInterest();
System.out.println("RESULTADO operación interes es :" + usuario.rateOfInterest());  // metodo de la interfaz padre o principal
}
}  