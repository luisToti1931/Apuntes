package ApuntesProgramación.UD2REL1;

import java.util.ArrayList;

public class ej12 {
    public static void main(String[] args) {
        ArrayList<String> nombres = new ArrayList<>();
        nombres.add("Carlos");
        nombres.add("Ana");
        nombres.add("Pedro");
        nombres.add("Laura");
        //elimino primer nombre
        String primerNombre = nombres.remove(0);
        System.out.println("Primer valor eliminado: " + primerNombre);
        // elimino ultimo nombre
        String ultimoNombre = nombres.remove(nombres.size() - 1);
        System.out.println("Ultimo nombre eliminado: " + ultimoNombre);
        // muestro array de lo resultante 
        System.out.print("Array de nombres: ");
        String mensaje = "";
        for (String nombre : nombres) {
            mensaje += nombre + "-";
        }
        mensaje = mensaje.substring(0, mensaje.length() - 1);
        System.out.println(mensaje);

    }
}
