/*Tipos de datos*/

/* datos valor numerico*/
console.log(27);
console.log(27.56); //punto flotante

/* datos texto */
("Texto a escribir"); //escribir texto entre comillas
("Texto a escribir"); //tambien se pueden usar comillas simples
`Texto a escribir`; //tambien se pueden usar backticks

/*imprimir texto en consola*/
console.log("Texto a escribir"); //imprime el texto en la consola
console.log("Texto a escribir"); //imprime el texto en la consola
console.log(`Texto a escribir`); //imprime el texto en la consola

/* datos booleanos */
console.log(true); //imprime el valor verdadero
console.log(false); //imprime el valor falso

/* datos nulos */
console.log(null); //imprime el valor nulo

/* datos indefinidos */
console.log(undefined); //imprime el valor indefinido

/* datos estructurales tienen 
varios tipos de datos dentro 
de una estructura */

/* datos objetos */
console.log({ nombre: "Juan", edad: 30 }); //imprime un objeto con propiedades nombre y edad

/* ejemplos mas detallados */
//imprime un objeto con propiedades nombre, edad y direccion, donde direccion es otro objeto con propiedades calle y numero
console.log({
  nombre: "Juan",
  edad: 30,
  direccion: { calle: "Calle Falsa", numero: 123 },
  fechaDeNacimiento: new Date(),
});

/* objetos dentro de objetos */
console.log({
  nombre: "Juan",
  edad: 30,
  direccion: {
    calle: "Calle Falsa",
    numero: 123,
    ciudad: { nombre: "Ciudad Falsa", pais: "Pais Falso" },
  },
});

/* objetos vacios */
console.log({}); //imprime un objeto vacio

/* datos arreglos */
console.log([1, 2, 3, 4, 5]); //imprime un arreglo con los numeros del 1 al 5

console.log(["Mexico", "Venezuela", "Ecuador"]); //imprime un arreglo con los nombres de tres paises

console.log([21, true, { nombre: "Juan" }, [1, 2, 3]]); //imprime un arreglo con diferentes tipos de datos

console.log([]); //imprime un arreglo vacio

/* datos simbolicos */
console.log(Symbol("simbolo")); //imprime un simbolo unico

/* datos funciones */
console.log(function () {
  return "Hola";
}); //imprime una funcion que devuelve el texto "Hola"

/* datos fecha */
console.log(new Date()); //imprime la fecha actual

/* datos expresiones regulares */
console.log(/abc/); //imprime una expresion regular que busca la cadena "abc"

/* datos mapas */
console.log(new Map()); //imprime un mapa vacio

/* datos conjuntos */
console.log(new Set()); //imprime un conjunto vacio

/* datos errores */
console.log(new Error()); //imprime un error

/* datos promesas */
console.log(new Promise((resolve, reject) => {})); //imprime una promesa vacia
