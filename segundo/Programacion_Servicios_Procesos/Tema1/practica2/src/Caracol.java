import java.util.Random;

public class Caracol {
    public static void main(String[] args) throws Exception {
        int ralentizacionMax = Integer.parseInt(args[0]);
        Random rd = new Random();
        int ralentizacionActual = rd.nextInt(ralentizacionMax) + 1;
        Thread.sleep(ralentizacionActual * 1000);
        System.out.println(args[1]);

    }
}
