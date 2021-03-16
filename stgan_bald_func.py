import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog,QWidget, QVBoxLayout, QListWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize,QDir
from PyQt5.QtWidgets import QMessageBox,QDesktopWidget
from stgan_bald import Ui_MainWindow
import main_func
from img_gen_webfunc import get_stgan_bald

class QmyMainWindow1(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_MainWindow()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面
        self.center()
        self.action_connect()
        self.filename1 = ''

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def action_connect(self):
        self.ui.pushButton_openfile.clicked.connect(self.open_file)
        self.ui.pushButton_deal.clicked.connect(self.deal_img)
        self.ui.pushButton_back.clicked.connect(self.back_home)
        self.ui.pushButton_exit.clicked.connect(self.exit_app)

    def open_file(self):
        curPath = QDir.currentPath()
        dlgTitle = "选择一张图片"
        filt = "All Files(*);;*.png;;*.jpg"
        filename1, filetype1 = QFileDialog.getOpenFileName(self, dlgTitle, curPath, filt)
        self.ui.lineEdit.setText(str(filename1))
        self.filename1 = str(filename1)

        print("Done!")

    def deal_img(self):
        if len(str(self.filename1)) > 0:
            img_path=str(self.filename1)
            # print(img_path)
            output_path=get_stgan_bald(img_path=img_path)
            if(len(str(output_path)))>0:
                dlgTitle = "温馨提示"
                strInfo = "运行结果请查看:"+str(output_path)
                QMessageBox.information(self, dlgTitle, strInfo)
                print(output_path)
            # if len(output_dir) > 0:
            #     print("Done！")
        else:
            dlgTitle = "温馨提示"
            strInfo = "请添加图片文件！"
            QMessageBox.information(self, dlgTitle, strInfo)
    def back_home(self):
        self.ui = main_func.QmyMainWindow()  # 创建窗体
        self.ui.showMaximized()
        self.ui.show()
        self.close()
    def exit_app(self,event):
        # self.close()
        # 这个方法复写父类的方法'closeEvent'
        dlgTitle = "温馨提示"
        strInfo = "您确定要退出吗?"
        reply = QMessageBox.question(self, dlgTitle, strInfo, QMessageBox.Yes | QMessageBox.No)
        # 重要！提醒的内容，从左到右：self,标题,提示内容,两个提示按钮
        if reply == QMessageBox.Yes:
            # 如果用户选择Yes
            quit()
            # 执行操作
        else:
            # 如果用户选择No
            pass

if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QmyMainWindow1()  # 创建窗体
    form.show()
    sys.exit(app.exec_())
