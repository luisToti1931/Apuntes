package segundo.Acceso_a_datos.Primer_Trimestre.Relacion4.ej2;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.XMLConstants;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import org.w3c.dom.Document;
import org.w3c.dom.Element;

public class RepositorioEquipos {
    // TODO 2.1 - Recuperar la lista serializada con ObjectInputStream.
    // Si no existe el .dat, devolver lista vacía. Comprobar tipos, IDs y
    // duplicados.
    public static List<Equipo> cargar(Path archivo) throws IOException {
        // PASO 1: si el fichero falta, devuelve una lista vacía.
        // Si existe, lee un Object y valida su contenido.
        List<Equipo> lista = new ArrayList<>();

        if (!Files.exists(archivo)) {
            return lista;
        }

        try(ObjectInputStream entrada = new ObjectInputStream(new FileInputStream(archivo.toFile()))) {
            Object leido = entrada.readObject();
            if (!(leido instanceof List)) {
                throw new IOException("El fichero no contiene una lista");
            }
            for(Object objeto : (List<?>) leido){
                if (!(objeto instanceof Equipo)) {
                    throw new IOException("Hay un elemento que no es Equipo");
                }

                Equipo equipo = (Equipo) objeto;
                if (equipo.getId() <= 0) {
                    throw new IOException("ID no válido: " + equipo.getId());
                }
                if (buscar(lista, equipo.getId()) != null) {
                    throw new IOException("ID duplicado: " + equipo.getId());
                }
                lista.add(equipo);
            }
        } catch (ClassNotFoundException e) {
            // TODO: handle exception
            throw new IOException("Error al leer el fichero", e);
        }
        return lista;
    }

    // TODO 2.2 - Crear carpeta y guardar la LISTA COMPLETA con ObjectOutputStream.
    // No usar APPEND en ficheros serializados.
    public static void guardar(Path archivo, List<Equipo> lista) throws IOException {
        // PASO 2: crea la carpeta y usa ObjectOutputStream.
        // El método es void: no necesita devolver nada.
        Path carpeta = archivo.toAbsolutePath().getParent();
        Files.createDirectories(carpeta);

        try (ObjectOutputStream salida = new ObjectOutputStream(new FileOutputStream(archivo.toFile()))) {
            salida.writeObject(new ArrayList<>(lista));
        }
    }

    // MÉTODO DE APOYO COMPLETO: busca por ID sin leer archivos.
    public static Equipo buscar(List<Equipo> lista, int id) {
        for (Equipo equipo : lista) {
            if (equipo.getId() == id) {
                return equipo;
            }
        }
        return null;
    }

    // TODO 2.3 - Modificar SOLO en memoria. Devolver false si ID desconocido
    // o unidades < 0. NO guardar aquí: lo hará Main en opción 4.
    public static boolean cambiarUnidades(List<Equipo> lista, int id, int unidades) {
        // PASO 3: localiza el equipo y cambia sus unidades.
        Equipo equipo = buscar(lista, id);
        if (equipo == null || unidades < 0) {
            return false;

        }
        return true;
    }

    // TODO 2.4 - Exportar DOM XML. Crear raíz <equipos> y cada <equipo id="...">.
    // Dentro, <nombre> y <unidades>. No concatenar cadenas XML manualmente.
    // Los errores de XML se convierten en IOException para simplificar Main.
    public static void exportarXml(Path archivo, List<Equipo> lista) throws IOException {
        // PASO 4: crea un Document XML, elementos y Transformer.
        try {
            Document documento = DocumentBuilderFactory.newInstance().newDocumentBuilder().newDocument();
            Element raiz = documento.createElement("equipos");
            documento.appendChild(raiz);
            for (Equipo eq : lista) {
                Element equipo = documento.createElement("equipo");
                equipo.setAttribute("id", String.valueOf(eq.getId()));

                Element nombre = documento.createElement("nombre");
                nombre.setTextContent(eq.getNombre());
                equipo.appendChild(nombre);

                Element unidades = documento.createElement("unidades");
                unidades.setTextContent(String.valueOf(eq.getUnidades()));
                equipo.appendChild(unidades);

                raiz.appendChild(equipo);
            }

            Files.createDirectories(archivo.toAbsolutePath().getParent());

            Transformer transformador = TransformerFactory.newInstance().newTransformer();
            transformador.setOutputProperty(OutputKeys.INDENT, "yes");
            transformador.transform(new DOMSource(documento), new StreamResult(archivo.toFile()));

        } catch (Exception e) {
            // TODO: handle exception
            throw new IOException("Error al exportar XML", e);
        }
    }
}