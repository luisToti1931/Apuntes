package ApuntesProgramación.UD2REL1;

import java.util.ArrayList;

public class ej14 {
    public static void main(String[] args) {
        ArrayList<Integer> numeros = new ArrayList<>();
        numeros.add(5);
        numeros.add(10);
        numeros.add(15);
        numeros.add(20);
        
        int primerNumero = numeros.get(0);
        int ultimoNumero = numeros.get(numeros.size() - 1);

        numeros.set(0, ultimoNumero);
        numeros.set((numeros.size() - 1), primerNumero);
        System.out.print("Array de numeros despues del cambio: ");
        String mensaje = "";
        for (Integer numero : numeros) {
            mensaje += numero + "-";
        }
        mensaje = mensaje.substring(0, mensaje.length() - 1);
        System.out.println(mensaje);
    }
}
