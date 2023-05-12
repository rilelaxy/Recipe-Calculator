import sys


from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QPushButton, QFormLayout, QGridLayout, QSpinBox, QMainWindow, QVBoxLayout, QComboBox, QWidget, QLabel, QHBoxLayout




# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    ingredients = ["Pick one!","Milk ", "Sugar ", "Egg ", "All Purpose Flour ", "Baking Soda ", "Vanilla Extract ", "Vegtable Oil ", "Olive Oil ","Honey ", "Butter " ]
    def __init__(self):
        super().__init__()
   
        self.setWindowTitle("Reinvent Recipe")


        # Labeling and fonts
        labelinstructions = QLabel("Instructions: Step 1: Input ingredients, Step 2: Press calculate Step 3: Select your recipe and enjoy!")
        font = labelinstructions.font()
        font.setPointSize(10)
        labelinstructions.setFont(font)
        labelinstructions.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        title = QLabel("Reinvent Recipe!")
        font = title.font()
        font.setPointSize(30)
        title.setFont(font)
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        # Comboboxes and item adding ingredients
        self.combo_boxes = []
        self.combobox1 = QComboBox()
        self.combobox1.addItems(MainWindow.ingredients)
        self.combo_boxes.append(self.combobox1)
        self.combobox2 = QComboBox()
        self.combobox2.addItems(MainWindow.ingredients)
        self.combo_boxes.append(self.combobox2)
        self.combobox3 = QComboBox()
        self.combobox3.addItems(MainWindow.ingredients)
        self.combo_boxes.append(self.combobox3)
        self.combobox4 = QComboBox()
        self.combobox4.addItems(MainWindow.ingredients)
        self.combo_boxes.append(self.combobox4)
        self.combobox5 = QComboBox()
        self.combobox5.addItems(MainWindow.ingredients)
        self.combo_boxes.append(self.combobox5)
        self.combobox6 = QComboBox()
        self.combobox6.addItems(MainWindow.ingredients)
        self.combo_boxes.append(self.combobox6)


        # Spinbox functions
        self.amountmeasured2 = QSpinBox()
        self.amountmeasured3 = QSpinBox()
        self.amountmeasured4 = QSpinBox()
        self.amountmeasured = QSpinBox()
        self.amountmeasured5 = QSpinBox()
        self.amountmeasured6 = QSpinBox()

        
        # Spinbox settings
        self.amountmeasured.setMinimum(-10)
        self.amountmeasured.setMaximum(3)
        self.amountmeasured.setSuffix(" of it's measured amount")
        self.amountmeasured.setSingleStep(1) 
        self.amountmeasured.valueChanged.connect(self.value_changed)
        self.amountmeasured.textChanged.connect(self.value_changed_str)
        
        self.amountmeasured2.setMinimum(-10)
        self.amountmeasured2.setMaximum(3)
        
        self.amountmeasured2.setSuffix(" of it's measured amount")
        self.amountmeasured2.setSingleStep(1) 
        self.amountmeasured2.valueChanged.connect(self.value_changed)
        self.amountmeasured2.textChanged.connect(self.value_changed_str)

        self.amountmeasured3.setMinimum(-10)
        self.amountmeasured3.setMaximum(3)

        self.amountmeasured3.setSuffix(" of it's measured amount")
        self.amountmeasured3.setSingleStep(1) 
        self.amountmeasured3.valueChanged.connect(self.value_changed)
        self.amountmeasured3.textChanged.connect(self.value_changed_str)
        
        self.amountmeasured4.setMinimum(-10)
        self.amountmeasured4.setMaximum(3)

        self.amountmeasured4.setSuffix(" of it's measured amount")
        self.amountmeasured4.setSingleStep(1) 
        self.amountmeasured4.valueChanged.connect(self.value_changed)
        self.amountmeasured4.textChanged.connect(self.value_changed_str)

        self.amountmeasured5.setSuffix(" of it's measured amount")
        self.amountmeasured5.setSingleStep(1) 
        self.amountmeasured5.valueChanged.connect(self.value_changed)
        self.amountmeasured5.textChanged.connect(self.value_changed_str)

        self.amountmeasured5.setMinimum(-10)
        self.amountmeasured5.setMaximum(3)

        self.amountmeasured6.setSuffix(" of it's measured amount")
        self.amountmeasured6.setSingleStep(1) 
        self.amountmeasured6.valueChanged.connect(self.value_changed)
        self.amountmeasured6.textChanged.connect(self.value_changed_str)

        self.amountmeasured6.setMinimum(-10)
        self.amountmeasured6.setMaximum(3)

        self.setCentralWidget(self.amountmeasured)
        
        # Calculate button
        button = QPushButton(text="Give me my recipe!", parent=self)
        button.setFixedSize(200, 60)

        
        # Grid layout setup
        layout1 = QGridLayout()
        layout1.addWidget(title, 0, 0, )
        layout1.addWidget(labelinstructions, 1, 0, )
        layout1.addWidget(self.combobox1, 2, 0,)
        layout1.addWidget(self.combobox2, 4, 0,)
        layout1.addWidget(self.combobox3, 6, 0,)
        layout1.addWidget(self.combobox4, 8, 0,)
        layout1.addWidget(self.combobox5, 10, 0,)
        layout1.addWidget(self.combobox6, 12, 0,)
        layout1.addWidget(self.amountmeasured, 3, 0,)
        layout1.addWidget(self.amountmeasured2, 5, 0,)
        layout1.addWidget(self.amountmeasured3, 7, 0,)
        layout1.addWidget(self.amountmeasured4, 9, 0,)
        layout1.addWidget(self.amountmeasured5, 11, 0,)
        layout1.addWidget(self.amountmeasured6, 13, 0,)
        layout1.addWidget(button, 14, 0, Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(layout1)
        container = QWidget()
        container.setLayout(layout1)
        self.setCentralWidget(container)

        # Button functionality
        self.result = QLabel("Click button for recipe!")
        self.result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result.adjustSize()
        button.clicked.connect(self.update)
        layout1.addWidget(self.result)

    def update(self):
        text = ""
        for box in self.combo_boxes:
            boxtext = box.currentText()
            if boxtext == "Pick one!":
                continue
            text += boxtext
        self.result.setText(text)

    def value_changed(self, i):
        print(i)


    def value_changed_str(self, s):
        print(s)


    def current_text_changed(self, s):
        print("Current text: ", s)


app = QApplication(sys.argv)


window = MainWindow()
window.show()


app.exec()