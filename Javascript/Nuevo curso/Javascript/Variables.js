/* 
variables 
Almacenan valores 
 */

/*
tres formas de definir variables: 
var
let
const
*/

/* 
variables con var: 
var se usa para declarar variables de manera global o local a una función, pero no a un bloque de código.
var se puede redeclarar y reasignar, lo que puede llevar a errores si no se tiene cuidado.
*/

// declaracion con var
var nombre = "Juan";

//redefinir variables con var
nombre = "Pedro";

//imprimir variables
console.log(nombre);

/* uso de var con objetos */
var persona = {
  nombre: "Juan",
  apellido: "Perez",
  edad: 30,
  direccion: {
    calle: "Calle 1",
    numero: 123,
    ciudad: "Madrid",
  },
  ciudadesVisitadas: ["Madrid", "Barcelona", "Paris"],
};

console.log(persona);


/* 
variables con let: 
let se usa para declarar variables de manera local a un bloque de código, 
lo que significa que solo están disponibles dentro del bloque donde se declaran.
let se puede reasignar, pero no se puede redeclarar dentro del mismo bloque de código,
lo que ayuda a evitar errores.   
*/

// declaracion con let
let nombre2 = "Maria";

//redefinir variables con let
nombre2 = "Ana";

//imprimir variables
console.log(nombre2);

{
    let apellido = "Perez";
}

//imprimir variables
console.log(apellido);



//variables con const
const NUMERO_PI = 3.14;

//imprimir constantes
console.log(NUMERO_PI);

// no se puede reasignar una constante
NUMERO_PI = 4;

// esta impresion no se ejecuta porque se produce un error al intentar reasignar una constante
console.log(NUMERO_PI);

/*
imprimir variables con backticks

los backticks permiten incluir variables dentro de una cadena de texto utilizando 
la sintaxis ${variable} y también permiten escribir cadenas de texto en varias líneas 
sin necesidad de usar caracteres especiales. 
*/
let nombre3 = "Carlos";
console.log(`Hola, mi nombre es ${nombre3}`); //imprime "Hola, mi nombre es Carlos" 
console.log(`Hola, mi nombre es ${nombre3}
    
y tengo 25 años`); //imprime "Hola, mi nombre es Carlos y tengo 25 años" en dos lineas