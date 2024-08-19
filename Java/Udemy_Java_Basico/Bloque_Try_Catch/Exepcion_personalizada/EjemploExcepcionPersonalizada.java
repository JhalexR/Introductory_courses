package Udemy_Java_Basico.Bloque_Try_Catch.Exepcion_personalizada;

public class EjemploExcepcionPersonalizada {
    public static void main(String[] args) {
        try {
            lanzarExcepcion();
        } catch (MiExcepcionPersonalizada e) {
            System.out.println("Se capturó una excepción personalizada: " + e.getMessage());
        }
    }

    public static void lanzarExcepcion() throws MiExcepcionPersonalizada {
        throw new MiExcepcionPersonalizada("Este es un mensaje de una excepción personalizada.");
    }
}
