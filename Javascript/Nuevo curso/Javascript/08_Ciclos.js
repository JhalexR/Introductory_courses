// Ciclos

// Ciclo while
var cont = 1;
while (cont <= 10) {
  console.log(cont);
  cont++;
}

// ciclo while con break
var cont = 1;
while (cont <= 10) {
  console.log(cont);
  if (cont == 5) {
    break;
  }
  cont++;
}

// ciclo while con continue
var cont = 1;
while (cont <= 10) {
  cont++;
  if (cont == 5) {
    continue;
  }
  console.log(cont);
}

// ciclo do while
var cont = 1;
do {
  console.log(cont);
  cont++;
} while (cont <= 10);

// ciclo for
for (var i = 1; i <= 10; i++) {
  console.log(i);
}

// ciclo for con break
for (var i = 1; i <= 10; i++) {
  console.log(i);
  if (i == 5) {
    break;
  }
}

// ciclo for con continue
for (var i = 1; i <= 10; i++) {
  if (i == 5) {
    continue;
  }
  console.log(i);
}

// ciclo for anidado
for (var i = 1; i <= 3; i++) {
  for (var j = 1; j <= 3; j++) {
    console.log(i + " " + j);
  }
}

// ciclo for in
var persona = {
  nombre: "Juan",
  edad: 30,
  ciudad: "Madrid"
};
for (var propiedad in persona) {
  console.log(propiedad + ": " + persona[propiedad]);
} // se usa para objetos

// ciclo for of
var numeros = [1, 2, 3, 4, 5];
for (var numero of numeros) {
  console.log(numero);
}// se usa para arrays

// iterando un string con for of
var palabra = "Hola";
for (var letra of palabra) {
  console.log(letra);
}

// ciclo forEach
var numeros = [1, 2, 3, 4, 5];
numeros.forEach(function(numero) {
  console.log(numero);
});