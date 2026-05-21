/* 
manipulacion de arreglos
*/

//declaracion de un arreglo
var letras = ['a', 'b', 'c', 'd', 'e'];

//funcion length
console.log(letras.length);

//for tradicional
for(let i = 0; i < letras.length; i++){
    const element = letras[i];
    console.log(element);
}

//for each
letras.forEach((elemento) => {
    console.log(elemento);
});