/*  Author: 
    John Alexander Peñaloza Rojas    
    Modulo: Estructura de datos - Segundo semestre 2024
    Grupo: B01 - subgrupo: 29
    fecha: 05/10/2024
*/

package Estructura_de_Datos.Subgrupo_29.Tercera_entrega.Version_propia;

// Clase Nodo del árbol binario
public class Nodo {
    int valor;
    Nodo izquierdo;
    Nodo derecho;

    public Nodo(int valor) {
        this.valor = valor;
        this.izquierdo = null;
        this.derecho = null;
    }
}