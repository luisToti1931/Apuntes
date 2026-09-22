package ApuntesProgramación.UD2REL1;

import java.util.ArrayList;

public class ej6 {
    public static void main(String[] args) {
        ArrayList<String> frutas = new ArrayList<>();
        frutas.add("manzana");
        frutas.add("banana");
        frutas.add("naranja");
        frutas.remove(0);
        frutas.add("fresa");

        System.out.print("Array eliminando primer elem. y añadiendo al final: ");
        // para que se ponga automaticamete un separador y al final no se quede el separador
        String mensaje = "";

        for (String fruta : frutas) {
            mensaje += fruta + "-";
        }
        // corta desde donde tu digas hasta donde tu digas
        mensaje = mensaje.substring(0, mensaje.length() - 1);
        System.out.println(mensaje);
    }
}
