# Práctica 2: Simulación de Caracoles con Procesos

Esta práctica simula una carrera entre "caracoles", donde cada caracol es un proceso independiente. Cada caracol tiene un retraso aleatorio antes de imprimir su nombre, lo que simula una "carrera".

### Funcionamiento
- **`Caracol.java`**: Genera un retraso aleatorio usando `Random` y `Thread.sleep()`, luego imprime su nombre con `System.out.println()`.
- **`LanzaCaracoles.java`**: Lanza varios procesos `Caracol` usando `ProcessBuilder`. Cada proceso se ejecuta con los parámetros adecuados, como el tiempo de retraso y el nombre del caracol. Los resultados de cada proceso se capturan con `BufferedReader` y se muestran en consola.
- **Manejo de excepciones**: Cualquier error durante la ejecución de los procesos es manejado con un bloque `try-catch`.

### Salida Esperada
Ejecutando el programa, la salida será algo como:

```plaintext
B
A
