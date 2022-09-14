import PySimpleGUI as sg


tai_khoan = 'hello'
mat_khau = '1234'

layout = [[sg.Text("Tài khoản: "), sg.Input(key = 'account_input')],
          [sg.Text("Mật khẩu: "), sg.Input(key = 'password_input')],
          [sg.Submit(key= 'submit_Button')]]
window = sg.Window("UIS",layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "submit_Button":
        if values['account_input'] != tai_khoan :
            sg.popup("WRONG ACCOUNT")
        elif values['password_input'] != mat_khau:
            sg.popup("WRONG PASSWORD")
    
            
window.close()