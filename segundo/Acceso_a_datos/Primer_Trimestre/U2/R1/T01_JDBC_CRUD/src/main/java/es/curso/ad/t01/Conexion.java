package es.curso.ad.t01;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public final class Conexion {
    private static final String URL = "jdbc:mysql://localhost:3307/ad_ud2?connectionTimeZone=UTC";
    private static final String USUARIO = "ad_user";
    private static final String CLAVE = "ad_pass";

    private Conexion() {
    }

    public static Connection abrir() throws SQLException {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
        } catch (ClassNotFoundException e) {
            // TODO: handle exception
            throw new SQLException("No se ha encontrado el driver de MySQL", e);
        }
        return DriverManager.getConnection(URL, USUARIO, CLAVE);
    }
}
