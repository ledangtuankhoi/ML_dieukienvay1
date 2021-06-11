from datetime import datetime
import sys
import platform
import socket
import os
import PyQt5
from PyQt5.QtWidgets import QFileDialog, QInputDialog
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
import PySide2
from PySide2.QtWidgets import QPushButton
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2 import QtCore,QtGui
import sys
from seaborn import palettes
from seaborn import widgets
from datetime import date

from fpdf import FPDF


import gui_base_old_pyuic5

#xự lý số liệu 
df = pd.read_csv('dataset_IBM/train_ctrUa4K.csv')
columnNames = pd.Series(df.columns.values) # to check the columns/variables/features present in our data set
# xóa những trường thiếu giá trị
df.dropna(axis=0, how='any', inplace=True)
df = df.drop(['Loan_ID'], axis=1)
# END xự lý số liệu 






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gui_base_old_pyuic5.Ui_MainWindow()
    ui.setupUi(MainWindow)
# end main
    # khai bao
    filename = 'null'
    
    # tao list khi xoa cac gia tri trung lap
    list_gioitinh = df["Gender"].drop_duplicates().tolist() 
    list_hocvan = df["Education"].drop_duplicates().tolist() 
    list_honnhan = df["Married"].drop_duplicates().tolist() 
    list_khuvuc = df["Property_Area"].drop_duplicates().tolist() 
    list_tukinhdoanh = df["Self_Employed"].drop_duplicates().tolist()
    list_lichsuvay = df["Credit_History"].drop_duplicates().tolist()

    # show ra man hinh console du lieu list
    print(list_gioitinh)
    print(list_hocvan)
    print(list_honnhan)
    print(list_khuvuc)
    print(list_tukinhdoanh)
    print(list_lichsuvay)

    # thêm các item vào combobox
    ui.cob_gioitinh.addItems(list_gioitinh)
    ui.cob_hocvan.addItems(list_hocvan)
    ui.cob_honnhan.addItems(list_honnhan)
    ui.cob_khuvuc.addItems(list_khuvuc)
    ui.cob_tukinhdoanh.addItems(list_tukinhdoanh)
    ui.cob_lichsuvay.addItems(['Yes','No'])
    # END thêm các item vào combobox

    
    #du lieu mau
    #Loan_ID,Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area,Decision
    # ['Male','Yes',1,'Not Graduate','No',4583,1508.0,128.0,360.0,1.0,'Rural'])
    mau = ['Male','Yes','0','Graduate','Yes','3000','0','66','360','1','Urban']
    ui.cob_gioitinh.setCurrentText(mau[0])
    ui.cob_honnhan.setCurrentText(mau[1])
    ui.txt_nguoiphuthuoc.setText(mau[2])
    ui.cob_hocvan.setCurrentText(mau[3])
    ui.cob_tukinhdoanh.setCurrentText(mau[4])
    ui.txt_thunhap.setText(mau[5])
    ui.txt_thunhapnguoithan.setText(mau[6])
    ui.txt_sotienvay.setText(mau[7])
    ui.txt_tgvay.setText(mau[8])
    if ui.cob_lichsuvay.currentText() == '1.0':
        mau[9] = 'Yes'
    else:
        mau[9] = 'No'
    ui.cob_lichsuvay.setCurrentText(mau[9])
    ui.cob_khuvuc.setCurrentText(mau[10])
    # END du lieu mau

# IMPORT CO SO DU LIEU VAO HE THONG
    def do_file(self):
        pathfile = QtWidgets.QFileDialog.getOpenFileName(caption='Open File',filter="File(*.csv)")
        filename = pathfile[0].rsplit("/",1)[1]

        # check format file


        # di chuyển file tới thu muc dataset của hệ thống
        os.rename(str(pathfile[0]), "dataset_IBM/" + filename)


        # lấy tên của file đã load
        print (pathfile[0].rsplit("/",1)[1])

