package Udemy_Java_Basico.Palabras_reservadas.Super_sintaxis;

class employee { // clase principal
 int wt = 8; // atributo de la clase principal 
}

class clerk extends employee { // 
 int wt = 10;  // atributo de la clase secundaria tiene el mismo nombre del atributo la clase principal
 void display() {
  // aca la expresion "super.wt" hace referencia al atributo "wt" de la clase "employee" 
  // y no al de clase "clerk", se usa "super" porque tienen el mismo nombre
  System.out.println(super.wt); 
 }

 public static void main(String args[]) {
  clerk c = new clerk();
  c.display();
 }

}
/*Instance refiere una variable de instancia de la clase actual de forma 
predeterminada, pero cuando debe referir la variable de instancia de clase
 principal, debe usar la palabra clave super para distinguir entre la variable 
 de instancia de la clase principal (aquí empleado) y la variable de instancia de 
 la clase actual (aquí, empleado) .*/