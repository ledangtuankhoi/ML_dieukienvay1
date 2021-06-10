import sys
from PySide2.QtWidgets import QPushButton
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from seaborn import palettes
from seaborn import widgets
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

    ui.label_status.setText('ELIGIBLE')

    
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


    def click_submit(self):
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
            str(logiRe.score(x_test,y_test)*100) + "%" +"\n"+ str(mau_test))
            ui.label_desi.setStyleSheet("border: 1px solid black;")
        else:
            ui.label_status.setText('')
            print("chua nhap lieu")
            ui.label_status.setStyleSheet("border: 1px solid black; background-color: transparent")
            ui.label_desi.setText('CHUA NHAP LIEU: ')



    def click_reset(self):
        print("btn_reset")
        ui.txt_thunhap.setText('')
        ui.txt_thunhapnguoithan.setText('')
        ui.txt_sotienvay.setText('')
        ui.txt_tgvay.setText('')
        ui.txt_nguoiphuthuoc.setText('')
        

    ui.btn_submit.clicked.connect(click_submit)
    ui.btn_reset.clicked.connect(click_reset)

# show main
    MainWindow.show()
    sys.exit(app.exec_())
