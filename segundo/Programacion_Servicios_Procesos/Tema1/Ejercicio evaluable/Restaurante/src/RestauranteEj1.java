import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;

public class RestauranteEj1 {
    public static void main(String[] args) {
        int numeroPedidos = 6;
        int capacidad = 2;//significa que la cola solo puede tener 2 pedidos a la vez

        //creamos la cola
        BlockingQueue<Integer> colaRecepcion = new ArrayBlockingQueue<>(capacidad);
        BlockingQueue<Integer> colaPan = new ArrayBlockingQueue<>(capacidad);
        BlockingQueue<Integer> colaCarne = new ArrayBlockingQueue<>(capacidad);
        BlockingQueue<Integer> colaIngredientes = new ArrayBlockingQueue<>(capacidad);
        BlockingQueue<Integer> colaEnsamblado = new ArrayBlockingQueue<>(capacidad);
        BlockingQueue<Integer> colaEmpaque = new ArrayBlockingQueue<>(capacidad);
        
        //creamos estaciones
        new Estacion("Recepcion", 3000, colaRecepcion, colaPan).start();
        new Estacion("Pan", 3000, colaPan, colaCarne).start();
        new Estacion("Carne", 3000, colaCarne, colaIngredientes).start();
        new Estacion("Ingredientes", 3000, colaIngredientes, colaEnsamblado).start();
        new Estacion("Ensamblado", 3000, colaEnsamblado, colaEmpaque).start();
        new Estacion("Empaque", 3000, colaEmpaque, null).start();

        //agregamos pedidos a la cola de recepcion
        for (int i = 1; i <= numeroPedidos; i++){
            try {
                colaRecepcion.put(i);
                System.out.println("Pedido #"+ i +" Ingresando en la recepcion.");
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        try {
            colaRecepcion.put(-1); //Envía la señal de fin
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
