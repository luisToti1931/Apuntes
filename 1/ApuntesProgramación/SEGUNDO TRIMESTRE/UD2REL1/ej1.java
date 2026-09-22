package ApuntesProgramación.UD2REL1;
import java.util.ArrayList;
public class ej1 {
    public static void main(String[] args){
        ArrayList<Integer> numeros = new ArrayList<>();
        numeros.add(5);
        numeros.add(10);
        numeros.add(15);
        numeros.add(20);
        System.out.println("Muestro primer y ultimo elemento: ");

        System.out.println("Primer elemento: " + numeros.get(0));
        System.out.println("Ultimo elemento: " + numeros.get(numeros.size()-1));

    }
}
