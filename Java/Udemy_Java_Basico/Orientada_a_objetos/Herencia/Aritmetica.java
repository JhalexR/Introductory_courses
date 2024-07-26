package Udemy_Java_Basico.Orientada_a_objetos.Herencia;	

import java.util.Scanner;

public class Aritmetica {
	protected Scanner t;
	protected int dato1;
	protected int dato2;
	protected int deducir;

	public Aritmetica(){
		t=new Scanner(System.in);

	}

	public void introducirValor1(){
		System.out.print("introduce un numero:");
		dato1=t.nextInt();
	}

	public void introducirValor2(){
		System.out.print("introduce un numero:");
		dato2=t.nextInt();

	}

	public void mostrarResultado(){
		System.out.println(deducir);
	}

}