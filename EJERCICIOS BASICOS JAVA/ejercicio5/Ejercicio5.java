
package com.mycompany.ejercicio5;


public class Ejercicio5 {

    public static void main(String[] args) {
        CuentaBancaria cuenta = new CuentaBancaria(1000);
        System.out.println("Saldo inicial: " + cuenta.obtenerSaldo());

        cuenta.depositar(100);
        cuenta.retirar(1200);
    }
}
 

