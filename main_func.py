# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QVBoxLayout,QListWidgetItem,QDesktopWidget,QMessageBox
from PyQt5.QtGui import  QPixmap
from PyQt5.QtCore import  QSize
from mainwindow import Ui_MainWindow
import animals_1_func
import chinese_ocr_func
import yolov3_resnet50_func
import stylepro_artistic_func
import stgan_bald_func
import mask_func
import deoldify_func
import humanseg_func

import json
class QmyMainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_MainWindow()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面
        self.website={
            'logo_url':"https://aistudio.baidu.com/aistudio/index",
            'project_url':"https://aistudio.baidu.com/aistudio/projectoverview/public",
            'dataset_url':'https://aistudio.baidu.com/aistudio/datasetoverview',
            'course_url':'https://aistudio.baidu.com/aistudio/course',
            'competition_url':'https://aistudio.baidu.com/aistudio/competition',
            'auth_url':'https://aistudio.baidu.com/aistudio/certification',
            'community_url':'https://ai.baidu.com/forum/topic/list/192',
            'ppweb_url':'https://www.paddlepaddle.org.cn/'
        }
        self.url_prefix = 'https://aistudio.baidu.com/aistudio/personalcenter/thirdview/'
        # login_ui=login_func.login_UI()
        # self.userId=login_ui.display_signal.connect(self.getuserid)
        self.video_url=[]
        self.center()
        self.link_connect()
        self.action_connect()


    ##  ==============自定义功能函数========================
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()+200) / 2)
    def link_connect(self):
        # 定义链接动作
        self.ui.pushButton_logo.clicked.connect(self.open_logo)
        self.ui.pushButton_project.clicked.connect(self.open_project)
        self.ui.pushButton_dataset.clicked.connect(self.open_dataset)
        self.ui.pushButton_course.clicked.connect(self.open_course)
        self.ui.pushButton_competition.clicked.connect(self.open_competition)
        self.ui.pushButton_auth.clicked.connect(self.open_auth)
        self.ui.pushButton_community.clicked.connect(self.open_community)
        self.ui.pushButton_ppweb.clicked.connect(self.open_ppweb)


    def action_connect(self):
        self.ui.image_generation.clicked.connect(self.show_animals_1)
        self.ui.image_generation_2.clicked.connect(self.show_chinese_ocr)
        self.ui.image_generation_3.clicked.connect(self.show_yolov3_resnet50)
        self.ui.image_generation_4.clicked.connect(self.show_stylepro_artistic)
        self.ui.image_generation_5.clicked.connect(self.show_stgan_bald)
        self.ui.image_generation_6.clicked.connect(self.show_mask)
        self.ui.image_generation_7.clicked.connect(self.show_photo_restoration_func)
        self.ui.image_generation_8.clicked.connect(self.show_humanseg)

    def open_logo(self):
        self.open_browser(self.website.get('logo_url'))
    def open_project(self):
        self.open_browser(self.website.get('project_url'))
    def open_dataset(self):
        self.open_browser(self.website.get('dataset_url'))
    def open_course(self):
        self.open_browser(self.website.get('course_url'))
    def open_competition(self):
        self.open_browser(self.website.get('competition_url'))
    def open_auth(self):
        self.open_browser(self.website.get('auth_url'))
    def open_community(self):
        self.open_browser(self.website.get('community_url'))
    def open_ppweb(self):
        self.open_browser(self.website.get('ppweb_url'))

    def open_browser(self,url):
        from PyQt5.QtCore import QUrl
        from PyQt5.QtGui import QDesktopServices
        QDesktopServices.openUrl(QUrl(url))

    def refresh_portrait(self,url):
        print("更新精灵图")
        import requests
        res=requests.get(url)
        imgPath='./images/1.jpg'
        with open(imgPath, 'wb') as f:
            f.write(res.content)
        return imgPath

    def show_animals_1(self):
        self.ui = animals_1_func.QmyMainWindow1()  # 创建窗体
        self.ui.show()
        self.hide()
    def show_chinese_ocr(self):
        self.ui = chinese_ocr_func.QmyMainWindow1()  # 创建窗体
        self.ui.show()
        self.hide()
    def show_yolov3_resnet50(self):
        self.ui = yolov3_resnet50_func.QmyMainWindow1()  # 创建窗体
        self.ui.show()
        self.hide()
    def show_stylepro_artistic(self):
        self.ui =stylepro_artistic_func.QmyMainWindow1()  # 创建窗体
        self.ui.show()
        self.hide()
    def show_stgan_bald(self):
        self.ui = stgan_bald_func.QmyMainWindow1()  # 创建窗体
        self.ui.show()
        self.hide()
    def show_mask(self):
        self.ui = mask_func.QmyMainWindow1()  # 创建窗体
        self.ui.show()
        self.hide()
    def show_photo_restoration_func(self):
        self.ui = deoldify_func.QmyMainWindow1()  # 创建窗体
        self.ui.show()
        self.hide()
    def show_humanseg(self):
        self.ui = humanseg_func.QmyMainWindow1()  # 创建窗体
        self.ui.show()
        self.hide()

    def closeEvent(self,event):
        # self.close()
        # 这个方法复写父类的方法'closeEvent'
        dlgTitle = "温馨提示"
        strInfo = "您确定要退出吗?"
        reply = QMessageBox.question(self, dlgTitle, strInfo, QMessageBox.Yes | QMessageBox.No)
        # 重要！提醒的内容，从左到右：self,标题,提示内容,两个提示按钮
        if reply == QMessageBox.Yes:
            # 如果用户选择Yes
            # 执行操作
            # quit()
            event.accept()
        else:
            # 如果用户选择No
            event.ignore()



##  ==============event处理函数==========================


##  ==========由connectSlotsByName()自动连接的槽函数============


##  =============自定义槽函数===============================


##  ============窗体测试程序 ================================
if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QmyMainWindow()  # 创建窗体
    form.show()
    sys.exit(app.exec_())
