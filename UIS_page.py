



from turtle import update
import PySimpleGUI as sg 
import pandas as pd 

file_Path = "D:/UIS_PROJECT/thoi_kho_bieu_output.csv"
thoi_Khoa_Bieu_df = pd.read_csv(file_Path)
thu_hoc = list(thoi_Khoa_Bieu_df.columns)
thoi_khoa_bieu = thoi_Khoa_Bieu_df.values.tolist()
ten_MSSV = "TRỊNH XUÂN BÁCH [20124038]"

# thoi_khoa_bieu = [['An toàn lao động và \n môi trường công nghiệp \n [2]15g10 -> 17g50\nTiết 10-12 \n GV: Đặng Quang Khoa',0,0,0,0,0,0]]
print(thu_hoc)
layout = [[sg.Text("THỜI KHOÁ BIỂU")],
          [sg.Text(ten_MSSV)],
          [sg.Text("NĂM HỌC : "), sg.DropDown([1,2,3], size = (30,6)), sg.Text('HỌC KỲ: '),sg.DropDown([1,2,3],size = (30,6))],

          [sg.Button('UPDATE', key='__UPDATE_BUTTON__')],
          [sg.Table(thoi_khoa_bieu, headings= thu_hoc, key='-TABLE-',row_height=115,justification = "left", 
                    expand_x=  True,expand_y=True, pad= 10)]]

window = sg.Window("UIS",layout, size= (1600,800))
 
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '__UPDATE_BUTTON__':
        new_thoi_khoa_bieu = pd.read_csv(file_Path)
        new_thoi_khoa_bieu = pd.read_csv(file_Path)
        thu_hoc = list(new_thoi_khoa_bieu.columns)
        thoi_khoa_bieu_new = new_thoi_khoa_bieu.values.tolist()
        window['-TABLE-'].update(thoi_khoa_bieu_new)
        
    
window.close()