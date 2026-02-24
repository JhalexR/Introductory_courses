//ejercicios condicionales

// traducir a ingles dia de la semana if else
var day = 'Miercoles';
if (day == 'Lunes') {
  console.log('Monday');
}else if (day == 'Martes') {
  console.log('Tuesday');
}else if (day == 'Miercoles') {
  console.log('Wednesday');
}else if (day == 'Jueves') {
  console.log('Thursday');
}else if (day == 'Viernes') {
  console.log('Friday');
}else if (day == 'Sabado') {
  console.log('Saturday');
}else if (day == 'Domingo') {
  console.log('Sunday');
} else {
  console.log('Dia no valido');
}

// traducir a ingles dia de la semana switch case
switch (day) {
  case 'Lunes':
    console.log('Monday');
    break;  
  case 'Martes':
    console.log('Tuesday');
    break;  
  case 'Miercoles':
    console.log('Wednesday');
    break;  
  case 'Jueves':
    console.log('Thursday');
    break;  
  case 'Viernes':
    console.log('Friday');
    break;  
  case 'Sabado':
    console.log('Saturday');        
    break;  
  case 'Domingo':
    console.log('Sunday');
    break;  
  default:
    console.log('Dia no valido');
}

// ejercicio según el total de la compra, se agregue un valor de envio if else
var valor = 15;

if (valor <= 10) {
    console.log('Se agrega valor de envio de 3');
} else if (valor <= 20 ) {
    console.log('Se agrega valor de envio de 5');
} else if (valor <= 50) {
    console.log('Se agrega valor de envio de 7');
} else {
    console.log('Se agrega valor de envio de 10');
}

// ejercicio según el total de la compra, se agregue un valor de envio switch case
switch (valor) {
  case valor <= 10:
    console.log('Se agrega valor de envio de 3');
    break;
    case valor <= 20:
    console.log('Se agrega valor de envio de 5');
    break;
    case valor <= 50:
    console.log('Se agrega valor de envio de 7');
    break;
    default:
    console.log('Se agrega valor de envio de 10');
}

// ejercicio según el total de la compra, se agregue un valor de envio switch case con true
switch (true) { 
  case valor <= 10:
    console.log('Se agrega valor de envio de 3');
    break;
  case valor <= 20:
    console.log('Se agrega valor de envio de 5');
    break;
  case valor <= 50:
    console.log('Se agrega valor de envio de 7');
    break;
  default:
    console.log('Se agrega valor de envio de 10');
}