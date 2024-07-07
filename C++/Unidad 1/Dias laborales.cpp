#include <stdio.h>
#include <conio.h>
#include <iostream>

using namespace std;

//funcion principal main
int main (void){

	//declaracion de variables
	int m=0;
	int i=0;
	int a=0;
	int h=0;
	
	//solicitud de datos del usuario
    cout<<"\nIntroduzca el año (formato aaaa) y presione enter: ";
	cin>>a;

    cout<<"\nIntroduzca el numero del dia de la semana del primer dia del mes: ";
	cout<<"\nLunes     1";
	cout<<"\nMartes    2";
	cout<<"\nMiercoles 3";
	cout<<"\nJueves    4";
	cout<<"\nViernes   5";
	cout<<"\nSabado    6";
	cout<<"\nDomingo   7";
	cin>>i;

//condicionales anidadas para conocer los dias habiles del mes segun los datos ingresados 
if (a>0){
		if(m>0 && m<13){
				if(i>0 && i<8){
					if(m!=2){
						if(m==1 || m==3 || m==5 || m==7 || m==8 || m==10 || m==12){
							if(i<5){
								cout<<"\nlos dias habiles del mes son 27";
								getch();
								}
							else {
								cout<<"\nlos dias habiles del mes son 28";
								getch();
								}
							}
						else{
							if(i<4){
								cout<<"\nlos dias habiles del mes son 27";
								getch();
								}
							else {
								cout<<"\nlos dias habiles del mes son 28";
								getch();
								}
							}
						}
					else{
						if(a%4==0 && a%100!=0 && a%400!=0)
							if(i==7){
								cout<<"\n año bisiesto numero de dias habiles del mes 24";
								getch();
								}
							else {
								cout<<"\n año bisiesto numero de dias habiles del mes 25";
								getch();
								}
						else {
							cout<<"\n año no es bisiesto numero de dias habiles del mes 25";
							getch();
							}

					}

				}
			else
				cout<<"\nERROR dia no es valido";
			}
		else
			cout<<"\nERROR mes no es valido";

		}
	else
		cout<<"\nERROR año no es valido";
getch();
}