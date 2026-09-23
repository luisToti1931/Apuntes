
import java.nio.file.Path;

public class RutasProyecto {
    public static void main(String[] args) {
        Path carpeta = Path.of("datos");
        Path archivo = carpeta.resolve("clubes.txt");
        Path copias = carpeta.resolve("copias");
        try {
            System.out.println("Ruta carpeta: " + carpeta.toAbsolutePath());
            System.out.println("Ruta archivo: " + archivo.toAbsolutePath());
            System.out.println("Ruta copias: " + copias.toAbsolutePath());

        } catch (Exception e) {
            System.err.println(e.getMessage());
        }
    }
}
