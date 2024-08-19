package Udemy_Java_Basico.Palabras_reservadas.Final_sintaxis.Metodo_Final;

class stud { // clase principal
    final void show() { // metodo declarado como final de la clase principal
        System.out.println("Class - stud : method defined");
    }
}

// clase secundaria o extendida
class books extends stud {

    // intento por sobreescribir el metodo en la clase secundaria 
    // esta parte va en comentario para evitar la notificacion de error 
    // debido a que no se puede sobreescribir un metodo declarado como "final"
 
    /*void show() {
    //System.out.println("Class - books : method defined");
    }*/

    // metodo main 
    public static void main(String args[]) {
        books B2 = new books(); // instancia de clase secundaria
        B2.show(); // se llama al metodo con el objeto creado
    }
}
/*Un método declarado como final no puede ser anulado; esto significa que 
incluso cuando una clase hija puede llamar al método final de la clase principal 
sin ningún problema, la anulación no será posible. Aquí hay un programa de muestra
 que muestra lo que no es válido dentro de un programa Java cuando un método se 
 declara como final.*/