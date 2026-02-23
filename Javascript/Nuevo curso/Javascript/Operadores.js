/* operadores */

// operador de asignacion 
let a = 1;
var b = 2;

// operador de asignacion de adicion
a += 3; // a = a + 3; => a = 4
a += b; // a = a + b; => a = 6

// operador de asignacion de resta
a -= 3; // a = a - 3; => a = 3
a -= b; // a = a - b; => a = 2

// operador de asignacion de multiplicacion
a *= 2; // a = a * 2; => a = 4
a *= b; // a = a * b; => a = 8

// operador de asignacion de division
a /= 2; // a = a / 2; => a = 4  
a /= b; // a = a / b; => a = 2

// operador de asignacion de modulo
a %= 2; // a = a % 2; => a = 0 
a %= b; // a = a % b; => a = 0


// operadores de comparacion
console.log(a == b); // false
console.log(a != b); // true
console.log(a > b); // false
console.log(a < b); // true
console.log(a >= b); // false
console.log(a <= b); // true   

// operadores logicos
console.log(a > 0 && b > 0); // true
console.log(a > 0 || b < 0);    // true
console.log(!(a > 0));           // false  

// operadores de incremento y decremento
a++; // a = a + 1; => a = 1
a--; // a = a - 1; => a = 0 
++a; // a = a + 1; => a = 1
--a; // a = a - 1; => a = 0

// operadores de igualdad estricta
console.log(a === b); // false
console.log(a !== b); // true
console.log(3 === '3'); // false (tipos diferentes)

// operadores de desigualdad estricta
console.log(3 !== '3'); // true (tipos diferentes)

// operadores de igualdad
console.log(a == b); // false
console.log(a != b); // true

// operadores de tipo
console.log(typeof a); // number
console.log(typeof b); // number

// operadores de concatenacion
let str1 = "Hola";
let str2 = "Mundo";
console.log(str1 + " " + str2); // Hola Mundo

// operadores de exponenciacion
a = 2;
console.log(a ** 3); // 8 (2 elevado a la potencia de 3)

// operadores de division entera
console.log(Math.floor(a / 2)); // 1 (división entera de a entre 2)

// operadores de resto
console.log(a % 2); // 0 (resto de a dividido entre 2)

// operadores de asignacion de exponenciacion
a **= 3; // a = a ** 3; => a = 8