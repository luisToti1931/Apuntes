package segundo.Acceso_a_datos.Primer_Trimestre.Relacion3.E1;

import java.io.IOException;
import java.io.ObjectOutputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

public class GuardarProductosBinario {
    public static void main(String[] args) {
        Path ruta = Path.of("datos", "productos.dat");

        List<Producto> productos = new ArrayList<>();

        productos.add(new Producto(1, "Ratón Gaming", 29.99, 15));
        productos.add(new Producto(2, "Teclado Mecánico", 79.95, 8));
        productos.add(new Producto(3, "Monitor 24\"", 149.00, 5));
        productos.add(new Producto(4, "Cascos Inalámbricos", 45.50, 12));

        try {
            Files.createDirectories(ruta.getParent());
            try (ObjectOutputStream salida = new ObjectOutputStream(Files.newOutputStream(ruta))) {
                salida.writeObject(productos);
                System.out.println("Lista guardada correctamente en binario");
            }
            if (Files.exists(ruta) && Files.size(ruta) > 0) {
                System.out.println("El archivo exixste y su tamaño es mayor a 0 bytes");
            }
        } catch (IOException e) {
            System.err.println(e.getMessage());
        }
    }
}