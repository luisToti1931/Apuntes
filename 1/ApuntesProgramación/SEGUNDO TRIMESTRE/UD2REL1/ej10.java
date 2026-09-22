package ApuntesProgramación.UD2REL1;

import java.util.ArrayList;

public class ej10 {
    public static void main(String[] args) {
        ArrayList<Integer> pila = new ArrayList<>();
        pila.add(10);
        pila.add(20);
        pila.add(30);
        System.out.println("Lista de clientes: " + pila);
        Integer clienteAtendido = pila.remove(pila.size() - 1);
        System.out.println("He atendido a " + clienteAtendido);
        System.out.println("Clientes restantes: " + pila);
        clienteAtendido = pila.remove(pila.size() - 1);
        System.out.println("He atendido a " + clienteAtendido);
        System.out.println("Clientes restantes: " + pila);
        clienteAtendido = pila.remove(pila.size() - 1);
        System.out.println("He atendido a " + clienteAtendido);
        System.out.println("Clientes restantes: " + pila);
    }
}