# fuc xu ly thuat toan
    def click_submit(self):
        # pathfile = QtWidgets.QFileDialog.getOpenFileNames(caption='Open File',filter="File(*.csv)")
        # print('----- A-----' + str(pathfile[0][0]))
        # print('----- A-----' + str(pathfile[0][1]))

        if   ui.txt_thunhap.text() != "" and ui.txt_thunhapnguoithan.text() != "" and ui.txt_sotienvay.text() != "" and ui.txt_tgvay.text() != "" :
            print("btn_reset")
            print("nguoiphuthoc: " + ui.txt_nguoiphuthuoc.text())
            print("sotienvay: " + ui.txt_sotienvay.text())
            print("thoi gian vay: " + ui.txt_tgvay.text())
            print("thunhap: " + ui.txt_thunhap.text())
            print("thu nhap nguoi than: " + ui.txt_thunhapnguoithan.text())
            print("hocvan: " + ui.cob_hocvan.currentText())
            print("honnhan: " + ui.cob_honnhan.currentText())
            print("khuvuc: " + ui.cob_khuvuc.currentText())
            print("tukinhdoanh: " + ui.cob_tukinhdoanh.currentText())
            print("gioitinh: " + ui.cob_gioitinh.currentText())

            #chuong trinh thu hienj
            df = pd.read_csv('dataset_IBM/train_ctrUa4K.csv')
            columnNames = pd.Series(df.columns.values) # to check the columns/variables/features present in our data set
            # xóa những trường thiếu giá trị
            df.dropna(axis=0, how='any', inplace=True)
            df = df.drop(['Loan_ID'], axis=1)


            # Loan ID,
            # Gender
            # ,Married
            # ,Dependents ,             Người phụ thuộc
            # ,Education
            # ,Self Employed,
            # Applicant Income          Thu nhập của người nộp đơn
            # ,Co applicant Income      Thu nhập của người thân
            # ,Loan Amount              Số tiền vay
            # ,Loan Amount Term         Thời hạn Số tiền Khoản vay
            # ,Credit History           Lịch sử tín dụng
            # ,Property Area
            # ,Loan_Status

            
            #lay du lieu tu nguoi dung
            Gender = ui.cob_gioitinh.currentText()
            Married = ui.cob_honnhan.currentText()
            Dependents = ui.txt_nguoiphuthuoc.text()
            Education= ui.cob_hocvan.currentText()
            Self_Employed= ui.cob_tukinhdoanh.currentText()
            ApplicantIncome= float(ui.txt_thunhap.text())
            CoapplicantIncome= float(ui.txt_thunhapnguoithan.text())
            LoanAmount = float(ui.txt_sotienvay.text())
            Loan_Amount_Term = float(ui.txt_tgvay.text())
            Property_Area = ui.cob_khuvuc.currentText()
            if ui.cob_lichsuvay.currentText() == 'yes':
                Credit_History = 1
            else:
                Credit_History = 0
                

            Loan_Status = 'N'

            # thêm người cần kiểm tra vào bảng để hình thành cột giá trị 
            df.loc[len(df.index)] = [Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area,Loan_Status] 
            # xem hangf cuoi cuar bang
            print(df.loc[len(df.index)])
            #  chuyển hóa bảng thành ma trận với giá trị có trong trường
            df = pd.get_dummies(df,drop_first=True)
            print("df-----------------------------" )
            
            print(df.sample(5))
            # cắt người cần kiểm tra ra để kiểm tra 
            mau_test = df.loc[len(df.index)]
            #drop mau khoi bang train
            df = df.drop(len(df.index))
            # print(df.loc[len(df.index)])
            # chuyển sang dạng từ numaray -> dataframe 
            mau_test = pd.DataFrame(mau_test)
            # chuyển mảng dạng dọc sang dạng ngang
            mau_test = mau_test.transpose()
            print('mautest')
            # mau_test[13]
            mau_test = mau_test.drop(['Loan_Status_Y'],axis=1)
            print(mau_test)
            # gán x_test là bằng giá trị trừ Loan_Status_Y để kiểm tra độ chính xác của thuật toán
            x_test = df.drop('Loan_Status_Y', axis=1)
            # x_train là mẫu giúp cho máy học các giá trị 
            x_train = x_test
            # y_test mẫu kiểm tra lại khi chạy thuộc toán giúp so sanh kết quả
            y_test = df['Loan_Status_Y']
            # y_train là mẫu kết quả giúp cho máy học 
            y_train = y_test

            logiRe = LogisticRegression()
            logiRe.fit(x_train,y_train)
            print("score",logiRe.score(x_test,y_test))
            print("predict", logiRe.predict(mau_test))

            if logiRe.predict(mau_test) == 1:
                ui.label_status.setText('ELIGIBLE')
                ui.label_status.setStyleSheet("border: 1px solid black; background-color: #5cb85c")
                ui.label_status.setText('CHO VAY')
                
            else:
                # kết quả trả về 
                ui.label_status.setText('ELIGIBLE')
                ui.label_status.setStyleSheet("border: 1px solid black; background-color: #ba0000")
                ui.label_status.setText('KHONG CHO VAY')
                
            # set border cho label
            ui.label_desi.setText('DO CHINH XAC THUAT TOAN: ' +
            str(logiRe.score(x_test,y_test)*100) + "%" 
            +"\n"+ str(mau_test.values.tolist()))
            ui.label_desi.setStyleSheet("border: 1px solid black;")
        else:
            ui.label_status.setText('')
            print("chua nhap lieu")
            ui.label_status.setStyleSheet("border: 1px solid black; background-color: transparent")
            ui.label_desi.setText('CHUA NHAP LIEU: ')


