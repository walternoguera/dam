# Control de Acceso a un Parking con Hilos

## Conceptos Clave:
- **Hilos (`Thread`)**: Se crean varios coches que intentan entrar y salir del parking al mismo tiempo.
- **Sincronización (`synchronized`)**: Se usa para evitar que múltiples hilos modifiquen el estado del parking simultáneamente.
- **Método `wait()`**: Hace que un coche espere si el parking está lleno.
- **Método `notifyAll()`**: Despierta a los coches en espera cuando un espacio queda libre.
- **Uso de colores ANSI en consola**: Cada coche tiene un color para visualizar mejor la ejecución.

## Funcionamiento del Código:
1. Se crea un parking con **5 espacios disponibles** (`Parking myParking = new Parking(5);`).
2. Se crean **10 coches (`Coche`)**, cada uno ejecutándose en su propio hilo.
3. Cada coche intenta entrar al parking:
   - Si hay espacio, entra (`entrar()`).
   - Si está lleno, **espera** (`wait()`).
4. Cada coche **simula estar comprando** (`Thread.sleep()` con un tiempo aleatorio).
5. Cuando el coche termina, **sale del parking** (`salir()`), liberando un espacio.

## Código Clave:
```java
public synchronized void entrar(String nombre_coche) throws InterruptedException {
    while (n_ocupadas == this.capacidad) {
        System.out.println("BLOQUEADO: el coche " + nombre_coche + " no puede pasar");
        wait(); // El coche espera hasta que haya espacio
    }
    n_ocupadas++;
    System.out.println("El coche " + nombre_coche + " YA HA ENTRADO Y APARCADO");
}
