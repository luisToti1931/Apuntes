
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class InspectorFichero {
    public static void main(String[] args) {
        Path carpeta = Path.of("datos");
        Path archivo = carpeta.resolve("clubes.txt");

        System.out.println("Ruta absoluta: " + carpeta.toAbsolutePath());

        try {
            if (Files.exists(archivo)) {
                System.out.println("Existe el archivo " + archivo);
                System.out.println("Bytes del archivo: " + Files.size(archivo));

            } else {
                System.out.println("El archivo " + archivo + " no existe");
            }
        } catch (IOException e) {
            System.err.println(e.getMessage());
        }
    }

}
