public class Principal {
    public static void main(String[] args) {
        
        Parking myParking = new Parking(5);
        for (int i = 1; i <= 10; i++){
            new Thread(new Coche(myParking, "coche_"+i,i)).start();
        }
    }
}
