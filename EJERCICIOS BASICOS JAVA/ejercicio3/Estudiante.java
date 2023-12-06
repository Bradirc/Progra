
package com.mycompany.ejercicio3;

public class Estudiante {
    // Atributos
    String nombre;
    int edad;
    double promedio;

    // Constructor
    Estudiante(String nombre, int edad, double promedio) {
        this.nombre = nombre;
        this.edad = edad;
        this.promedio = promedio;
    }

    // Método para mostrar información del estudiante
    void mostrarInformacion() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Edad: " + edad + " años");
        System.out.println("Promedio: " + promedio);
    }

    // Método para determinar si el estudiante aprueba o no
    void determinarAprobacion() {
        if (promedio >= 6.0) {
            System.out.println(nombre + " ha aprobado.");
        } else {
            System.out.println(nombre + " no ha aprobado.");
        }
    }
}


