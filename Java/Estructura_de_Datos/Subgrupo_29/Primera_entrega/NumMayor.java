package Estructura_de_Datos.Subgrupo_29.Primera_entrega;

/*  Author: 
    John Alexander Peñaloza Rojas
    
    Modulo: Estructura de datos - Segundo semestre 2024
    Grupo: B01 - subgrupo: 29
    fecha: 05/09/2024
*/

import java.util.Scanner;
import java.util.Arrays; 

public class NumMayor {

	public static void main(String[] args) 
	{
		int[] numero; // declaración de variable
		numero = new int[10]; // longitud de 10 elementos

		Scanner digito = new Scanner(System.in);
				
        for (int x=0; x<10; x++)
        {
		   System.out.print("Introduce el número de la posicion "+(x+1)+" :");
		   numero[x]=digito.nextInt();           			
		}

        Arrays.sort(numero); /* funcion para ordenar arrays */
		System.out.println(" El segundo número mayor es: " + numero[8]); /*se muestra por consola el segundo numero mas alto */

        digito.close();
    }
}