package ApuntesProgramación.UD2REL1;

import java.util.ArrayList;

public class ej13 {
    public static void main(String[] args) {
        ArrayList<String> letras = new ArrayList<>();
        letras.add("a");
        letras.add("b");
        letras.add("c");
        letras.add("d");

        ArrayList<String> invertido = new ArrayList<>();

        for (int i = 0; i < letras.size(); i++) {
            invertido.add(letras.get(letras.size() - 1 - i));
        }
        System.out.println(invertido);
    }

}
