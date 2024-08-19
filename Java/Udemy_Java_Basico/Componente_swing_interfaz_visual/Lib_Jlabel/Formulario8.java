package Udemy_Java_Basico.Componente_swing_interfaz_visual.Lib_Jlabel;

import javax.swing.*; // Importamos el paquete javax.swing donde se encuentran definidas las clase JFrame y JLabel
public class Formulario8 extends JFrame { // Heredamos de la clase de JFrame

    // Definimos dos atributos de la clase JLabel
    private JLabel label1,label2;
    public Formulario8() {
        setLayout(null);

        // En el constructor creamos las dos JLabel y las ubicamos llamando al método setBounds, no hay que olvidar de llamar al método add que añade la JLabel al JFrame:
        label1=new JLabel("Sistema de Facturación.");
        label1.setBounds(10,20,300,30);
        add(label1);
        label2=new JLabel("Vesion 1.0");
        label2.setBounds(10,100,100,30);
        add(label2);
    }
        
    public static void main(String[] ar) {
        Formulario8 formularios=new Formulario8(); // creamos un objeto de la clase que acabamos de codificar
        formularios.setBounds(0,0,300,200); // llamamos al setBounds para ubicar y dar tamaño al JFrame
        formularios.setResizable(false);// llamamos al método setResizable pasando el valor false para no permitir modificar el tamaño del JFrame en tiempo de ejecución
        formularios.setVisible(true);// llamamos al método setVisible para que se visualice el JFrame:
    }
}