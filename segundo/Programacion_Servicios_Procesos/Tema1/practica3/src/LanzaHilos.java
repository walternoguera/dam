import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.List;
import java.util.ArrayList;

public class LanzaHilos {
    public static void main(String[] args) {
        String[][] parametros = {
                { "3", "C" },
                { "1", "D" }
        };

        try {
            List<Process> listaProceso = new ArrayList<>();

            for (String[] param : parametros) {
                ProcessBuilder pb = new ProcessBuilder("java", "-cp",
                        "C:\\Users\\WALTERALFONSOMORELNO\\Documents\\dam\\segundo\\Programacion_Servicios_Procesos\\Tema1\\practica2\\bin",
                        "Caracol", param[0], param[1]);// reemplazar el path por bin
                Process p = pb.start();
                listaProceso.add(p);

                new Thread(() -> { // clase thread
                    try {
                        BufferedReader salidaCaracol1 = new BufferedReader(new InputStreamReader(p.getInputStream()));
                        String linea;
                        while ((linea = salidaCaracol1.readLine()) != null) {
                            System.out.println(linea);
                        }
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }).start();
            }
        } catch (Exception ee) {
            System.err.println("Exception: " + ee.getMessage());
        }
    }
}
