
package com.mycompany.creacionclase;

public class Creacionclase {

    public static void main(String[] args) {
        
        Asignatura asignatura1 = new Asignatura("Programacion", "1PROG", 1);
        Asignatura asignatura2 = new Asignatura("Lenguaje de marca", "MSI", 1);
        
       asignatura2.setCodigo ("1LM");
       asignatura1.setCurso (2);
       
       System.out.println("La primera asignatura es " + asignatura1.getNombre() + "con codigo" + asignatura2.getCodigo());
       System.out.println("La primera asignatura es " + asignatura2.getNombre() + "con codigo" + asignatura1.getCodigo() + " con curso" + asignatura2.getCurso());
                
    }
}
