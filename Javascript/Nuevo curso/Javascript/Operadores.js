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