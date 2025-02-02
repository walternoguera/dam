# JavaFX Hello World

Este es un **proyecto básico de JavaFX** que muestra una ventana con un botón y un texto. Al hacer clic en el botón, el texto cambia dinámicamente.

## 📌 Características principales
- **Uso de JavaFX** para crear una interfaz gráfica.
- **Separación entre la vista (FXML) y la lógica (Controller en Java)**.
- **Carga de la interfaz desde un archivo FXML** mediante `FXMLLoader`.
- **Manejo de eventos**: un botón cambia el texto de una etiqueta (`Label`).

## 📂 Estructura del proyecto
```
📦 Proyecto JavaFX
 ├── 📂 src
 │   ├── 📂 main
 │   │   ├── 📂 java
 │   │   │   ├── 📂 org.example.holamundo
 │   │   │   │   ├── HelloApplication.java   # Clase principal que inicia la aplicación JavaFX
 │   │   │   │   ├── HelloController.java    # Controlador que maneja la lógica de la interfaz
 │   │   ├── 📂 resources
 │   │   │   ├── 📂 org.example.holamundo
 │   │   │   │   ├── hello-view.fxml         # Archivo FXML que define la interfaz gráfica
```

## 📜 Explicación del código
### **1️⃣ `HelloApplication.java`**
- `Application` → Clase base de todas las aplicaciones JavaFX.
- `start(Stage stage)` → Método que se ejecuta al iniciar la aplicación.
  ```java
  @Override
  public void start(Stage stage) throws IOException {
      FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("hello-view.fxml"));
      Scene scene = new Scene(fxmlLoader.load(), 320, 240);
      stage.setTitle("Hello!");
      stage.setScene(scene);
      stage.show();
  }
  ```
    - `FXMLLoader` carga la interfaz desde `hello-view.fxml`.
    - `Scene` define el contenido de la ventana.
    - `stage.setTitle()` establece el título de la ventana.
    - `stage.show()` muestra la ventana.

### **2️⃣ `HelloController.java`**
- `@FXML` → Anotación que indica que un campo o método está vinculado con el archivo FXML.
- `private Label welcomeText;` → Etiqueta de texto en la interfaz gráfica.
- `onHelloButtonClick()` → Método llamado cuando el usuario hace clic en el botón.
  ```java
  @FXML
  protected void onHelloButtonClick() {
      welcomeText.setText("hola mundo");
  }
  ```
    - Cambia el texto del `Label` cuando el usuario presiona el botón.

### **3️⃣ `hello-view.fxml`**
- `<VBox>` → Contenedor que organiza elementos verticalmente.
  ```xml
  <VBox alignment="CENTER" spacing="20.0"
        xmlns:fx="http://javafx.com/fxml/1"
        xmlns="http://javafx.com/javafx/23.0.1"
        fx:controller="org.example.holamundo.HelloController">
  ```
    - `alignment="CENTER"` → Centra los elementos dentro del VBox.
    - `spacing="20.0"` → Agrega espacio entre los elementos.
- `<Label>` → Etiqueta de texto.
  ```xml
  <Label fx:id="welcomeText" />
  ```
    - `fx:id="welcomeText"` → Identificador para enlazar con `HelloController.java`.
- `<Button>` → Botón interactivo.
  ```xml
  <Button onAction="#onHelloButtonClick" text="Hello!" />
  ```
    - `onAction="#onHelloButtonClick"` → Ejecuta el método `onHelloButtonClick()` cuando se presiona.

## 🔗 Recursos útiles
- [Documentación oficial de JavaFX](https://openjfx.io/)
- [Guía rápida de FXML](https://openjfx.io/javadoc/17/javafx.fxml/javafx/fxml/doc-files/introduction_to_fxml.html)

---
📌 **Autor:** [Walter Morel Noguera](https://walternoguera.com) 