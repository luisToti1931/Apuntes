package es.curso.ad.t01;

import java.math.BigDecimal;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import es.curso.ad.t01.Conexion;

public class ClubDao {
    public int insertar(String nombre, String ciudad,
            BigDecimal presupuesto) throws SQLException {
        String sql = "INSERT INTO club(nombre, ciudad, presupuesto) VALUES (?, ?, ?)";
        try (Connection conexion = Conexion.abrir();
                PreparedStatement sentencia = conexion.prepareStatement(
                        sql, Statement.RETURN_GENERATED_KEYS)) {
            sentencia.setString(1, nombre);
            sentencia.setString(2, ciudad);
            sentencia.setBigDecimal(3, presupuesto);
            sentencia.executeUpdate();
            try (ResultSet claves = sentencia.getGeneratedKeys()) {
                if (claves.next()) {
                    return claves.getInt(1);
                }
                throw new SQLException("No se ha generado el ID del club");
            }
        }
    }

    public List<Club> listar() throws SQLException {
        String sql = "SELECT id, nombre, ciudad, presupuesto FROM club ORDER BY id";
        List<Club> clubes = new ArrayList<>();
        try (Connection conexion = Conexion.abrir();
                PreparedStatement sentencia = conexion.prepareStatement(sql);
                ResultSet filas = sentencia.executeQuery()) {
            while (filas.next()) {
                clubes.add(leerClub(filas));
            }
        }
        return clubes;
    }

    public Optional<Club> buscar(int id) throws SQLException {
        String sql = "SELECT id, nombre, ciudad, presupuesto FROM club WHERE id = ?";
        try (Connection conexion = Conexion.abrir();
                PreparedStatement sentencia = conexion.prepareStatement(sql)) {
            sentencia.setInt(1, id);
            try (ResultSet filas = sentencia.executeQuery()) {
                if (filas.next()) {
                    return Optional.of(leerClub(filas));
                }
            }
        }
        return Optional.empty();
    }

    public boolean cambiarCiudad(int id, String ciudad) throws SQLException {
        String sql = "UPDATE club SET ciudad = ? WHERE id = ?";
        try (Connection conexion = Conexion.abrir();
                PreparedStatement sentencia = conexion.prepareStatement(sql)) {
            sentencia.setString(1, ciudad);
            sentencia.setInt(2, id);
            return sentencia.executeUpdate() == 1;
        }
    }

    public boolean borrar(int id) throws SQLException {
        String sql = "DELETE FROM club WHERE id = ?";
        try (Connection conexion = Conexion.abrir();
                PreparedStatement sentencia = conexion.prepareStatement(sql)) {
            sentencia.setInt(1, id);
            return sentencia.executeUpdate() == 1;
        }
    }

    private Club leerClub(ResultSet filas) throws SQLException {
        return new Club(
                filas.getInt("id"),
                filas.getString("nombre"),
                filas.getString("ciudad"),
                filas.getBigDecimal("presupuesto"));
    }

    public List<Club> listarPorCiudad(String ciudad) throws SQLException {
        String sql = " SELECT id, nombre, ciudad, presupuesto FROM club WHERE ciudad = ? ORDER BY ciudad ASC";
        List<Club> clubes = new ArrayList<>();
        try (Connection conexion = Conexion.abrir();
                PreparedStatement sentencia = conexion.prepareStatement(sql)) {
            sentencia.setString(1, ciudad);

            try (ResultSet filas = sentencia.executeQuery()) {
                while (filas.next()) {
                    clubes.add(new Club(
                            filas.getInt("id"),
                            filas.getString("nombre"),
                            filas.getString("ciudad"),
                            filas.getBigDecimal("presupuesto")));
                }
            }
        }
        return clubes;
    }

    public int insertarJugador(String nombre, int dorsal, int clubId) throws SQLException {

        String sql = "INSERT INTO jugador (nombre, dorsal, club_id) VALUES (?, ?, ?)";

        try (Connection conexion = Conexion.abrir();
                PreparedStatement sentencia = conexion.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {

            sentencia.setString(1, nombre);
            sentencia.setInt(2, dorsal);
            sentencia.setInt(3, clubId);

            sentencia.executeUpdate();
            // aqui se recuperan las claves que genera automaticamente mysql
            try (ResultSet claves = sentencia.getGeneratedKeys()) {
                // aqui comprobamos si hay clave generada y si avanza te devuelve el id generado
                if (claves.next()) {
                    return claves.getInt(1);
                }
            }
        }
        // si no hay clave generada te devuelve -1 (no se ha podido recuperar el id)
        return -1;
    }

    public record ResumenClub(int id, String nombre, long totalJugadores) {
    }

    public List<ResumenClub> resumenClubes() throws SQLException {
        String sql = "SELECT c.id, c.nombre, COUNT(j.id) AS totalJugadores"
                + " FROM club c LEFT JOIN jugador j on c.id = j.club_id" + " GROUP BY c.id, c.nombre";

        List<ResumenClub> resumenes = new ArrayList<>();

        try (Connection conexion = Conexion.abrir();
                PreparedStatement sentencia = conexion.prepareStatement(sql);
                ResultSet filas = sentencia.executeQuery()) {
            while (filas.next()) {
                resumenes.add(new ResumenClub(
                        filas.getInt("id"),
                        filas.getString("nombre"),
                        filas.getLong("totalJugadores")));
            }
        }
        return resumenes;
    }
}