// ejercicios con ciclos

// tabla de multiplicar del 1 al 12 con formato
for (var i = 1; i <= 12; i++) 
    for (var j = 1; j <= 10; j++) 
        console.log(i + " x " + j + " = " + (i*j));

// tabla de multiplicar del 1 al 12 con formato usando while
var mult = 1
while (mult <= 12) {
  var multi = 1;
  while (multi <= 10) {
    console.log(mult + ' x ' + multi + ' = ' + mult*multi);
    multi++;
  }
  mult++;
}

// tabla de multiplicar del 1 al 12 con formato usando do while
var mult = 1;
do {
	var multi = 1;
	do {
		console.log(mult + ' x ' + multi + ' = ' + mult*multi);
        multi++;
	} while (multi <= 10);
    mult++;
} while (mult <= 12);