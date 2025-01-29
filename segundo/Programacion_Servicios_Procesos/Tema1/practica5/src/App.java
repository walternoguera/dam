public class App {
    public static void main(String[] args) throws Exception {

        MyBuffer buffer1 = new MyBuffer(5);
        //cola fifo
        buffer1.producir(12);
        buffer1.producir(13);
        buffer1.producir(14);
        buffer1.producir(15);
        buffer1.producir(16);

        //consumimos y por defecto va usar el primero es decir el 12
        int val = buffer1.consumir();

        System.out.println(buffer1);
    }
}
