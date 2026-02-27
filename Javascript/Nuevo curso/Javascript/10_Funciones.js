//funciones

// las funciones pueden ser tratadas como un valor 

// funciones de forma declarativa
function saludar (nombre){
	console.log('hola soy ${nombre}');
}

// usar función;
saludar('Alex');

function saludar (nombre){
	return 'hola soy ${nombre}'
}

var saludo = saludar('Alex');

comsole.log('saludo');

comsole.log(saludar('Alex'));

// funciones de expresión o anónimas
var suma = function (a, b){ //no se le asigna un nombre
	return a + b;
}

// funciones arrow 
var restar =(a, b) => {
	return a - b;
}

console.log(restar(4, 2));

var multiplicar = (a, b) => a * b; // el return esta implícito 
cosole.log(mutlplicar (2, 2));