package ApuntesProgramación.UD2REL1;

import java.util.ArrayList;

public class ej2 {
    public static void main(String[] args) {
        ArrayList<String> colores = new ArrayList<>();

        colores.add("rojo");
        colores.add("verde");
        colores.add("azul");
        System.out.print("Array de colores: ");
        System.out.print(String.join(" - ", colores));
    }

}
