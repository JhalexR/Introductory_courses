package Estructura_de_Datos.Tablas_Hash;

import java.util.Hashtable; /* La declaracion de la tabla hash se realiza importando este conjunto */

public class HashTable2 {

    public static void main(String[] args){

        int aux[] = {49, 43, 65, 45, 67, 68, 97};
        Hashtable<Integer, Integer> tablahash = new Hashtable<>();
        /* La palabra reservada es Hashtable <Tipo de dato, tipo de llave>
           seguido por el nombre de la tabla = la creacion de objeto */

        for (int i=0; i<aux.length;i++){
            tablahash.put(Math.abs(aux[i])%7, aux[i]);
        }

        System.out.println(tablahash);

        // busqueda en tabla hash "contains" y "get"
        System.out.println("el valor 97 se encuentra en : "+tablahash.contains(97));
        System.out.println("cuenta con posicion 6 : "+tablahash.contains(6));
        System.out.println("valor de la posicion 6 : "+tablahash.get(6));

        // eliminar en tabla hash
        tablahash.remove(6);

        //verificar si esta vacia
        System.out.println("la tabla hash esta vacia? "+tablahash.isEmpty());

        // vaciar tabla hash
        tablahash.clear();
    }
}