#include <stdio.h>
#include <conio.h>
#include <iostream>

using namespace std;

//funcion principal main
int main (void){

    //declaracion de variables
    float h=0;
	float s=0;
	int c=0;
	char n_1[15]={'\0'};
	char n_2[15]={'\0'};
	char a_1[15]={'\0'};
	char a_2[15]={'\0'};

    //solictud de informacion al usuario

    cout<<"\nIntroduzca el primer nombre del empleado y presione enter: ";
	scanf("%s",n_1);

    cout<<"\nIntroduzca el segundo nombre del empleado y presione enter: ";
	scanf("%s",n_2);

    cout<<"\nIntroduzca el primer apellido del empleado y presione enter: ";
	scanf("%s",a_1);

    cout<<"\nIntroduzca el primer apellido del empleado y presione enter: ";
	scanf("%s",a_2);

    cout<<"\nIntroduzca el valor de la hora de trabajo y presione enter: ";
	cin>>h;

    cout<<"\nIntroduzca cantidad de horas trabajadas y presione enter: ";
	cin>>c;

    //condicionales para establecer el total del sueldo dependiendo del valor de la hora
    //y de las horas trabajadas

    if(c>0 && c<41){
		s=h*c;
		h=(s*0.012);
		s=s-h;
	}
	else{
		if(c>40 && c<50){
            s=h*40;
			h=(c-40)*(h*2);
			s=s+h;
			h=(s*0.012);
			s=s-h;
		}
		else{
			if(c>50){
	 			s=h*40;
				h=(10*(h*2))+((c-50)*(h*3));
				s=s+h;
				h=(s*0.12);
				s=s-h;
			}
            else
				cout<<"\nERROR cantidad de horas erronea";
		}
	}

    //salida por pantalla del resultado del sueldo del empleado

    cout<<"\n\n\t\tNombre de empleado: "<<n_1<<" "<<n_2<<" "<<a_1<<" "<<a_2;
	cout<<"\n\n\t\tNumero de horas trabajadas: "<<c;
	cout<<"\n\n\t\tSueldo total de empleado despues de recargos e impuesto 12% es $"<<s;

getch();
}


