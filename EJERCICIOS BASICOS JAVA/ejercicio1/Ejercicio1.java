
//EJERCICIOS DE CAMBIO DE VARIABLE

package com.mycompany.ejercicio1;

public class Ejercicio1 {

    public static void main(String[] args) {
        
        int num1 = 35;
        int num2 = 20; 
        int aux;
        
        System.out.println("__Antes__");
        System.out.println("Num1: " + num1);
        System.out.println("Num2: " + num2);
        
        aux = num2; 
        num2 = num1;
        num1 = aux;
        
        System.out.println("__Despues__");
        System.out.println("Num1: " + num1);
        System.out.println("Num2: "+ num2);
    }
}
