package Estructura_de_Datos.Tablas_Hash;

import java.util.Hashtable; /* La declaracion de la tabla hash se realiza importando este conjunto */

public class HashTable2 {

    public static void main(String[ ] args){

        int aux[] = {49, 43, 65, 45, 67, 68, 97};
        Hashtable<Integer, Integer> tablahash = new Hashtable<>();
        /* La palabra reservada es HashTable <Tipo de dato, tipo de llave>
           seguido por el nombre de la tabla = la creacion de objeto */

        for (int i=0; i<=aux.length;i++){
            tablahash.put(Math.abs(aux[i])%7, aux[i]);
        }

        System.out.println(tablahash);
    }
}