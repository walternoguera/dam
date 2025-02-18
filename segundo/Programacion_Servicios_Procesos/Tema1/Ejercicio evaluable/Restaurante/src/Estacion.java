import java.util.concurrent.BlockingDeque;
import java.util.concurrent.BlockingQueue;

public class Estacion extends Thread{
    private String nombre;
    private int tiempoProceso;
    private BlockingQueue<Integer> entrada; //?
    private BlockingQueue<Integer> salida;
    public Estacion(String nombre, int tiempoProceso, BlockingQueue<Integer> entrada, BlockingQueue<Integer> salida) {
        this.nombre = nombre;
        this.tiempoProceso = tiempoProceso;
        this.entrada = entrada;
        this.salida = salida;
    }

    public void run(){
try {
            while (true) {
                int pedido = entrada.take(); //toma el pedido de la cola

                //Si el pedido es -1, significa que ya no hay más pedidos y la estación debe finalizar
                if (pedido == -1) {
                    System.out.println(nombre + " ha terminado su trabajo.");
                    if (salida != null) salida.put(-1); //Pasa la señal de FIN a la siguiente estación
                    break;
                }

                System.out.println(nombre + " procesando el Pedido #" + pedido);
                Thread.sleep(tiempoProceso);
                System.out.println(nombre + " completado para el Pedido #" + pedido);

                if (salida != null) salida.put(pedido); //Pasa el pedido a la siguiente estación
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
