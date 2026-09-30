package Relacion2;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class Ej1 {
    public static void main(String[] args) {
        Path ruta = Path.of("datos", "videojuegos.csv");
        int id;

        try {
            List<String> videojuegos = Files.readAllLines(ruta, StandardCharsets.UTF_8);
            for (int i = 1; i < videojuegos.size(); i++) {
                String linea = videojuegos.get(i);
                String[] campos = linea.split(";", -1);

                if (campos.length == 3) {
                    try {
                        id = Integer.parseInt(campos[0]);
                        String titulo = campos[1];
                        String plataforma = campos[2];

                        System.out.println("[" + id + "] " + titulo + " - " + plataforma);

                    } catch (NumberFormatException e) {
                        System.err.println(e.getMessage());
                    }
                } else {
                    System.out.println("No tiene los campos suficientes");
                }
            }

        } catch (IOException e) {
            System.err.println(e.getMessage());
        }

    }

}
