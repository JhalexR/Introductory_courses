package Estudio_Autonomo.Interfaces;

//Conceptos

//Paquetes organizan clases e interfaces.
//Clases contienen métodos y pueden implementar interfaces.
//Objetos son instancias de clases.
//Interfaces definen métodos que las clases deben implementar.
//Métodos son funciones definidas dentro de clases.

// Definición de clase que implementa la interfaz
public class Perro implements Animal {
    private String nombre;

    public Perro(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public void hacerSonido() {
        System.out.println("Guau");
    }

    public void saludar() {
        System.out.println("Hola, mi nombre es " + nombre);
    }
}