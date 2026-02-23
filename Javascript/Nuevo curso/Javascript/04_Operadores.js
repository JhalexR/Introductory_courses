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

// operadores de bit a bit
console.log(a & b); // 0 (AND bit a bit)
console.log(a | b); // 2 (OR bit a bit)
console.log(a ^ b); // 2 (XOR bit a bit)
console.log(~a); // -2 (NOT bit a bit)
console.log(a << 1); // 2 (desplazamiento a la izquierda)

// operadores de desplazamiento a la derecha
console.log(a >> 1); // 0 (desplazamiento a la derecha con signo)
console.log(a >>> 1); // 0 (desplazamiento a la derecha sin signo)  

// operadores de asignacion de bit a bit    
a &= b; // a = a & b; => a = 0
a |= b; // a = a | b; => a = 2
a ^= b; // a = a ^ b; => a = 2
a <<= 1; // a = a << 1; => a = 2

// operadores de asignacion de desplazamiento a la derecha
a >>= 1; // a = a >> 1; => a = 0
a >>>= 1; // a = a >>> 1; => a = 0

// operadores ternarios
let edad = 18;
let mensaje = (edad >= 18) ? "Eres mayor de edad" : "Eres menor de edad";
console.log(mensaje); // Eres mayor de edad

// operadores de incremento y decremento
a++; // a = a + 1; => a = 1
a--; // a = a - 1; => a = 0 
++a; // a = a + 1; => a = 1
--a; // a = a - 1; => a = 0

// operadores de incremento y decremento en expresiones
a = 1;
console.log(a++); // 1 (primero se devuelve el valor de a, luego se incrementa a)
console.log(++a); // 3 (primero se incrementa a, luego se devuelve el valor de a)
console.log(a--); // 3 (primero se devuelve el valor de a, luego se decrementa a)
console.log(--a); // 1 (primero se decrementa a, luego se devuelve el valor de a)

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
console.log(typeof 'variable'); // string
console.log(typeof true); // boolean
console.log(typeof null); // object
console.log(typeof undefined); // undefined
console.log(typeof {}); // object
console.log(typeof []); // object
console.log(typeof function () {}); // function
console.log(typeof new Date()); // object

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

// operador de destructuracion
var ubicacion = { pais: "Mexico", capital: "CDMX" };
var { pais } = ubicacion; // se extrae la propiedad pais del objeto ubicacion 
console.log(pais); // Mexico

// operador de destructuracion con alias
var ubicacion = { pais: "Mexico", capital: "CDMX" };
var { pais:nacion } = ubicacion; // se extrae la propiedad pais del objeto ubicacion y se asigna a la variable nacion
console.log(nacion); // Mexico
console.log(pais); // ReferenceError: pais is not defined (pais no existe como variable independiente)

// operador de destructuracion con valores por defecto
var ubicacion = { pais: "Mexico" };
var { capital = "CDMX" } = ubicacion; // se extrae la propiedad capital del objeto ubicacion y se asigna a la variable capital, si no existe se asigna el valor por defecto "CDMX"
console.log(capital); // CDMX

// operador de desestructuración de arreglos
var arreglo = [1,2,3,4];
var [x,p,f] = arreglo; // desestructura por orden
console.log(x); // imprime la posición 1
console.log(f); // imprime la posición 3

// operador de miembro o de acceso de propiedad
// notación punto
var moneda = {
	local: 'peso',
	extranjera: 'euro'
}
console.log(moneda.peso);
console.log(moneda.extranjera);

// notación por corchetes
var moneda = {
	local: 'peso',
	extranjera: 'euro'
}
console.log(moneda['peso']);

// notación por corchetes en arreglos
var arreglo2 = [21,22,23,24,25,26]
// se accede por el numero de posición teniendo en cuenta la posición 0
console.log(arreglo2[3]); // imprime 24