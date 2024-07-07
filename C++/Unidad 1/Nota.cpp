#include <stdio.h>
#include <conio.h>
#include <iostream>

using namespace std;

//funciona principal main
int main (void){

	//declaracion de variables
    int x=0;
	int y=0;
	int z=0;

	//solictud de datos al usuario
	cout<<"\nIntroduzca la primera nota y presione enter: ";
	cin>> x;

	cout<<"\nIntroduzca la segunda nota y presione enter: ";
	cin>> y;

	cout<<"\nIntroduzca la tercera nota y presione enter: ";
	cin>> z;

	//condicionales donde se calcula cual es la nota mas alta
	if (x>y) {
		if(x>z)
			cout<<"\nla nota mayor es la primera: "<<x;
		else
			cout<<"\nla nota mayor es la tercera: "<<z;
	}
	else{
		if(y>z)
			cout<<"\nla nota mayor es la segunda: "<<y;
		else
			cout<<"\nla nota mayor es la tercera: "<<z;
	}
	getch();
}