package Relacion2;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Ej3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Path carpeta = Path.of("datos", "inventario.csv");
        int id = 0;
        String nombre;
        int stockOriginal = 0;
        int idUsuario;
        String[] campos;
        String linea;
        boolean encontrado = false;
        boolean lineaValida = false;

        System.out.println("Introduce id: ");
        idUsuario = sc.nextInt();
        sc.nextLine();

        System.out.println("Introduce nuevo stock: ");
        int nuevoStock = sc.nextInt();
        sc.nextLine();
        try {
            List<String> inventarioOriginal = Files.readAllLines(carpeta, StandardCharsets.UTF_8);
            List<String> inventarioNuevo = new ArrayList<>();
            for (int i = 1; i < inventarioOriginal.size(); i++) {
                linea = inventarioOriginal.get(i);
                campos = linea.split(";", -1);
                lineaValida = false;
                if (campos.length == 3) {
                    id = Integer.parseInt(campos[0]);
                    nombre = campos[1];
                    stockOriginal = Integer.parseInt(campos[2]);

                    if (id == idUsuario) {
                        inventarioNuevo.add(id + ";" + nombre + ";" + stockOriginal);
                        encontrado = true;
                    }
                } else {
                    System.out.println("No existe alguno de los campos");
                }
            }
        } catch (IOException e) {
            System.err.println(e.getMessage());
        }
    }

}
