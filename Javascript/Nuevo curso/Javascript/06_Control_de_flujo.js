/*
control de flujo
*/

// condicionales

// estructura if 
var llueve = false;
if(llueve){
	console.log('necesito una sombrilla'); // no se imprime
}

llueve = true;
if(llueve){
	console.log('necesito una sombrilla'); // si se imprime
}

// estructura else
const MAYORIA_DE_EDAD = 18;
var edadPersona =12;

if(edadPersona >= MAYORIA_DE_EDAD){
	console.log('es mayor de edad');
}
else {
	console.log('es menor de edad');
}

// estructura else if
var semaforo = 'rojo';
if(semaforo === 'verde'){
	console.log('Seguir');
} else if(semaforo === 'amarillo') {
	console.log('Prepararse');
} else if (semaforo === 'rojo'){
	console.log('Detenerse');
}
  else {
	console.log('color no identificado');
}


// switch
let producto ='mango';
switch(producto){
	case 'papaya':
		console.log('papaya 1 USD');
	break;
	case 'naranja':
		console.log('naranaja 1 USD');
	break;
	case 'mango':
	case 'piña': 
		console.log('piñas y mangos 1 USD'); // como no hay break se imprime este mensaje
	break;
	default:
		console.log('producto no existe');
}