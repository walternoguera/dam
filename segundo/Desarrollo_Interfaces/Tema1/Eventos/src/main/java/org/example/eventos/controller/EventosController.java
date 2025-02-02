package org.example.eventos.controller;

import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.effect.DropShadow;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseDragEvent;
import javafx.scene.input.MouseEvent;
import org.example.eventos.MyApplication;

import java.net.URL;
import java.util.ResourceBundle;

public class EventosController implements Initializable {

    @FXML
    private Button btn1;

    @FXML
    private Button btn2;

    @FXML
    private Button btn3;

    @FXML
    private Button btn4;

    @FXML
    private Button btnBorrar;

    @FXML
    private Button btnIgual;

    @FXML
    private Button btnSumar;

    @FXML
    private TextField textoNumero;

    private DropShadow sombra;


    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        //empieza a generar la logica de la app
        instancias();
        initGUI();
        acciones();

    }

    private void acciones() {
        //cuando se pasa por encima del boton, sombra
        //cuando se sale del boton, se quita la sombra
        //cuando se pulsa en el boton, pasa algo

        btnSumar.setOnMouseEntered(new EventHandler<MouseEvent>() {
            @Override
            public void handle(MouseEvent event) {
                btnSumar.setEffect(sombra);
            }
        });

        btnSumar.setOnMouseExited(new EventHandler<MouseEvent>() {
            @Override
            public void handle(MouseEvent event) {
                btnSumar.setEffect(null);
            }
        });

    }
    private void instancias(){
        sombra = new DropShadow();
    }
    private void initGUI(){
        btnSumar.setGraphic(new ImageView(new Image(MyApplication.class.getResourceAsStream("/iconos/mas.png"))));
        btnSumar.setBackground(null);
        btnIgual.setGraphic(new ImageView(new Image(MyApplication.class.getResourceAsStream("/iconos/igual.png"))));
        btnIgual.setBackground(null);
        btnBorrar.setGraphic(new ImageView(new Image(MyApplication.class.getResourceAsStream("/iconos/borrar.png"))));
        btnBorrar.setBackground(null);
    }
}
