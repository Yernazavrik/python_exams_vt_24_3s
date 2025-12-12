from PyQt5.QtWidgets import *

class FormProduct:
    def __init__(self):
        self.layout = QVBoxLayout()
    
    def add_widget(self, widget):
        self.layout.addWidget(widget)


class FormBuilder:
    def __init__(self):
        self.product = FormProduct()
    
    def add_title(self):
        pass
    
    def add_inputs(self):
        pass
    
    def add_controls(self):
        pass
    
    def get_result(self):
        return self.product


class MiniFormBuilder(FormBuilder):
    def add_title(self):
        title = QLabel("Мини форма")
        self.product.add_widget(title)
    
    def add_inputs(self):
        input_field = QLineEdit()
        self.product.add_widget(input_field)
    
    def add_controls(self):
        button = QPushButton("Кнопка")
        self.product.add_widget(button)

class FullFormBuilder(FormBuilder):
    def add_title(self):
        title = QLabel("Расширенная форма")
        self.product.add_widget(title)
    
    def add_inputs(self):
        input1 = QLineEdit()
        input2 = QLineEdit()
        self.product.add_widget(input1)
        self.product.add_widget(input2)
    
    def add_controls(self):
        button1 = QPushButton("Кнопка 1")
        button2 = QPushButton("Кнопка 2")
        self.product.add_widget(button1)
        self.product.add_widget(button2)

class FormDirector:
    def __init__(self, builder): 
        self.builder = builder
    
    def build_form(self):
        self.builder.add_title()
        self.builder.add_inputs()
        self.builder.add_controls()
        return self.builder.get_result()


def main():
    app = QApplication([])


    mini_builder = MiniFormBuilder()
    director = FormDirector(mini_builder)
    mini_product = director.build_form()
    window1 = QWidget()
    window1.setLayout(mini_product.layout)
    window1.setWindowTitle("Мини форма")
    window1.show()

    full_builder = FullFormBuilder()
    director = FormDirector(full_builder)
    full_product = director.build_form()
    
    window2 = QWidget()
    window2.setLayout(full_product.layout)
    window2.setWindowTitle("Расширенная форма")
    window2.show()

    app.exec_()

if __name__ == "__main__":
    main()
