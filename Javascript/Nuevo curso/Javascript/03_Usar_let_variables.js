/*
declarar variables con let
“let se usa para declarar variables de manera local a un bloque de código”
Un bloque es cualquier sección entre llaves { }, como en un if, for, while, o una función.
Cuando declaras una variable con let, solo existe dentro de ese bloque.
Ejemplo: */

if (true) {
  let mensaje = "Hola";
  console.log(mensaje); // ✅ Funciona
}

console.log(mensaje); // ❌ Error: mensaje is not defined
/*
Aquí mensaje solo vive dentro del if.
Esto es diferente a var, que tiene alcance de función, no de bloque.
*/
 
/*
“let se puede reasignar”
Significa que puedes cambiar el valor de la variable después de declararla.
*/

let contador = 1;
contador = 2; // permitido
console.log(contador); // 2

// No hay problema en modificar su valor.
/*
“pero no se puede redeclarar dentro del mismo bloque”
No puedes declarar otra vez la misma variable con let en el mismo bloque.
*/
let edad = 20;
// let edad = 25; // ❌ Error: Identifier 'edad' has already been declared

// Sin embargo, sí puedes usar el mismo nombre en bloques distintos:
let numero = 10;

if (true) {
  let numero = 20; // permitido (bloque diferente)
  console.log(numero); // 20
}

console.log(numero); // 10
//Cada bloque tiene su propio alcance.
// Ejemplo clásico con var (problema):

for (var i = 0; i < 3; i++) {
  setTimeout(() => {
    console.log(i);
  }, 100);
}
/*
Resultado:
3
3
3
*/

// Ahora con let:
for (let i = 0; i < 3; i++) {
  setTimeout(() => {
    console.log(i);
  }, 100);
}
/*
Resultado 
0
1
2
*/
