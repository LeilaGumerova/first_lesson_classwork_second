from first import *


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = New()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
