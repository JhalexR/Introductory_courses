package Udemy_Java_Basico.Bloque_Try_Catch;

public class EjemploTryCatch {
    public static void main(String[] args) {
        try {
            int division = 10 / 0;  // Esto causará una excepción de tipo ArithmeticException
            System.out.println("El resultado es: " + division);
        } catch (ArithmeticException e) {
            // Aquí manejamos la excepción
            System.out.println("Error: División por cero no permitida.");
        }
        
        System.out.println("El programa continúa después del bloque try-catch.");
    }
}
