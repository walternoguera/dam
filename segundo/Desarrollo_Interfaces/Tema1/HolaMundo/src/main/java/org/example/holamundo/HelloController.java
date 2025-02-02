package org.example.holamundo;

import javafx.fxml.FXML; // Importa la anotación @FXML
import javafx.scene.control.Label; // Importa la clase Label para manejar etiquetas de texto en JavaFX

public class HelloController {

    @FXML // Indica que este Label está vinculado con un elemento en el archivo FXML
    private Label welcomeText;

    @FXML // Indica que este método se usará en el archivo FXML como un manejador de eventos
    protected void onHelloButtonClick() {
        // Cambia el texto del Label cuando se hace clic en el botón
        welcomeText.setText("hola mundo");
    }
}
