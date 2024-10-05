import java.util.HashSet; 
import java.util.Set;  

public class Subconjunto {    

    public static boolean esSubconjunto(int[] S, int[] T) {    

        // Creamos un HashSet para almacenar los elementos de T  
        Set<Integer> conjuntoT = new HashSet<>();  
        for (int t : T) {  
            conjuntoT.add(t);  
           }   

        // Verificamos si cada elemento de S está en T  
        for (int s : S) {  
            if (!conjuntoT.contains(s)) {  
                return false; // Si un elemento de S no está en T, S no es subconjunto de T  
            }  
        }   
        return true; // Todos los elementos de S están en T, por lo tanto, S es subconjunto de T  
    }  

    public static void main(String[ ] args) {  
        int[ ] S = {1, 2, 3};  
        int[ ] T = {1, 2, 3, 4, 5};  
        boolean esSubconjunto = esSubconjunto(S, T);  
        System.out.println("S es subconjunto de T: " + esSubconjunto);  
    }  
} 