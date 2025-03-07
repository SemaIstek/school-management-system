# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/onur/Documents/GitHub/school-management-system/Teacher_UI/teacher.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 741)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("background-color: rgb(187, 62, 3);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 1031, 911))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background-color: rgb(0, 95, 115);\n"
"border-color: rgb(148, 210, 189);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.teacher_main = QtWidgets.QWidget()
        self.teacher_main.setObjectName("teacher_main")
        self.teacher_main_name = QtWidgets.QLabel(self.teacher_main)
        self.teacher_main_name.setGeometry(QtCore.QRect(40, 20, 401, 50))
        self.teacher_main_name.setMinimumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.teacher_main_name.setFont(font)
        self.teacher_main_name.setStyleSheet("color: rgb(238, 155, 0);")
        self.teacher_main_name.setObjectName("teacher_main_name")
        self.teacher_main_date = QtWidgets.QLabel(self.teacher_main)
        self.teacher_main_date.setGeometry(QtCore.QRect(680, 20, 250, 50))
        self.teacher_main_date.setMinimumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.teacher_main_date.setFont(font)
        self.teacher_main_date.setStyleSheet("color: rgb(238, 155, 0);")
        self.teacher_main_date.setObjectName("teacher_main_date")
        self.label_main_announcements = QtWidgets.QLabel(self.teacher_main)
        self.label_main_announcements.setGeometry(QtCore.QRect(30, 80, 200, 40))
        self.label_main_announcements.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_main_announcements.setFont(font)
        self.label_main_announcements.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_main_announcements.setObjectName("label_main_announcements")
        self.teacher_singout_button = QtWidgets.QPushButton(self.teacher_main)
        self.teacher_singout_button.setGeometry(QtCore.QRect(810, 550, 200, 100))
        self.teacher_singout_button.setMinimumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.teacher_singout_button.setFont(font)
        self.teacher_singout_button.setStyleSheet("color: rgb(238, 155, 0);")
        self.teacher_singout_button.setObjectName("teacher_singout_button")
        self.announcement_textbrowser = QtWidgets.QTextBrowser(self.teacher_main)
        self.announcement_textbrowser.setGeometry(QtCore.QRect(20, 120, 651, 192))
        self.announcement_textbrowser.setObjectName("announcement_textbrowser")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.teacher_main)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 330, 642, 80))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.annuncement_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.annuncement_label.setObjectName("annuncement_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.annuncement_label)
        self.announcement_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.announcement_lineEdit.setMinimumSize(QtCore.QSize(500, 50))
        self.announcement_lineEdit.setText("")
        self.announcement_lineEdit.setObjectName("announcement_lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.announcement_lineEdit)
        self.create_announcement_button = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.create_announcement_button.setObjectName("create_announcement_button")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.create_announcement_button)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.teacher_main)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(20, 440, 641, 80))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.announcement_to_delete_combobox = QtWidgets.QComboBox(self.formLayoutWidget_3)
        self.announcement_to_delete_combobox.setObjectName("announcement_to_delete_combobox")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.announcement_to_delete_combobox)
        self.label = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.delete_announcement_button = QtWidgets.QPushButton(self.formLayoutWidget_3)
        self.delete_announcement_button.setObjectName("delete_announcement_button")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.delete_announcement_button)
        self.tabWidget.addTab(self.teacher_main, "")
        self.teacher_profile = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(17)
        self.teacher_profile.setFont(font)
        self.teacher_profile.setObjectName("teacher_profile")
        self.label_profile_name = QtWidgets.QLabel(self.teacher_profile)
        self.label_profile_name.setGeometry(QtCore.QRect(40, 39, 200, 51))
        self.label_profile_name.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_profile_name.setFont(font)
        self.label_profile_name.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_profile_name.setObjectName("label_profile_name")
        self.label_profile_surname = QtWidgets.QLabel(self.teacher_profile)
        self.label_profile_surname.setGeometry(QtCore.QRect(40, 100, 200, 50))
        self.label_profile_surname.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_profile_surname.setFont(font)
        self.label_profile_surname.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_profile_surname.setObjectName("label_profile_surname")
        self.label_profile_birth = QtWidgets.QLabel(self.teacher_profile)
        self.label_profile_birth.setGeometry(QtCore.QRect(40, 170, 200, 50))
        self.label_profile_birth.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_profile_birth.setFont(font)
        self.label_profile_birth.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_profile_birth.setObjectName("label_profile_birth")
        self.label_profile_mail = QtWidgets.QLabel(self.teacher_profile)
        self.label_profile_mail.setGeometry(QtCore.QRect(40, 230, 200, 50))
        self.label_profile_mail.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_profile_mail.setFont(font)
        self.label_profile_mail.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_profile_mail.setObjectName("label_profile_mail")
        self.label_profile_city = QtWidgets.QLabel(self.teacher_profile)
        self.label_profile_city.setGeometry(QtCore.QRect(40, 290, 200, 50))
        self.label_profile_city.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_profile_city.setFont(font)
        self.label_profile_city.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_profile_city.setObjectName("label_profile_city")
        self.label_profile_tel = QtWidgets.QLabel(self.teacher_profile)
        self.label_profile_tel.setGeometry(QtCore.QRect(40, 340, 200, 50))
        self.label_profile_tel.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_profile_tel.setFont(font)
        self.label_profile_tel.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_profile_tel.setObjectName("label_profile_tel")
        self.teacher_profil_name_edit = QtWidgets.QTextEdit(self.teacher_profile)
        self.teacher_profil_name_edit.setGeometry(QtCore.QRect(260, 30, 321, 50))
        self.teacher_profil_name_edit.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.teacher_profil_name_edit.setFont(font)
        self.teacher_profil_name_edit.setStyleSheet("color: rgb(238, 155, 0);")
        self.teacher_profil_name_edit.setReadOnly(True)
        self.teacher_profil_name_edit.setOverwriteMode(False)
        self.teacher_profil_name_edit.setObjectName("teacher_profil_name_edit")
        self.teahcer_profil_surname_edit = QtWidgets.QTextEdit(self.teacher_profile)
        self.teahcer_profil_surname_edit.setGeometry(QtCore.QRect(260, 90, 321, 50))
        self.teahcer_profil_surname_edit.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.teahcer_profil_surname_edit.setFont(font)
        self.teahcer_profil_surname_edit.setStyleSheet("color: rgb(238, 155, 0);")
        self.teahcer_profil_surname_edit.setReadOnly(True)
        self.teahcer_profil_surname_edit.setOverwriteMode(False)
        self.teahcer_profil_surname_edit.setObjectName("teahcer_profil_surname_edit")
        self.teacher_profil_birth_edit = QtWidgets.QTextEdit(self.teacher_profile)
        self.teacher_profil_birth_edit.setGeometry(QtCore.QRect(260, 160, 321, 50))
        self.teacher_profil_birth_edit.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.teacher_profil_birth_edit.setFont(font)
        self.teacher_profil_birth_edit.setStyleSheet("color: rgb(238, 155, 0);")
        self.teacher_profil_birth_edit.setReadOnly(True)
        self.teacher_profil_birth_edit.setOverwriteMode(False)
        self.teacher_profil_birth_edit.setObjectName("teacher_profil_birth_edit")
        self.teacher_profil_mail_edit = QtWidgets.QTextEdit(self.teacher_profile)
        self.teacher_profil_mail_edit.setGeometry(QtCore.QRect(260, 220, 321, 50))
        self.teacher_profil_mail_edit.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.teacher_profil_mail_edit.setFont(font)
        self.teacher_profil_mail_edit.setStyleSheet("color: rgb(238, 155, 0);")
        self.teacher_profil_mail_edit.setReadOnly(True)
        self.teacher_profil_mail_edit.setOverwriteMode(False)
        self.teacher_profil_mail_edit.setObjectName("teacher_profil_mail_edit")
        self.teacher_profil_city_edit = QtWidgets.QTextEdit(self.teacher_profile)
        self.teacher_profil_city_edit.setGeometry(QtCore.QRect(260, 280, 321, 50))
        self.teacher_profil_city_edit.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.teacher_profil_city_edit.setFont(font)
        self.teacher_profil_city_edit.setStyleSheet("color: rgb(238, 155, 0);")
        self.teacher_profil_city_edit.setReadOnly(False)
        self.teacher_profil_city_edit.setOverwriteMode(False)
        self.teacher_profil_city_edit.setObjectName("teacher_profil_city_edit")
        self.teacher_profil_tel_edit = QtWidgets.QTextEdit(self.teacher_profile)
        self.teacher_profil_tel_edit.setGeometry(QtCore.QRect(260, 340, 321, 50))
        self.teacher_profil_tel_edit.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.teacher_profil_tel_edit.setFont(font)
        self.teacher_profil_tel_edit.setStyleSheet("color: rgb(238, 155, 0);")
        self.teacher_profil_tel_edit.setReadOnly(False)
        self.teacher_profil_tel_edit.setOverwriteMode(False)
        self.teacher_profil_tel_edit.setObjectName("teacher_profil_tel_edit")
        self.tabWidget.addTab(self.teacher_profile, "")
        self.teacher_plan = QtWidgets.QWidget()
        self.teacher_plan.setObjectName("teacher_plan")
        self.label_plan_lesson = QtWidgets.QLabel(self.teacher_plan)
        self.label_plan_lesson.setGeometry(QtCore.QRect(40, 30, 200, 50))
        self.label_plan_lesson.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_plan_lesson.setFont(font)
        self.label_plan_lesson.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_plan_lesson.setObjectName("label_plan_lesson")
        self.label_plan_mentor = QtWidgets.QLabel(self.teacher_plan)
        self.label_plan_mentor.setGeometry(QtCore.QRect(540, 30, 300, 50))
        self.label_plan_mentor.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_plan_mentor.setFont(font)
        self.label_plan_mentor.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_plan_mentor.setObjectName("label_plan_mentor")
        self.teacher_plan_lesson = QtWidgets.QTableWidget(self.teacher_plan)
        self.teacher_plan_lesson.setGeometry(QtCore.QRect(30, 80, 441, 481))
        self.teacher_plan_lesson.setObjectName("teacher_plan_lesson")
        self.teacher_plan_lesson.setColumnCount(0)
        self.teacher_plan_lesson.setRowCount(0)
        self.teacher_plan_mentoring = QtWidgets.QTableWidget(self.teacher_plan)
        self.teacher_plan_mentoring.setGeometry(QtCore.QRect(530, 80, 461, 481))
        self.teacher_plan_mentoring.setObjectName("teacher_plan_mentoring")
        self.teacher_plan_mentoring.setColumnCount(0)
        self.teacher_plan_mentoring.setRowCount(0)
        self.create_lesson = QtWidgets.QPushButton(self.teacher_plan)
        self.create_lesson.setGeometry(QtCore.QRect(70, 600, 131, 28))
        self.create_lesson.setObjectName("create_lesson")
        self.create_mentor = QtWidgets.QPushButton(self.teacher_plan)
        self.create_mentor.setGeometry(QtCore.QRect(540, 600, 141, 28))
        self.create_mentor.setObjectName("create_mentor")
        self.update_lessons = QtWidgets.QPushButton(self.teacher_plan)
        self.update_lessons.setGeometry(QtCore.QRect(230, 600, 93, 28))
        self.update_lessons.setObjectName("update_lessons")
        self.update_mentoring = QtWidgets.QPushButton(self.teacher_plan)
        self.update_mentoring.setGeometry(QtCore.QRect(710, 600, 121, 28))
        self.update_mentoring.setObjectName("update_mentoring")
        self.tabWidget.addTab(self.teacher_plan, "")
        self.teacher_to_do = QtWidgets.QWidget()
        self.teacher_to_do.setObjectName("teacher_to_do")
        self.tasks_tableWidget = QtWidgets.QTableWidget(self.teacher_to_do)
        self.tasks_tableWidget.setGeometry(QtCore.QRect(70, 230, 891, 192))
        self.tasks_tableWidget.setObjectName("tasks_tableWidget")
        self.tasks_tableWidget.setColumnCount(0)
        self.tasks_tableWidget.setRowCount(0)
        self.layoutWidget = QtWidgets.QWidget(self.teacher_to_do)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 50, 331, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.create_task_form_layout = QtWidgets.QFormLayout(self.layoutWidget)
        self.create_task_form_layout.setContentsMargins(0, 0, 0, 0)
        self.create_task_form_layout.setObjectName("create_task_form_layout")
        self.task_name_label = QtWidgets.QLabel(self.layoutWidget)
        self.task_name_label.setStyleSheet("")
        self.task_name_label.setObjectName("task_name_label")
        self.create_task_form_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.task_name_label)
        self.task_name_input = QtWidgets.QLineEdit(self.layoutWidget)
        self.task_name_input.setObjectName("task_name_input")
        self.create_task_form_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.task_name_input)
        self.assignee_label = QtWidgets.QLabel(self.layoutWidget)
        self.assignee_label.setObjectName("assignee_label")
        self.create_task_form_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.assignee_label)
        self.assignee_input_combo = QtWidgets.QComboBox(self.layoutWidget)
        self.assignee_input_combo.setObjectName("assignee_input_combo")
        self.create_task_form_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.assignee_input_combo)
        self.due_date_label = QtWidgets.QLabel(self.layoutWidget)
        self.due_date_label.setObjectName("due_date_label")
        self.create_task_form_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.due_date_label)
        self.due_date_input = QtWidgets.QDateEdit(self.layoutWidget)
        self.due_date_input.setMinimumDate(QtCore.QDate(2023, 1, 1))
        self.due_date_input.setCalendarPopup(True)
        self.due_date_input.setObjectName("due_date_input")
        self.create_task_form_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.due_date_input)
        self.create_task_button = QtWidgets.QPushButton(self.layoutWidget)
        self.create_task_button.setObjectName("create_task_button")
        self.create_task_form_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.create_task_button)
        self.tabWidget.addTab(self.teacher_to_do, "")
        self.teacher_attendance = QtWidgets.QWidget()
        self.teacher_attendance.setObjectName("teacher_attendance")
        self.label_lesson_status = QtWidgets.QLabel(self.teacher_attendance)
        self.label_lesson_status.setGeometry(QtCore.QRect(40, 30, 400, 50))
        self.label_lesson_status.setMinimumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_lesson_status.setFont(font)
        self.label_lesson_status.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_lesson_status.setObjectName("label_lesson_status")
        self.label_mentor_status = QtWidgets.QLabel(self.teacher_attendance)
        self.label_mentor_status.setGeometry(QtCore.QRect(540, 21, 480, 50))
        self.label_mentor_status.setMinimumSize(QtCore.QSize(480, 50))
        self.label_mentor_status.setMaximumSize(QtCore.QSize(480, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_mentor_status.setFont(font)
        self.label_mentor_status.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_mentor_status.setObjectName("label_mentor_status")
        self.teacher_attendance_lesson = QtWidgets.QTableWidget(self.teacher_attendance)
        self.teacher_attendance_lesson.setGeometry(QtCore.QRect(30, 90, 481, 511))
        self.teacher_attendance_lesson.setObjectName("teacher_attendance_lesson")
        self.teacher_attendance_lesson.setColumnCount(0)
        self.teacher_attendance_lesson.setRowCount(0)
        self.tableWidget = QtWidgets.QTableWidget(self.teacher_attendance)
        self.tableWidget.setGeometry(QtCore.QRect(560, 90, 401, 511))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tabWidget.addTab(self.teacher_attendance, "")
        self.student_dance = QtWidgets.QWidget()
        self.student_dance.setObjectName("student_dance")
        self.chat_list = QtWidgets.QComboBox(self.student_dance)
        self.chat_list.setGeometry(QtCore.QRect(30, 30, 230, 50))
        self.chat_list.setMinimumSize(QtCore.QSize(230, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chat_list.setFont(font)
        self.chat_list.setStyleSheet("color: rgb(238, 155, 0);")
        self.chat_list.setObjectName("chat_list")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.chat_list.addItem("")
        self.teacher_chat_message_panel = QtWidgets.QTextEdit(self.student_dance)
        self.teacher_chat_message_panel.setGeometry(QtCore.QRect(290, 70, 700, 421))
        self.teacher_chat_message_panel.setMinimumSize(QtCore.QSize(700, 0))
        self.teacher_chat_message_panel.setMaximumSize(QtCore.QSize(700, 16777215))
        self.teacher_chat_message_panel.setStyleSheet("background-color: rgb(233, 216, 166);")
        self.teacher_chat_message_panel.setObjectName("teacher_chat_message_panel")
        self.teacher_chat_message = QtWidgets.QTextEdit(self.student_dance)
        self.teacher_chat_message.setGeometry(QtCore.QRect(290, 530, 700, 100))
        self.teacher_chat_message.setMinimumSize(QtCore.QSize(700, 100))
        self.teacher_chat_message.setMaximumSize(QtCore.QSize(700, 100))
        self.teacher_chat_message.setStyleSheet("background-color: rgb(233, 216, 166);")
        self.teacher_chat_message.setObjectName("teacher_chat_message")
        self.teacher_chat_send_button = QtWidgets.QPushButton(self.student_dance)
        self.teacher_chat_send_button.setGeometry(QtCore.QRect(50, 530, 200, 100))
        self.teacher_chat_send_button.setMinimumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.teacher_chat_send_button.setFont(font)
        self.teacher_chat_send_button.setStyleSheet("color: rgb(238, 155, 0);\n"
"background-color: rgb(148, 210, 189);")
        self.teacher_chat_send_button.setObjectName("teacher_chat_send_button")
        self.tabWidget.addTab(self.student_dance, "")
        self.admin_page = QtWidgets.QWidget()
        self.admin_page.setObjectName("admin_page")
        self.formLayoutWidget = QtWidgets.QWidget(self.admin_page)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 50, 360, 501))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_profile_birth_admin = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_profile_birth_admin.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_profile_birth_admin.setFont(font)
        self.label_profile_birth_admin.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_profile_birth_admin.setObjectName("label_profile_birth_admin")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_profile_birth_admin)
        self.label_profile_city_admin = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_profile_city_admin.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_profile_city_admin.setFont(font)
        self.label_profile_city_admin.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_profile_city_admin.setObjectName("label_profile_city_admin")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_profile_city_admin)
        self.label_profile_name_admin = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_profile_name_admin.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_profile_name_admin.setFont(font)
        self.label_profile_name_admin.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_profile_name_admin.setObjectName("label_profile_name_admin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_profile_name_admin)
        self.label_profile_surname_admin = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_profile_surname_admin.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_profile_surname_admin.setFont(font)
        self.label_profile_surname_admin.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_profile_surname_admin.setObjectName("label_profile_surname_admin")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_profile_surname_admin)
        self.label_profile_mail_admin = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_profile_mail_admin.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_profile_mail_admin.setFont(font)
        self.label_profile_mail_admin.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_profile_mail_admin.setObjectName("label_profile_mail_admin")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_profile_mail_admin)
        self.label_profile_tel_admin = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_profile_tel_admin.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_profile_tel_admin.setFont(font)
        self.label_profile_tel_admin.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_profile_tel_admin.setObjectName("label_profile_tel_admin")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_profile_tel_admin)
        self.label_profile_birth_admin_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_profile_birth_admin_2.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_profile_birth_admin_2.setFont(font)
        self.label_profile_birth_admin_2.setStyleSheet("color: rgb(238, 155, 0);")
        self.label_profile_birth_admin_2.setObjectName("label_profile_birth_admin_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_profile_birth_admin_2)
        self.teacher_name_admin = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.teacher_name_admin.setObjectName("teacher_name_admin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.teacher_name_admin)
        self.teache_surname_admin = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.teache_surname_admin.setObjectName("teache_surname_admin")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.teache_surname_admin)
        self.teacher_email_admin = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.teacher_email_admin.setObjectName("teacher_email_admin")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.teacher_email_admin)
        self.teacher_password_admin = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.teacher_password_admin.setObjectName("teacher_password_admin")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.teacher_password_admin)
        self.teacher_birthdate_admin = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.teacher_birthdate_admin.setObjectName("teacher_birthdate_admin")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.teacher_birthdate_admin)
        self.teacher_city_admin = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.teacher_city_admin.setObjectName("teacher_city_admin")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.teacher_city_admin)
        self.teacher_tel_admin = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.teacher_tel_admin.setObjectName("teacher_tel_admin")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.teacher_tel_admin)
        self.create_teacher_account_button = QtWidgets.QPushButton(self.formLayoutWidget)
        self.create_teacher_account_button.setObjectName("create_teacher_account_button")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.create_teacher_account_button)
        self.tabWidget.addTab(self.admin_page, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.teacher_main_name.setText(_translate("MainWindow", "HOŞGELDİN AHMET"))
        self.teacher_main_date.setText(_translate("MainWindow", "26/12/2023"))
        self.label_main_announcements.setText(_translate("MainWindow", "Announcements"))
        self.teacher_singout_button.setText(_translate("MainWindow", "Sing Out"))
        self.annuncement_label.setText(_translate("MainWindow", "Announcement Text"))
        self.announcement_lineEdit.setPlaceholderText(_translate("MainWindow", "Your announcement"))
        self.create_announcement_button.setText(_translate("MainWindow", "Create Announcement"))
        self.label.setText(_translate("MainWindow", "Select Announcement"))
        self.delete_announcement_button.setText(_translate("MainWindow", "Delete Announcement"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.teacher_main), _translate("MainWindow", "Main"))
        self.label_profile_name.setText(_translate("MainWindow", "Name :"))
        self.label_profile_surname.setText(_translate("MainWindow", "Surname :"))
        self.label_profile_birth.setText(_translate("MainWindow", "Date of Birth :"))
        self.label_profile_mail.setText(_translate("MainWindow", "E-Mail :"))
        self.label_profile_city.setText(_translate("MainWindow", "City :"))
        self.label_profile_tel.setText(_translate("MainWindow", "Tel :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.teacher_profile), _translate("MainWindow", "Profile"))
        self.label_plan_lesson.setText(_translate("MainWindow", "Lesson Plan"))
        self.label_plan_mentor.setText(_translate("MainWindow", "Mentor Meeting Plan"))
        self.create_lesson.setText(_translate("MainWindow", "Lesson create/edit"))
        self.create_mentor.setText(_translate("MainWindow", "Mentoring create/edit"))
        self.update_lessons.setText(_translate("MainWindow", "Lesson refresh"))
        self.update_mentoring.setText(_translate("MainWindow", "Mentoring refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.teacher_plan), _translate("MainWindow", "Lesson / Mentor Plan"))
        self.task_name_label.setText(_translate("MainWindow", "Task Name"))
        self.assignee_label.setText(_translate("MainWindow", "Assignee"))
        self.due_date_label.setText(_translate("MainWindow", "Due Date"))
        self.create_task_button.setText(_translate("MainWindow", "Create Task"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.teacher_to_do), _translate("MainWindow", "To do List"))
        self.label_lesson_status.setText(_translate("MainWindow", "Lesson Attendance Status"))
        self.label_mentor_status.setText(_translate("MainWindow", "Mentor Meeting Attendance Status"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.teacher_attendance), _translate("MainWindow", "Attendance Status"))
        self.chat_list.setItemText(0, _translate("MainWindow", "Please Select Person:"))
        self.chat_list.setItemText(1, _translate("MainWindow", "None"))
        self.chat_list.setItemText(2, _translate("MainWindow", "None"))
        self.chat_list.setItemText(3, _translate("MainWindow", "None"))
        self.chat_list.setItemText(4, _translate("MainWindow", "None"))
        self.chat_list.setItemText(5, _translate("MainWindow", "None"))
        self.chat_list.setItemText(6, _translate("MainWindow", "None"))
        self.chat_list.setItemText(7, _translate("MainWindow", "None"))
        self.chat_list.setItemText(8, _translate("MainWindow", "None"))
        self.chat_list.setItemText(9, _translate("MainWindow", "None"))
        self.chat_list.setItemText(10, _translate("MainWindow", "None"))
        self.teacher_chat_send_button.setText(_translate("MainWindow", "SEND"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.student_dance), _translate("MainWindow", "Chat"))
        self.label_profile_birth_admin.setText(_translate("MainWindow", "Date of Birth :"))
        self.label_profile_city_admin.setText(_translate("MainWindow", "City :"))
        self.label_profile_name_admin.setText(_translate("MainWindow", "Name :"))
        self.label_profile_surname_admin.setText(_translate("MainWindow", "Surname :"))
        self.label_profile_mail_admin.setText(_translate("MainWindow", "E-Mail :"))
        self.label_profile_tel_admin.setText(_translate("MainWindow", "Tel :"))
        self.label_profile_birth_admin_2.setText(_translate("MainWindow", "Password"))
        self.create_teacher_account_button.setText(_translate("MainWindow", "Create Teacher Account"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.admin_page), _translate("MainWindow", "Admin"))
