
package com.mycompany.ejercicio5;

class CuentaBancaria {
    private double saldo;

    // Constructor
    CuentaBancaria(double saldoInicial) {
        this.saldo = saldoInicial;
    }

    // Método para realizar un depósito
    void depositar(double monto) {
        if (monto > 0) {
            saldo += monto;
            System.out.println("Depósito realizado. Nuevo saldo: " + saldo);
        } else {
            System.out.println("El monto del depósito debe ser mayor que cero.");
        }
    }

    // Método para realizar un retiro
    void retirar(double monto) {
        if (monto > 0 && monto <= saldo) {
            saldo -= monto;
            System.out.println("Retiro realizado. Nuevo saldo: " + saldo);
        } else {
            System.out.println("Monto de retiro inválido o saldo insuficiente.");
        }
    }

    // Método para obtener el saldo actual
    double obtenerSaldo() {
        return saldo;
    }
}

