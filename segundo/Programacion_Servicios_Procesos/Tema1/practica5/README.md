# Productor-Consumidor en Java

## Conceptos clave:
- **Hilos (Thread)**: Permiten ejecutar tareas en paralelo.
- **Sincronización**: Controla el acceso a recursos compartidos.
- **Buffer compartido (`MyBuffer`)**: Donde los productores colocan elementos y los consumidores los extraen.
- **Métodos `wait()` y `notifyAll()`**: Se usan para gestionar la espera y el despertar de los hilos.

## Ciclo de Vida de los Hilos:
1. Se crea un hilo (`Thread` con `Runnable`).
2. Se inicia con `.start()`, lo que ejecuta su `run()`.
3. Si el buffer está lleno, el productor se bloquea (`wait()`).
4. Si el buffer está vacío, el consumidor se bloquea (`wait()`).
5. Cuando hay cambios en el buffer, `notifyAll()` despierta los hilos bloqueados.

## Dependency Management

The `JAVA PROJECTS` view allows you to manage your dependencies. More details can be found [here](https://github.com/microsoft/vscode-java-dependency#manage-dependencies).
