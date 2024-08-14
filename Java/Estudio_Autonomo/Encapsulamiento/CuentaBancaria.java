package Estudio_Autonomo.Encapsulamiento;

public class CuentaBancaria {
    // Atributos privados

    // Atributos privados: titular y saldo están declarados como private, 
    // lo que significa que no pueden ser accedidos directamente desde fuera de la clase CuentaBancaria. 
    // Esto protege los datos de accesos y modificaciones no controladas.
    private String titular;
    private double saldo;

    // Constructor
    public CuentaBancaria(String titular, double saldoInicial) {
        this.titular = titular;
        this.saldo = saldoInicial;
    }

    // Métodos públicos para acceder y modificar los atributos

    // Métodos públicos: Los métodos getTitular(), getSaldo(), depositar(), y retirar() están declarados como public, 
    // lo que permite a los usuarios de la clase acceder a los atributos o modificar su valor de manera controlada. 
    // Estos métodos actúan como una interfaz pública que permite interactuar con el objeto CuentaBancaria.
    public String getTitular() {
        return titular;
    }

    public double getSaldo() {
        return saldo;
    }

    // Validaciones: Los métodos depositar() y retirar() incluyen validaciones 
    // que aseguran que solo se depositen cantidades positivas y que no se retire más dinero del que hay en la cuenta. 
    // Estas validaciones ayudan a mantener la integridad de los datos.
    public void depositar(double cantidad) {
        if (cantidad > 0) {
            saldo += cantidad;
        }
    }

    public void retirar(double cantidad) {
        if (cantidad > 0 && cantidad <= saldo) {
            saldo -= cantidad;
        }
    }
}