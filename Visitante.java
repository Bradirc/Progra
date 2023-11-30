
public class Visitante extends Personas {
    public String numeroCarnet;

    public Visitante(String nombre, int edad, String cedula, String numeroCarnet) {
        super(nombre, edad, cedula);
        this.numeroCarnet = numeroCarnet;
    }

    public void comprar() {
        System.out.println("El visitante esta comprando.");
    }
}
    
