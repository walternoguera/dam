package org.example.holamundo; // Define el paquete donde se encuentra la clase

import javafx.application.Application; // Importa la clase base para aplicaciones JavaFX
import javafx.fxml.FXMLLoader; // Permite cargar archivos FXML (interfaces gráficas definidas en XML)
import javafx.scene.Scene; // Representa una escena en JavaFX
import javafx.stage.Stage; // Representa una ventana en JavaFX

import java.io.IOException; // Manejo de excepciones para operaciones de entrada/salida

// Clase principal que extiende Application, lo que la convierte en una aplicación JavaFX
public class HelloApplication extends Application {

    @Override
    public void start(Stage stage) throws IOException {
        // Carga el archivo FXML que define la interfaz gráfica
        FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("hello-view.fxml"));

        // Crea una escena con el diseño cargado del FXML y define su tamaño (320x240 píxeles)
        Scene scene = new Scene(fxmlLoader.load(), 320, 240);

        // Establece el título de la ventana
        stage.setTitle("Hello!");

        // Asigna la escena a la ventana
        stage.setScene(scene);

        // Muestra la ventana en pantalla
        stage.show();
    }

    // Método main, punto de entrada de la aplicación
    public static void main(String[] args) {
        launch(); // Inicia la aplicación JavaFX
    }
}
