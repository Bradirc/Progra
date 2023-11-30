public class perro {
    String raza, nombre;
    int edad;
    public perro(String raza,String nombre, int edad){
        this.raza=raza;
        this.nombre=nombre;
        this.edad=edad;
    }
     //metodo
     public void dormir(){
        System.out.println(this.raza + this.nombre +" Empezo a dormir");

    }
    public void come(){
        System.out.println(this.raza + this.nombre +" Empezo a comer");
    }

    public static void main(String[] args) {
        perro p1 =new perro("Golden"," juan",2);//instancia=dar vida
        p1.come();
        p1.dormir();
    }

}