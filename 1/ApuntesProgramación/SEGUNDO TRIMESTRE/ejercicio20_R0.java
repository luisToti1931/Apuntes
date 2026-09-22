import java.util.Scanner;

public class ejercicio20_R0 {

    public static int contarPalabrasEnCadena(String cadena) {
        String[] palabrasSeparadas = cadena.split(" ");
        int numeroDePalabras = palabrasSeparadas.length;
        return numeroDePalabras;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Introduzca una frase: ");
        String cadenaDePalabras = scanner.nextLine();
        int numeroDePalabras = contarPalabrasEnCadena(cadenaDePalabras);

        System.out.println("La frase " + cadenaDePalabras + " tiene " + numeroDePalabras + " palabras");
        scanner.close();

    }
}
