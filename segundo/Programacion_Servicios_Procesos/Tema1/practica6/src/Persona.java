
import java.util.concurrent.Semaphore;


public class Persona implements Runnable
{
    private final Semaphore semaforo;
    private final String nombre;
    private final int persona_lenta;
    public Persona (Semaphore semaforo, String nombre, int persona_lenta)
    {
        this.semaforo=semaforo;
        this.nombre=nombre;
        this.persona_lenta = persona_lenta;
    }
    @Override
    public void run() 
    {
        try 
        {
            System.out.println("Pide permiso "+nombre);
            semaforo.acquire(); // pide permiso para entrar en un hueco    
            System.out.println("Trabajando " +nombre+ " con una persona lenta "+persona_lenta);      
            Thread.sleep(persona_lenta);
  
        } catch (InterruptedException e) 
        {
            System.out.println("Hilo interrumpido "+e.getMessage());
        }
        finally
        {
            System.out.println("Termina "+nombre);
            semaforo.release(); // libera un hueco
        }      
    }
}