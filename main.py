import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()

        self.setWindowTitle("calculator")

        self.hbox_line = QHBoxLayout()
        self.hbox0 = QHBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()
        self.vbox = QVBoxLayout()

        self.vbox.addLayout(self.hbox_line)
        self.vbox.addLayout(self.hbox0)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)

        self.line = QLineEdit(self)
        #self.line.setReadOnly(True)
        self.line.setEnabled(False)

        self.b_1 = QPushButton("1", self)
        self.b_2 = QPushButton("2", self)
        self.b_3 = QPushButton("3", self)
        self.b_4 = QPushButton("4", self)
        self.b_5 = QPushButton("5", self)
        self.b_6 = QPushButton("6", self)
        self.b_7 = QPushButton("7", self)
        self.b_8 = QPushButton("8", self)
        self.b_9 = QPushButton("9", self)
        self.b_0 = QPushButton("0", self)
        self.b_clear = QPushButton("AC", self)
        self.b_delete = QPushButton("delete", self)
        self.b_point = QPushButton(".", self)
        self.b_del = QPushButton("/", self)
        self.b_umn = QPushButton("*", self)
        self.b_minus = QPushButton("-", self)
        self.b_plus = QPushButton("+", self)
        self.b_res = QPushButton("=", self)

        # порядок расположения
        self.hbox_line.addWidget(self.line)
        self.hbox1.addWidget(self.b_1)
        self.hbox1.addWidget(self.b_2)
        self.hbox1.addWidget(self.b_3)
        self.hbox1.addWidget(self.b_plus)
        self.hbox2.addWidget(self.b_4)
        self.hbox2.addWidget(self.b_5)
        self.hbox2.addWidget(self.b_6)
        self.hbox2.addWidget(self.b_minus)
        self.hbox3.addWidget(self.b_7)
        self.hbox3.addWidget(self.b_8)
        self.hbox3.addWidget(self.b_9)
        self.hbox3.addWidget(self.b_umn)
        self.hbox4.addWidget(self.b_0)
        self.hbox4.addWidget(self.b_point)
        self.hbox4.addWidget(self.b_res)
        self.hbox4.addWidget(self.b_del)
        self.hbox0.addWidget(self.b_clear)
        self.hbox0.addWidget(self.b_delete)

        self.setLayout(self.vbox)

        self.b_1.clicked.connect(lambda: self.addText("1"))
        self.b_2.clicked.connect(lambda: self.addText("2"))
        self.b_3.clicked.connect(lambda: self.addText("3"))
        self.b_4.clicked.connect(lambda: self.addText("4"))
        self.b_5.clicked.connect(lambda: self.addText("5"))
        self.b_6.clicked.connect(lambda: self.addText("6"))
        self.b_7.clicked.connect(lambda: self.addText("7"))
        self.b_8.clicked.connect(lambda: self.addText("8"))
        self.b_9.clicked.connect(lambda: self.addText("9"))
        self.b_0.clicked.connect(lambda: self.addText("0"))
        self.b_point.clicked.connect(lambda: self.addText("."))
        self.b_del.clicked.connect(lambda: self.operation("/"))
        self.b_umn.clicked.connect(lambda: self.operation("*"))
        self.b_minus.clicked.connect(lambda: self.operation("-"))
        self.b_plus.clicked.connect(lambda: self.operation("+"))
        self.b_res.clicked.connect(self.result)
        self.b_clear.clicked.connect(self.clear)
        self.b_delete.clicked.connect(self.delete)

    def addText(self, param):
        line = self.line.text()
        self.line.setText(line + param)

    def operation(self, param):
        self.num1 = self.line.text()
        self.line.setText("")
        self.op = param

    def delete(self):
        text = self.line.text()
        self.line.setText(text[:len(text) - 1])

    def clear(self):
        self.line.setText("")

    def result(self):
        self.num2 = self.line.text()
        try:
            float(self.num1)
            float(self.num2)
        except:
            return
        if self.op == "+":
            self.line.setText(str(float(self.num1) + float(self.num2)))
        elif self.op == "-":
            self.line.setText(str(float(self.num1) - float(self.num2)))
        elif self.op == "*":
            self.line.setText(str(float(self.num1) * float(self.num2)))
        elif self.op == "/":
            if float(self.num2) == 0:
                self.line.setText(str("на ноль делить нельзя"))
            else:
                self.line.setText(str(float(self.num1) / float(self.num2)))

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Plus:
            self.operation("+")
        if e.key() == Qt.Key_Minus:
            self.operation("-")
        if e.key() == Qt.Key_Slash:
            self.operation("/")
        if e.key() == Qt.Key_Asterisk:
            self.operation("*")
        if e.key() == Qt.Key_1:
            self.addText("1")
        if e.key() == Qt.Key_2:
            self.addText("2")
        if e.key() == Qt.Key_3:
            self.addText("3")
        if e.key() == Qt.Key_4:
            self.addText("4")
        if e.key() == Qt.Key_5:
            self.addText("5")
        if e.key() == Qt.Key_6:
            self.addText("6")
        if e.key() == Qt.Key_7:
            self.addText("7")
        if e.key() == Qt.Key_8:
            self.addText("8")
        if e.key() == Qt.Key_9:
            self.addText("9")
        if e.key() == Qt.Key_0:
            self.addText("0")
        if e.key() == Qt.Key_Period:
            self.addText(".")
        if e.key() == Qt.Key_Delete:
            self.clear()
        if e.key() == Qt.Key_Backspace:
            self.delete()
        if e.key() == Qt.Key_Enter:
            self.result()
        if e.key() == Qt.Key_Equal:
            self.result()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
