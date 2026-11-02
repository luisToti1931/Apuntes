package segundo.Acceso_a_datos.Primer_Trimestre.Relacion4.ej1;

import java.io.IOException;
import java.nio.file.Path;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Path archivo = Path.of("datos", "inscripciones.csv");
        try (Scanner teclado = new Scanner(System.in)) {
            int opcion = -1;
            while (opcion != 0) {
                System.out.println("\nGESTOR DE INSCRIPCIONES");
                System.out.println("1. Listar | 2. Buscar | 3. Alta | 4. Cambiar plazas");
                System.out.println("5. Eliminar | 6. Restaurar última copia | 0. Salir");
                System.out.print("Opción: ");
                try {
                    opcion = Integer.parseInt(teclado.nextLine().trim());
                    switch (opcion) {
                        case 1 -> {
                            // EJEMPLO COMPLETO: lectura y salida solo desde main.
                            List<Inscripcion> lista = GestorInscripciones.cargar(archivo);
                            if (lista.isEmpty()) {
                                System.out.println("No hay inscripciones.");
                            }
                            for (Inscripcion item : lista) {
                                System.out.println(item);
                            }
                        }
                        case 2 -> {
                            // EJEMPLO COMPLETO: consulta sin modificar el archivo.
                            System.out.print("ID que buscas: ");
                            int id = Integer.parseInt(teclado.nextLine().trim());
                            Inscripcion encontrada = GestorInscripciones.buscar(
                                    GestorInscripciones.cargar(archivo), id);
                            System.out.println(encontrada == null ? "ID no encontrado." : encontrada);
                        }
                        case 3 -> {
                            // EJEMPLO COMPLETO: alta y validación por la capa de datos.
                            System.out.print("ID: ");
                            int id = Integer.parseInt(teclado.nextLine().trim());
                            System.out.print("Persona: ");
                            String persona = teclado.nextLine().trim();
                            System.out.print("Taller: ");
                            String taller = teclado.nextLine().trim();
                            System.out.print("Plazas: ");
                            int plazas = Integer.parseInt(teclado.nextLine().trim());
                            boolean alta = GestorInscripciones.registrar(
                                    archivo, new Inscripcion(id, persona, taller, plazas));
                            System.out.println(alta ? "Inscripción añadida." : "Datos incorrectos o ID repetido.");
                        }
                        case 4 -> {
                            // TODO 1.6-A - Pedir ID y nuevas plazas, llamar a actualizarPlazas
                            // y mostrar un mensaje distinto según el boolean recibido.
                            // Solicita ID, plazas y muestra el resultado.
                            System.out.println("Introduce el ID de la inscripción a actualizar: ");
                            int id = Integer.parseInt(teclado.nextLine());
                            System.out.print("Introduce las nuevas plazas: ");
                            int plazas = Integer.parseInt(teclado.nextLine());

                            try {
                                boolean actualizado = GestorInscripciones.actualizarPlazas(archivo, id, plazas);

                                if (actualizado) {
                                    System.out.println("Plazas actualizadas correctamente");
                                } else {
                                    System.out.println("Error");
                                }
                            } catch (IOException e) {
                                // TODO: handle exception
                                System.out.println("Error al actualizar el archivo: " + e.getMessage());
                            }
                        }
                        case 5 -> {
                            // TODO 1.6-B - Pedir ID, eliminar y mostrar el resultado.
                            // Solicita ID para eliminar y muestra el resultado.
                            System.out.print("Introduce el ID de la inscripción que deseas eliminar: ");
                            int id = Integer.parseInt(teclado.nextLine());

                            try {
                                boolean eliminado = GestorInscripciones.eliminar(archivo, id);
                                if (eliminado) {
                                    System.out.println("¡Inscripción eliminada correctamente!");
                                } else {
                                    System.out.println("No se pudo eliminar (el ID no existe en el archivo).");
                                }
                            } catch (IOException e) {
                                System.out.println("Error al procesar el archivo: " + e.getMessage());
                            }
                        }
                        case 6 -> {
                            // TODO 1.6-C - Pedir confirmación S/N antes de restaurar.
                            // Pide confirmación antes de llamar a restaurar.
                            System.out.print(
                                    "¿Estás seguro de que deseas restaurar el archivo desde la copia de seguridad (.bak)? (S/N): ");
                            String confirmacion = teclado.nextLine().trim();

                            if (confirmacion.equalsIgnoreCase("S")) {
                                try {
                                    boolean restaurado = GestorInscripciones.restaurar(archivo);
                                    if (restaurado) {
                                        System.out
                                                .println("¡Archivo restaurado con éxito desde la copia de seguridad!");
                                    } else {
                                        System.out.println(
                                                "No se pudo restaurar: no se encuentra ninguna copia de seguridad (.bak).");
                                    }
                                } catch (IOException e) {
                                    System.out.println("Error al restaurar el archivo: " + e.getMessage());
                                }
                            } else {
                                System.out.println("Operación de restauración cancelada.");
                            }
                        }
                        case 0 -> System.out.println("Hasta luego.");
                        default -> System.out.println("Opción desconocida.");
                    }
                } catch (NumberFormatException e) {
                    System.out.println("Introduce un número entero válido.");
                } catch (IOException e) {
                    System.out.println("Error de archivo: " + e.getMessage());
                }
            }
        }
    }
}