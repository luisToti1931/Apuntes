package ApuntesProgramación.UD2REL1;
import java.util.ArrayList;

public class ej7 {
        public static void main(String[] args) {
        ArrayList<String> dias = new ArrayList<>(); 
            dias.add("lunes");
            dias.add("martes");
            dias.add("miercoles");
            dias.add("jueves");
            dias.add("viernes");
            dias.add("sabado");
            dias.add("domingo");
            
            dias.set(6, "Domingo (Fin de semana)");

            System.out.println(dias);
    }
}
