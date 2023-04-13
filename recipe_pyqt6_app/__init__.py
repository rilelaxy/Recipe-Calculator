__version__ = '0.1.0'
import sys


from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QPushButton, QFormLayout, QGridLayout, QSpinBox, QMainWindow, QVBoxLayout, QComboBox, QWidget, QLabel, QHBoxLayout




# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    ingredients = ["Pick one!","Milk", "Sugar", "Egg", "All Purpose Flour", "Baking Soda", "Vanilla Extract", "Vegtable Oil", "Olive Oil","Honey", "Butter" ]
    def __init__(self):
        super().__init__()
   
        self.setWindowTitle("Reinvent Recipe")


        # label stuff here
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

        # combo boxes here
        combobox1 = QComboBox()
        combobox1.addItems(MainWindow.ingredients)
        combobox2 = QComboBox()
        combobox2.addItems(MainWindow.ingredients)
        combobox3 = QComboBox()
        combobox3.addItems(MainWindow.ingredients)
        combobox4 = QComboBox()
        combobox4.addItems(MainWindow.ingredients)
        combobox5 = QComboBox()
        combobox5.addItems(MainWindow.ingredients)
        combobox6 = QComboBox()
        combobox6.addItems(MainWindow.ingredients)


        # spinbox stuff here
        amountmeasured = QSpinBox()


        amountmeasured.setMinimum(-10)
        amountmeasured.setMaximum(3)
        # Or: widget.setRange(-10,3)


        
        amountmeasured.setSuffix(" of it's measured amount")
        amountmeasured.setSingleStep(1) 
        amountmeasured.valueChanged.connect(self.value_changed)
        amountmeasured.textChanged.connect(self.value_changed_str)
        
        amountmeasured2 = QSpinBox()


        amountmeasured2.setMinimum(-10)
        amountmeasured2.setMaximum(3)
        # Or: widget.setRange(-10,3)


        
        amountmeasured2.setSuffix(" of it's measured amount")
        amountmeasured2.setSingleStep(1) 
        amountmeasured2.valueChanged.connect(self.value_changed)
        amountmeasured2.textChanged.connect(self.value_changed_str)

        amountmeasured3 = QSpinBox()


        amountmeasured3.setMinimum(-10)
        amountmeasured3.setMaximum(3)
        # Or: widget.setRange(-10,3)


        
        amountmeasured3.setSuffix(" of it's measured amount")
        amountmeasured3.setSingleStep(1) 
        amountmeasured3.valueChanged.connect(self.value_changed)
        amountmeasured3.textChanged.connect(self.value_changed_str)
        
        amountmeasured4 = QSpinBox()


        amountmeasured4.setMinimum(-10)
        amountmeasured4.setMaximum(3)
        # Or: widget.setRange(-10,3)


        
        amountmeasured4.setSuffix(" of it's measured amount")
        amountmeasured4.setSingleStep(1) 
        amountmeasured4.valueChanged.connect(self.value_changed)
        amountmeasured4.textChanged.connect(self.value_changed_str)

        amountmeasured5 = QSpinBox()


        amountmeasured5.setMinimum(-10)
        amountmeasured5.setMaximum(3)
        # Or: widget.setRange(-10,3)


        
        amountmeasured5.setSuffix(" of it's measured amount")
        amountmeasured5.setSingleStep(1) 
        amountmeasured5.valueChanged.connect(self.value_changed)
        amountmeasured5.textChanged.connect(self.value_changed_str)

        amountmeasured6 = QSpinBox()


        amountmeasured6.setMinimum(-10)
        amountmeasured6.setMaximum(3)
        # Or: widget.setRange(-10,3)


        
        amountmeasured6.setSuffix(" of it's measured amount")
        amountmeasured6.setSingleStep(1) 
        amountmeasured6.valueChanged.connect(self.value_changed)
        amountmeasured6.textChanged.connect(self.value_changed_str)
        
        


        button = QPushButton(text="Give me my recipe!", parent=self)
        button.setFixedSize(200, 60)


        

        self.setCentralWidget(amountmeasured)
        # layout here
        layout1 = QGridLayout()
        layout1.addWidget(title, 0, 0, )
        layout1.addWidget(labelinstructions, 1, 0, )
        layout1.addWidget(combobox1, 2, 0,)
        layout1.addWidget(combobox2, 4, 0,)
        layout1.addWidget(combobox3, 6, 0,)
        layout1.addWidget(combobox4, 8, 0,)
        layout1.addWidget(combobox5, 10, 0,)
        layout1.addWidget(combobox6, 12, 0,)
        layout1.addWidget(amountmeasured, 3, 0,)
        layout1.addWidget(amountmeasured2, 5, 0,)
        layout1.addWidget(amountmeasured3, 7, 0,)
        layout1.addWidget(amountmeasured4, 9, 0,)
        layout1.addWidget(amountmeasured5, 11, 0,)
        layout1.addWidget(amountmeasured6, 13, 0,)
        layout1.addWidget(button, 14, 0, Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(layout1)
        container = QWidget()
        container.setLayout(layout1)
        self.setCentralWidget(container)

        self.result = QLabel("Click button for recipe!")
        self.result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result.adjustSize()
        button.clicked.connect(self.update)
        layout1.addWidget(self.result)
    def update(self):
        self.result.setText("Muffins")

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