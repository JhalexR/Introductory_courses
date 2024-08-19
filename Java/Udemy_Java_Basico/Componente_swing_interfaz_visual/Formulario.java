package Udemy_Java_Basico.Componente_swing_interfaz_visual;

import javax.swing.*; // importar libreria swing "*" importa todos lo de la libreria

// se crea una clase extendida de la clase del sistema Jframe
public class Formulario extends JFrame{
    private JLabel label1;  // atributo para la clase del tipo de Jlabel -> clase para mostrar texto en una ventana
    
    // metodo constructor del atributo 
    public Formulario() {
        setLayout(null); // metodo de la Jframe , indica posicionamiento absoluto 
        label1=new JLabel("Hola Mundo."); // texto que a mostrar en la ventana
        label1.setBounds(10,20,200,30); // localizacion inicial y tamaño de ventana
        add(label1); // metodo de la clase Jframe que pasa el control de Jfrme a Jlabel
    }

    // metodo main 
    public static void main(String[] ar) {
        Formulario formulario1=new Formulario(); // creacion de objeto de la clase
        formulario1.setBounds(10,10,400,300); // usamos metodos de las clases Jframe y Jlabel 
        formulario1.setVisible(true); // usamos metodos de las clases Jframe y Jlabel 
    }
}