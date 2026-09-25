
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class PrepararCarpetas {
    public static void main(String[] args) {
        Path carpeta1 = Path.of("datos");
        Path carpeta2 = Path.of("datos/copias");

        Path archivo1 = carpeta1.resolve("clubes.txt");
        Path archivo2 = carpeta2.resolve("respaldo.txt");

        try {
            Files.createDirectories(carpeta1);
            Files.createDirectories(carpeta2);

            if (Files.notExists(archivo1)) {
                Files.createFile(archivo1);
            }

            if (Files.notExists(archivo2)) {
                Files.createFile(archivo2);
            }

            System.out.println("---ARCHIVO1---");
            System.out.println("¿Existe?: " + Files.exists(archivo1));
            System.out.println("Bytes: " + Files.size(archivo1));

            System.out.println();

            System.out.println("---ARCHIVO2---");
            System.out.println("¿Existe?: " + Files.exists(archivo2));
            System.out.println("Bytes: " + Files.size(archivo2));
        } catch (IOException e) {
            System.err.println(e.getMessage());
        }
    }
}
