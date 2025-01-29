class Tarea implements Runnable
{
    private final int tiempo;
    private final String nombre;
    public Tarea(String nombreTarea, int tiempoDormido){
        this.tiempo=tiempoDormido;
        this.nombre=nombreTarea;
    }

    @Override
    public void run() {
        try {
            System.out.println(this.nombre + ":inicio de ejecución");
            Thread.sleep(this.tiempo);
            System.out.println(this.nombre + ": fin de ejecución");
        } catch (Exception e) {
            System.out.println("Exception" + e.getMessage());
        }
    }
}