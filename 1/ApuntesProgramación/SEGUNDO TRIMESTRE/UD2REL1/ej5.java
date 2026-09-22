package ApuntesProgramación.UD2REL1;

import java.util.ArrayList;

public class ej5 {
    public static void main(String[] args) {
        ArrayList<String> animales = new ArrayList<>();
        animales.add("perro");
        animales.add("gato");
        animales.add(0, "loro");
        animales.add(1, "tortuga");
        animales.remove(0);

        System.out.println("Array animales sin el primer elemento: ");
        System.out.print(String.join(" - ", animales));
    }
}
