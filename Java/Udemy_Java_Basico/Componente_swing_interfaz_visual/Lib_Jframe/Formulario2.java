package Udemy_Java_Basico.Componente_swing_interfaz_visual.Lib_Jframe;

import javax.swing.*; // Importamos el paquete donde se encuentra la clase JFrame:
public class Formulario2 extends JFrame{ // Planteamos una clase que herede de la clase JFrame:
    public Formulario2() {
        setLayout(null); // En el constructor indicamos que ubicaremos los controles visuales con coordenadas absolutas mediante la desactivación del Layout heredado
    }

    // metodo main
    public static void main(String[] ar) {
        Formulario2 formulario1=new Formulario2(); // creamos un objeto de la clase 
        //  llamamos a los métodos setBounds y setVisible
        formulario1.setBounds(10,20,400,300); // El método setBounds ubica el JFrame (la ventana) en la columna 10, fila 20 con un ancho de 400 píxeles y un alto de 300.
        formulario1.setVisible(true); // Debemos llamar al método setVisible y pasarle el valor true para que se haga visible la ventana.
    }
}