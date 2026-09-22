package ApuntesProgramación.UD2REL1;

import java.util.ArrayList;

public class ej3 {
    public static void main(String[] args) {
        ArrayList<String> colores = new ArrayList<>();
        colores.add("rojo");
        colores.add("verde");
        colores.add("azul");
        colores.remove(colores.size() - 1);

        System.out.print("Array eliminando el ultimo de la lista: ");
        System.out.print(String.join(" - ", colores));
    }

}
