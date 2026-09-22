package ApuntesProgramación.UD2REL1;

import java.util.ArrayList;

public class ej4 {
    public static void main(String[] args) {
        ArrayList<String> animales = new ArrayList<>();
        animales.add("perro");
        animales.add("gato");
        animales.add(0, "loro");
        animales.add(0,"tortuga");
        System.out.println(animales);
    }
}
