package ApuntesProgramación.UD2REL1;

import java.util.ArrayList;

public class ej9 {
    public static void main(String[] args) {
        ArrayList<String> cola = new ArrayList<>();
        cola.add("cliente1");
        cola.add("cliente2");
        cola.add("cliente3");
        System.out.println("Lista de clientes: " + cola);
        String clienteAtendido = cola.remove(0);
        System.out.println("He atendido a " + clienteAtendido);
        System.out.println("Clientes restantes: " + cola);
        clienteAtendido = cola.remove(0);
        System.out.println("He atendido a " + clienteAtendido);
        System.out.println("Clientes restantes: " + cola);
        clienteAtendido = cola.remove(0);
        System.out.println("He atendido a " + clienteAtendido);
        System.out.println("Clientes restantes: " + cola);

    }
}
