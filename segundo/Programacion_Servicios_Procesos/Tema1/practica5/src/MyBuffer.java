import java.util.LinkedList;

public class MyBuffer {

    private final int capacidad;
    private final LinkedList<Integer> cola = new LinkedList<>();

    public MyBuffer (int in_capacidad)
    {
        this.capacidad=in_capacidad;
    }
    public synchronized void producir(int value) throws InterruptedException
    {
        while (cola.size()==capacidad) 
        {            
            System.out.println("BLOQUEADO PRODUCTOR para elemento "+value);
            wait();
        }
        cola.add(value);
        notifyAll();        
    }
    public synchronized int consumir(int nivel) throws InterruptedException
    {
        while (cola.isEmpty()) 
        {            
            System.out.println("BLOQUEADO CONSUMIDOR NIVEL:"+nivel+" COLA VACIAAAAAAAAAAAAAAAAAAAAAAAAAAA");
            wait();
        }
        int value = cola.removeFirst();
        notifyAll();
        return value;
    }

    @Override
    public String toString() {
        return "MiBuffer con capacidad "+capacidad+" contiene "+cola.toString();
    }
}
