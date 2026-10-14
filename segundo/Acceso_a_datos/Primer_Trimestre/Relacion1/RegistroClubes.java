import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.util.Scanner;

public class RegistroClubes {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Path carpeta = Path.of("datos", "clubes.txt");
        int id = 0;
        String nombre;
        String ciudad;

        while (id != -1) {
            try {
                System.out.println("Introduce un id: ");
                id = sc.nextInt();
                sc.nextLine();

                if (id == -1) {
                    break;
                }
                System.out.println("Introduce un nombre: ");
                nombre = sc.nextLine();
                System.out.println("Introduce una ciudad: ");
                ciudad = sc.nextLine();

                Files.createDirectories(carpeta.getParent());
                try (BufferedWriter salida = Files.newBufferedWriter(carpeta, StandardCharsets.UTF_8,
                        StandardOpenOption.CREATE, StandardOpenOption.APPEND)) {
                    salida.write(id + ";" + nombre + ";" + ciudad);
                    salida.newLine();
                }

            } catch (IOException e) {
                System.err.println(e.getMessage());
            }

            try (BufferedReader entrada = Files.newBufferedReader(
                    carpeta, StandardCharsets.UTF_8)) {
                String linea;
                while ((linea = entrada.readLine()) != null) {
                    System.out.println(linea);
                }
            } catch (IOException e) {
                System.err.println("No se pudo leer: " + e.getMessage());
            }

        }
    }
}
