package Udemy_Java_Basico.Orientada_a_objetos.Clases_abstractas;

// una clase de la que no se tiene intencion de crear objetos, si no que
// unicamente servira para unificar datos y operaciones de subclases
// puede declararse de manera especial en java como clase abstracta

// es una clase que declara existencia de metodos 
// pero no la implementacion de dichos metodos

// una clase abstracta puede contener metodos no abstractos 
// pero al menos uno de ellos debe ser abstracto

// metodo abstracto
// debe llevar la palabra reservada abstract 
// termnina en ";"
// solo puede ir en una clase abstracta

// palabra reservada abstract sirve para declarar clase asbtracta
abstract class Bancos{  
	abstract public int obtenerTipoInteres();
}