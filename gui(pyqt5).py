from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 314)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 421, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menu = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.menu.setObjectName("menu")
        self.Cadastros = QtWidgets.QWidget()
        self.Cadastros.setObjectName("Cadastros")
        self.frame = QtWidgets.QFrame(self.Cadastros)
        self.frame.setGeometry(QtCore.QRect(0, 0, 411, 281))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.button_Cadastrar_livro = QtWidgets.QPushButton(self.frame)
        self.button_Cadastrar_livro.setGeometry(QtCore.QRect(300, 60, 85, 27))
        self.button_Cadastrar_livro.setObjectName("button_Cadastrar_livro")
        self.button_Cancelar = QtWidgets.QPushButton(self.frame)
        self.button_Cancelar.setGeometry(QtCore.QRect(20, 240, 85, 27))
        self.button_Cancelar.setObjectName("button_Cancelar")
        self.label_nome_livros = QtWidgets.QLabel(self.frame)
        self.label_nome_livros.setGeometry(QtCore.QRect(20, 40, 54, 17))
        self.label_nome_livros.setObjectName("label_nome_livros")
        self.label_quatidade_livros = QtWidgets.QLabel(self.frame)
        self.label_quatidade_livros.setGeometry(QtCore.QRect(160, 40, 71, 17))
        self.label_quatidade_livros.setObjectName("label_quatidade_livros")
        self.editText_nome_livros = QtWidgets.QLineEdit(self.frame)
        self.editText_nome_livros.setGeometry(QtCore.QRect(20, 60, 113, 29))
        self.editText_nome_livros.setObjectName("editText_nome_livros")
        self.editText_quantidade_livros = QtWidgets.QLineEdit(self.frame)
        self.editText_quantidade_livros.setGeometry(QtCore.QRect(150, 60, 113, 29))
        self.editText_quantidade_livros.setObjectName("editText_quantidade_livros")
        self.Label_Livros = QtWidgets.QLabel(self.frame)
        self.Label_Livros.setGeometry(QtCore.QRect(10, 10, 111, 17))
        self.Label_Livros.setObjectName("Label_Livros")
        self.label_Usuarios = QtWidgets.QLabel(self.frame)
        self.label_Usuarios.setGeometry(QtCore.QRect(10, 100, 131, 17))
        self.label_Usuarios.setObjectName("label_Usuarios")
        self.editText_nome_usuario = QtWidgets.QLineEdit(self.frame)
        self.editText_nome_usuario.setGeometry(QtCore.QRect(20, 150, 113, 29))
        self.editText_nome_usuario.setObjectName("editText_nome_usuario")
        self.label_nome_usuarios = QtWidgets.QLabel(self.frame)
        self.label_nome_usuarios.setGeometry(QtCore.QRect(20, 130, 54, 17))
        self.label_nome_usuarios.setObjectName("label_nome_usuarios")
        self.label_cpf = QtWidgets.QLabel(self.frame)
        self.label_cpf.setGeometry(QtCore.QRect(160, 130, 54, 17))
        self.label_cpf.setObjectName("label_cpf")
        self.editText_cpf_usuario = QtWidgets.QLineEdit(self.frame)
        self.editText_cpf_usuario.setGeometry(QtCore.QRect(150, 150, 113, 29))
        self.editText_cpf_usuario.setObjectName("editText_cpf_usuario")
        self.button_Cadastrar_usuario = QtWidgets.QPushButton(self.frame)
        self.button_Cadastrar_usuario.setGeometry(QtCore.QRect(300, 150, 85, 27))
        self.button_Cadastrar_usuario.setObjectName("button_Cadastrar_usuario")
        self.menu.addTab(self.Cadastros, "")
        self.Biblioteca = QtWidgets.QWidget()
        self.Biblioteca.setObjectName("Biblioteca")
        self.frame_2 = QtWidgets.QFrame(self.Biblioteca)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 411, 281))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.button_Cancelar_2 = QtWidgets.QPushButton(self.frame_2)
        self.button_Cancelar_2.setGeometry(QtCore.QRect(10, 240, 85, 27))
        self.button_Cancelar_2.setObjectName("button_Cancelar_2")
        self.editText_buscar_usuario = QtWidgets.QLineEdit(self.frame_2)
        self.editText_buscar_usuario.setGeometry(QtCore.QRect(290, 0, 113, 29))
        self.editText_buscar_usuario.setObjectName("editText_buscar_usuario")
        self.textView_Nome_usuario = QtWidgets.QLabel(self.frame_2)
        self.textView_Nome_usuario.setGeometry(QtCore.QRect(10, 10, 54, 17))
        self.textView_Nome_usuario.setObjectName("textView_Nome_usuario")
        self.textView_nome_Livro = QtWidgets.QLabel(self.frame_2)
        self.textView_nome_Livro.setGeometry(QtCore.QRect(10, 110, 54, 17))
        self.textView_nome_Livro.setObjectName("textView_nome_Livro")
        self.editText_buscar_livro = QtWidgets.QLineEdit(self.frame_2)
        self.editText_buscar_livro.setGeometry(QtCore.QRect(290, 100, 113, 29))
        self.editText_buscar_livro.setObjectName("editText_buscar_livro")
        self.button_buscar_usuario = QtWidgets.QPushButton(self.frame_2)
        self.button_buscar_usuario.setGeometry(QtCore.QRect(320, 30, 85, 27))
        self.button_buscar_usuario.setObjectName("button_buscar_usuario")
        self.button_buscar_livro = QtWidgets.QPushButton(self.frame_2)
        self.button_buscar_livro.setGeometry(QtCore.QRect(320, 130, 85, 27))
        self.button_buscar_livro.setObjectName("button_buscar_livro")
        self.textView_isDisponivel = QtWidgets.QLabel(self.frame_2)
        self.textView_isDisponivel.setGeometry(QtCore.QRect(150, 110, 111, 17))
        self.textView_isDisponivel.setObjectName("textView_isDisponivel")
        self.label_quantidade = QtWidgets.QLabel(self.frame_2)
        self.label_quantidade.setGeometry(QtCore.QRect(10, 140, 81, 17))
        self.label_quantidade.setTextFormat(QtCore.Qt.RichText)
        self.label_quantidade.setObjectName("label_quantidade")
        self.textView_Quantidade = QtWidgets.QLabel(self.frame_2)
        self.textView_Quantidade.setGeometry(QtCore.QRect(110, 140, 54, 17))
        self.textView_Quantidade.setObjectName("textView_Quantidade")
        self.button_devolver = QtWidgets.QPushButton(self.frame_2)
        self.button_devolver.setGeometry(QtCore.QRect(120, 240, 85, 27))
        self.button_devolver.setObjectName("button_devolver")
        self.button_reservar = QtWidgets.QPushButton(self.frame_2)
        self.button_reservar.setGeometry(QtCore.QRect(220, 240, 85, 27))
        self.button_reservar.setObjectName("button_reservar")
        self.button_alugar = QtWidgets.QPushButton(self.frame_2)
        self.button_alugar.setGeometry(QtCore.QRect(320, 240, 85, 27))
        self.button_alugar.setObjectName("button_alugar")
        self.list_Alugados = QtWidgets.QListView(self.frame_2)
        self.list_Alugados.setGeometry(QtCore.QRect(10, 30, 281, 51))
        self.list_Alugados.setFlow(QtWidgets.QListView.LeftToRight)
        self.list_Alugados.setObjectName("list_Alugados")
        self.list_Alugou = QtWidgets.QListView(self.frame_2)
        self.list_Alugou.setGeometry(QtCore.QRect(10, 170, 381, 51))
        self.list_Alugou.setFlow(QtWidgets.QListView.LeftToRight)
        self.list_Alugou.setObjectName("list_Alugou")
        self.menu.addTab(self.Biblioteca, "")
        self.verticalLayout.addWidget(self.menu)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.menu.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_Cadastrar_livro.setText(_translate("MainWindow", "Cadastrar"))
        self.button_Cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.label_nome_livros.setText(_translate("MainWindow", "Nome"))
        self.label_quatidade_livros.setText(_translate("MainWindow", "Quantidade"))
        self.Label_Livros.setText(_translate("MainWindow", "Cadastro De Livros"))
        self.label_Usuarios.setText(_translate("MainWindow", "Cadastro De Usuarios"))
        self.label_nome_usuarios.setText(_translate("MainWindow", "Nome"))
        self.label_cpf.setText(_translate("MainWindow", "CPF"))
        self.button_Cadastrar_usuario.setText(_translate("MainWindow", "Cadastrar"))
        self.menu.setTabText(self.menu.indexOf(self.Cadastros), _translate("MainWindow", "Cadastros"))
        self.button_Cancelar_2.setText(_translate("MainWindow", "Cancelar"))
        self.textView_Nome_usuario.setText(_translate("MainWindow", "Usuario"))
        self.textView_nome_Livro.setText(_translate("MainWindow", "Livro"))
        self.button_buscar_usuario.setText(_translate("MainWindow", "Buscar"))
        self.button_buscar_livro.setText(_translate("MainWindow", "Buscar"))
        self.textView_isDisponivel.setText(_translate("MainWindow", "Disponivel"))
        self.label_quantidade.setText(_translate("MainWindow", "Quantidade:"))
        self.textView_Quantidade.setText(_translate("MainWindow", "numeros"))
        self.button_devolver.setText(_translate("MainWindow", "Devolver"))
        self.button_reservar.setText(_translate("MainWindow", "Reservar"))
        self.button_alugar.setText(_translate("MainWindow", "Alugar"))
        self.menu.setTabText(self.menu.indexOf(self.Biblioteca), _translate("MainWindow", "Biblioteca"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())