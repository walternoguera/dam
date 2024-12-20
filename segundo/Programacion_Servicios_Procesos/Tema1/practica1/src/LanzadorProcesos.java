import java.io.BufferedReader;
import java.io.InputStreamReader;

public class LanzadorProcesos {
    public static void main(String[] args) {
        ProcessBuilder pb = new ProcessBuilder("java", "-cp", "bin", "ProcesoP01", "Jose");
        try {
            /* Proceso 1 */
            Process proceso = pb.start();
            BufferedReader lectorSalida = new BufferedReader(new InputStreamReader(proceso.getInputStream()));
            String linea;
            while ((linea = lectorSalida.readLine()) != null) {
                System.out.println("Extraido del proceso: " + linea);
            }
            System.out.println("Con PID: " + proceso.pid());

            /* Proceso 2 */
            Process proceso2 = pb.start();
            lectorSalida = new BufferedReader(new InputStreamReader(proceso2.getInputStream()));
            while ((linea = lectorSalida.readLine()) != null) {
                System.out.println("Extraido del proceso: " + linea);
            }
            System.out.println("Con PID: " + proceso2.pid());
        } catch (Exception ee) {
            System.out.println("Exception " + ee.getMessage());
        }
        System.out.println("Fin del proceso padre lanzador");
    }
}
