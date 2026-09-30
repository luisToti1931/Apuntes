package Relacion2;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Scanner;

public class Ej2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Path carpeta = Path.of("datos", "alumnos.csv");
        int id = 0;
        String[] campos;
        String linea;
        String nombre;
        String grupo;

        boolean encontrado = false;
        
        System.out.println("Introduce el id: ");
        int idUsuario = sc.nextInt();
        sc.nextLine();

        try {
            List<String> alumnos = Files.readAllLines(carpeta, StandardCharsets.UTF_8);

            for (int i = 1; i < alumnos.size(); i++) {
                linea = alumnos.get(i);
                campos = linea.split(";", -1);

                if (campos.length == 3) {
                    id = Integer.parseInt(campos[0]);
                    nombre = campos[1];
                    grupo = campos[2];

                    if (id == idUsuario) {
                        System.out.println(id + ";" + nombre + ";" + grupo);
                        encontrado = true;
                        break;
                    }
                } else {
                    System.out.println("No existe alguno de los campos");
                }
            }
        } catch (IOException e) {
            System.err.println(e.getMessage());
        }
        sc.close();
    }

}
