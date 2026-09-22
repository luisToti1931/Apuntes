package ApuntesProgramación.UD2REL1;

import java.util.ArrayList;

public class ej11 {
    public static void main(String[] args) {
        ArrayList<String> nombres = new ArrayList<>();
        nombres.add("Ana");
        nombres.add("Pedro");
        nombres.add(nombres.size(), "Laura");
        nombres.add(0, "Carlos");
        System.out.print("Array de nombres: ");
        String mensaje = "";
        for (String nombre : nombres) {
            mensaje += nombre + "-";
        }
        mensaje = mensaje.substring(0, mensaje.length()-1);
        System.out.println(mensaje);
    }
}
