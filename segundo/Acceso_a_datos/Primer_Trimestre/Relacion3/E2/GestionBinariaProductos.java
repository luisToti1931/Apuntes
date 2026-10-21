package segundo.Acceso_a_datos.Primer_Trimestre.Relacion3.E2;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Scanner;

import segundo.Acceso_a_datos.Primer_Trimestre.Relacion3.E1.Producto;

public class GestionBinariaProductos {
    public static void main(String[] args) {
        Path ruta = Path.of("datos", "productos.dat");
        Scanner sc = new Scanner(System.in);
        if (Files.notExists(ruta)) {
            System.out.println("No hay productos guardados");
            return;
        }
        List<Producto> productos = null;
        try (ObjectInputStream entrada = new ObjectInputStream(Files.newInputStream(ruta))) {
            Object dato = entrada.readObject();
            if (!(dato instanceof List<?> lista)) {
                System.out.println("El archivo no tiene una lista");
                return;
            }

            for (Object elemento : lista) {
                if (!(elemento instanceof Producto)) {
                    System.out.println("Ha habido un error");
                    return;
                }
            }
            productos = (List<Producto>) lista;
        } catch (IOException | ClassNotFoundException e) {
            System.err.println(e.getMessage());
        }
        System.out.println("---- Productos actuales ----");
        for (Producto producto : productos) {
            System.out.println(producto);
        }

        try {
            System.out.println("Introduce el id del producto que quieres modificar: ");
            int idBuscado = sc.nextInt();
            sc.nextLine();

            Producto productoEncontrado = null;

            for (Producto producto : productos) {
                if (producto.getId() == idBuscado) {
                    productoEncontrado = producto;
                    break;
                }
            }

            if (productoEncontrado == null) {
                System.out.println("Error, no existe el id");
                return;
            }

            System.out.println("Introduce el nuevo stock: ");
            int nuevoStock = sc.nextInt();
            sc.nextLine();

            productoEncontrado.setStock(nuevoStock);

            try (ObjectOutputStream salida = new ObjectOutputStream(Files.newOutputStream(ruta))) {
                salida.writeObject(productos);
                System.out.println("Stock modificado correctamente ");
            }
        } catch (IOException e) {
            System.err.println(e.getMessage());
        }
        sc.close();
    }

}
