from PyQt5.QtWidgets import QMainWindow

from QueryСlass import QueryHandler
from gui import Ui_MainWindow
from utils import CATEGORIES


class AppWindow(QMainWindow, Ui_MainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.handler = QueryHandler('categories.db')

    def initUI(self) -> None:
        """
        Настройка окна
        """
        self.setupUi(self)
        self.pushButton.clicked.connect(self.translate)
        self.comboBox.currentTextChanged.connect(self.change_widget)

    def translate(self) -> None:
        """
        Функция, выполняющая перевод количества УВ между классификациями
        """
        sys_from, sys_to = CATEGORIES[self.comboBox.currentText()][0], \
                           CATEGORIES[self.comboBox_2.currentText()][0]
        category = self.choose_category()
        res = ";\n".join(self.handler.query(sys_from, sys_to, category))
        self.show_result(res)

    def show_result(self, res: str) -> None:
        """
        Отображает результат в область вывода
        """
        self.plainTextEdit_2.clear()
        self.plainTextEdit_2.appendPlainText(res)

    def change_widget(self) -> None:
        """
        Заменяет виджет в QTabWidget при смене категории
        """
        index = CATEGORIES[self.comboBox.currentText()][1]
        self.stackedWidget.setCurrentIndex(index)

    def choose_category(self) -> str:
        """
         Осуществляет выбор категории
        """
        if self.comboBox.currentText() == "РФ-2013":
            return self.comboBox_3.currentText()
        elif self.comboBox.currentText() == "РКООН":
            return self.comboBox_4.currentText().split(' (')[0]
        else:
            return self.comboBox_5.currentText()
