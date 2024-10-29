module com.example.musical_notation {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.kordamp.bootstrapfx.core;

    opens com.example.musical_notation to javafx.fxml;
    exports com.example.musical_notation;
}