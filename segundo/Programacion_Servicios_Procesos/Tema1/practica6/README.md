# Control de Acceso con Semáforos en Java

## Conceptos Clave:
- **Hilos (`Thread`)**: Permiten ejecutar múltiples tareas en paralelo.
- **Semáforo (`Semaphore`)**: Controla cuántos hilos pueden acceder a un recurso al mismo tiempo.
- **Método `acquire()`**: Bloquea el hilo hasta que haya un permiso disponible.
- **Método `release()`**: Libera un permiso para que otro hilo pueda ejecutarse.

## Funcionamiento del Código:
1. Se crea un semáforo con **1 permiso** (`Semaphore semaforo = new Semaphore(1);`).
2. Se crean 8 hilos (`Persona`), cada uno con un tiempo de espera aleatorio.
3. Cada hilo intenta adquirir el semáforo (`acquire()`):
   - Si el semáforo está disponible, entra y ejecuta su tarea.
   - Si el semáforo está ocupado, el hilo se bloquea hasta que se libere.
4. Una vez que termina, libera el semáforo (`release()`), permitiendo que otro hilo lo tome.

## Código Clave:
```java
Semaphore semaforo = new Semaphore(1); // Solo 1 hilo puede acceder a la vez

semaforo.acquire(); // Pide permiso para acceder
System.out.println("Trabajando " + nombre);
Thread.sleep(persona_lenta); // Simula el trabajo
semaforo.release(); // Libera el permiso para que otro hilo pueda ejecutarse