# RESET CAC TRUONG GIA TRI
    def click_reset(self):
        print("btn_reset")
        ui.txt_thunhap.setText('')
        ui.txt_thunhapnguoithan.setText('')
        ui.txt_sotienvay.setText('')
        ui.txt_tgvay.setText('')
        ui.txt_nguoiphuthuoc.setText('')

# XUAT QUYẾT ĐỊNH RA FILE PDF
    def exportPDF(seft):
        #chuong trinh thu hienj
        df1 = pd.read_csv('dataset_IBM/train_ctrUa4K.csv')
        columnNames = pd.Series(df1.columns.values) # to check the columns/variables/features present in our data set

        # xóa những trường thiếu giá trị
        df1.dropna(axis=0, how='any', inplace=True)
        df1 = df1.drop(['Loan_ID'], axis=1)

        #lay du lieu tu nguoi dung
        Gender = ui.cob_gioitinh.currentText()
        Married = ui.cob_honnhan.currentText()
        Dependents = ui.txt_nguoiphuthuoc.text()
        Education= ui.cob_hocvan.currentText()
        Self_Employed= ui.cob_tukinhdoanh.currentText()
        ApplicantIncome= float(ui.txt_thunhap.text())
        CoapplicantIncome= float(ui.txt_thunhapnguoithan.text())
        LoanAmount = float(ui.txt_sotienvay.text())
        Loan_Amount_Term = float(ui.txt_tgvay.text())
        Property_Area = ui.cob_khuvuc.currentText()
        if ui.cob_lichsuvay.currentText() == 'yes':
            Credit_History = 1
        else:
            Credit_History = 0
            

        Loan_Status = 'N'

        # thêm người cần kiểm tra vào bảng để hình thành cột giá trị 
        df1.loc[len(df1.index)] = [Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area,Loan_Status] 
        # xem hangf cuoi cuar bang
        print(df1.loc[len(df1.index)])
        #  chuyển hóa bảng thành ma trận với giá trị có trong trường
        df1 = pd.get_dummies(df1,drop_first=True)
        print("df1-----------------------------" )
        
        print(df1.sample(5))
        # cắt người cần kiểm tra ra để kiểm tra 
        mau_test = df1.loc[len(df1.index)]
        #drop mau khoi bang train
        df1 = df1.drop(len(df1.index))
        # print(df1.loc[len(df1.index)])
        # chuyển sang dạng từ numaray -> dataframe 
        mau_test = pd.DataFrame(mau_test)
        # chuyển mảng dạng dọc sang dạng ngang
        mau_test = mau_test.transpose()
        print('mautest')
        # mau_test[13]
        mau_test = mau_test.drop(['Loan_Status_Y'],axis=1)
        print(mau_test)
        # gán x_test là bằng giá trị trừ Loan_Status_Y để kiểm tra độ chính xác của thuật toán
        x_test = df1.drop('Loan_Status_Y', axis=1)
        # x_train là mẫu giúp cho máy học các giá trị 
        x_train = x_test
        # y_test mẫu kiểm tra lại khi chạy thuộc toán giúp so sanh kết quả
        y_test = df1['Loan_Status_Y']
        # y_train là mẫu kết quả giúp cho máy học 
        y_train = y_test

        logiRe = LogisticRegression()
        logiRe.fit(x_train,y_train)
        print("score",logiRe.score(x_test,y_test))
        print("predict", logiRe.predict(mau_test))

        if logiRe.predict(mau_test) == 1:
            quyetdinh = 'CHO VAY------- YES'
            
        else:
            quyetdinh = 'KHONG CHO VAY------- NO'

        # save FPDF() class into a 
        # variable pdf
        pdf = FPDF()
        
        # Add a page
        pdf.add_page()
        
        # set style and size of font 
        # that you want in the pdf
        pdf.set_font("Arial", size = 11)
        
        # create a cell
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        today = datetime.today()
        current_today = today.strftime("%d/%m/%Y")
        print("Current Time =", current_time)
        pdf.cell(200, 5, txt = "thoi gian thuc hien" + str(current_today) + str(current_time), 
                ln = 1, align = 'C')
        pdf.cell(200, 5, txt = "----------------------------------------------------",
                ln = 50, align = 'C')
        pdf.cell(200, 5, txt = "quyet dinh cua thuan toan",
                ln = 50, align = 'L')
        pdf.cell(200, 5, txt = "" + str(quyetdinh),
                ln = 50, align = 'R')
        pdf.cell(200, 5, txt = "----------------------------------------------------",
                ln = 50, align = 'C')
        # add another cell
        pdf.cell(200, 5, txt = "thong tin nguoi nhap don.",
                ln = 2, align = 'L')
        pdf.cell(200, 5, txt = "gioi tinh.",
                ln = 2, align = 'L')
        pdf.cell(200, 5, txt = "" + str(ui.cob_gioitinh.currentText()),
                ln = 2, align = 'R')
        # add another cell
        pdf.cell(200, 5, txt = "Tinh trang hon nhan",
                ln = 2, align = 'L')
        pdf.cell(200, 5, txt = "" + str( ui.cob_honnhan.currentText()),
                ln = 2, align = 'R')
        # add another cell
        pdf.cell(200, 5, txt = "so nguoi phu thuoc vao nguoi nop don",
                ln = 2, align = 'L')
        pdf.cell(200, 5, txt = "" + str( ui.txt_nguoiphuthuoc.text()),
                ln = 2, align = 'R')
        # add another cell
        pdf.cell(200, 5, txt = "trinh do hoc van",
                ln = 2, align = 'L')
        pdf.cell(200, 5, txt = "" + str( ui.cob_hocvan.currentText()),
                ln = 2, align = 'R')
        # add another cell
        pdf.cell(200, 5, txt = "tu kinh doanh",
                ln = 2, align = 'L')
        pdf.cell(200, 5, txt = "" + str( ui.cob_tukinhdoanh.currentText()),
                ln = 2, align = 'R')
        # add another cell
        pdf.cell(200, 5, txt = "thu nhap cua nguoi nop don",
                ln = 2, align = 'L')
        pdf.cell(200, 5, txt = "" + str( ui.txt_thunhap.text()),
                ln = 2, align = 'R')
        # add another cell
        pdf.cell(200, 5, txt = "thu nhap cua nguoi than",
                ln = 2, align = 'L')
        pdf.cell(200, 5, txt = "" + str( ui.txt_thunhapnguoithan.text()),
                ln = 2, align = 'R')
        # add another cell
        pdf.cell(200, 5, txt = "so tien vay",
                ln = 2, align = 'L')
        pdf.cell(200, 5, txt = "" + str( ui.txt_sotienvay.text()),
                ln = 2, align = 'R')
        # add another cell
        pdf.cell(200, 5, txt = "thoi gian vay",
                ln = 2, align = 'L')
        pdf.cell(200, 5, txt = "" + str( ui.txt_tgvay.text()),
                ln = 2, align = 'R')
        # add another cell
        pdf.cell(200, 5, txt = "khu vuc song cua nguoi nop don",
                ln = 2, align = 'L')
        pdf.cell(200, 5, txt = "" + str( ui.cob_khuvuc.currentText()),
                ln = 2, align = 'R')
        # add another cell
        pdf.cell(200, 5, txt = "nguoi nop don da vay tien truoc day",
                ln = 2, align = 'L')
        pdf.cell(200, 5, txt = "" + str( ui.cob_lichsuvay.currentText()),
                ln = 2, align = 'R')
        # add another cell
        pdf.cell(200, 5, txt = "do tinh cay thuat toan",
                ln = 2, align = 'L')
        pdf.cell(200, 5, txt = "" + str(logiRe.score(x_test,y_test)*100) + "%",
                ln = 2, align = 'R')
        # add another cell
        pdf.cell(200, 5, txt = "nguoi thuc hien",
                ln = 3, align = 'L')
        pdf.cell(200, 5, txt = "" + str(platform.node()),
                ln = 3, align = 'R')
        
        
        # save the pdf with name .pdf
        filename = QtWidgets.QFileDialog.getSaveFileName(caption='Open File',filter="File(*.pdf)")
        print(filename[0])
        pdf.output(filename[0])   
        # pdf.output("EXPORT_QD.pdf")   
        # print(str(ui.cob_gioitinh.currentText()))

    ui.btn_submit.clicked.connect(click_submit)
    ui.btn_reset.clicked.connect(click_reset)
    ui.btn_import.clicked.connect(do_file)
    ui.btn_export.clicked.connect(exportPDF)
    # pathfile = QtWidgets.QFileDialog.getOpenFileNames(caption='Open File',filter="File(*.csv)")
    # print(pathfile)
    # print('----- A-----' + str(pathfile[0][0]))
    # print('----- A-----' + str(pathfile[0][1]))

# show main
    MainWindow.show()
    sys.exit(app.exec_())
