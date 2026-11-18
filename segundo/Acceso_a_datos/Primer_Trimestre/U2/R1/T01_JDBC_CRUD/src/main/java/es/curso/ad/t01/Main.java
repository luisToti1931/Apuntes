package es.curso.ad.t01;

import java.math.BigDecimal;
import java.sql.SQLException;

import es.curso.ad.t01.ClubDao.ResumenClub;

public class Main {
    public static void main(String[] args) {
        ClubDao dao = new ClubDao();
        try {
            System.out.println("CLUBES INICIALES");
            for (Club club : dao.listar()) {
                System.out.println(club);
            }
            System.out.println("\nCLUBES DE GRANADA");
            for (Club club : dao.listarPorCiudad("Granada")) {
                System.out.println(club);
            }
            System.out.println("\nINSERTAR JUGADOR");

            int idJugador = dao.insertarJugador("Jorge Pascual", 91, 1);

            System.out.println("Jugador creado con id: " + idJugador);

            System.out.println("\nRESUMEN DE CLUBES");

            for(ResumenClub resumen : dao.resumenClubes()){
                System.out.println(resumen);
            }

            String nombreTemporal = "Club de prueba JDBC";
            int id = dao.insertar(nombreTemporal, "Granada", new BigDecimal("120.50"));
            System.out.println("Creado con ID " + id);
            System.out.println("Buscado: " + dao.buscar(id).orElseThrow());
            System.out.println("Actualizado: " + dao.cambiarCiudad(id, "Jaén"));
            System.out.println("Tras cambiar: " + dao.buscar(id).orElseThrow());
            System.out.println("Borrado: " + dao.borrar(id));
            System.out.println("¿Sigue existiendo? " + dao.buscar(id).isPresent());
        } catch (SQLException e) {
            System.err.println("Error de base de datos: " + e.getMessage());
        }
    }
}
