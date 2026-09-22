package ApuntesProgramación.UD2REL1;

import java.util.ArrayList;

public class ej8 {
    public static void main(String[] args) {
        ArrayList<Integer> numeros = new ArrayList<>();
        numeros.add(100);
        numeros.add(200);
        numeros.add(300);

        Integer variableTemporal = numeros.get(0);
        numeros.set(0, numeros.get(2));
        numeros.set(2, variableTemporal);

        System.out.print(numeros);
    }
}
