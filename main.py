from turtle import tracer
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
from selenium.webdriver.common.by import By


hieu_tk = 20154038
hieu_mk = 418912874312
back_tk = 20124038
back_mk = 229812


print("-- Import library --")
driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")
url = 'https://online.hcmute.edu.vn/'
driver.get(url)
print('-- Finish initializing a driver--')

driver.find_element(By.ID,"ctl00_lbtDangnhap").click()
driver.find_element(By.XPATH,"/html/body/div/form/table/tbody/tr[5]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/input").send_keys(back_tk)
driver.find_element(By.XPATH,"/html/body/div/form/table/tbody/tr[5]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/input").send_keys(back_mk)

driver.find_element(By.XPATH, "/html/body/div/form/table/tbody/tr[5]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr[4]/td/table/tbody/tr/td[2]/input").click()
driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_ctl00_ctl00_lnkThoiKhoaBieu").click()
print("-- Complete login to page --")

def loc_mon_hoc (mon_hoc):
    ten_mon_hoc = mon_hoc[0:mon_hoc.find("[")]
    gio_hoc = mon_hoc[mon_hoc.find("]")+1:mon_hoc.find('Tiết')]
    tiet_hoc = mon_hoc[mon_hoc.find('Tiết'):mon_hoc.find('GV')]
    giang_vien =mon_hoc[mon_hoc.find("GV"):mon_hoc.find('Cơ')]
    mon_hoc = ten_mon_hoc +'\n'+ gio_hoc+'\n'+ tiet_hoc +'\n'+ giang_vien
    return mon_hoc

def transform_web_element_to_list(x_path):
    find_list = driver.find_element(By.XPATH, x_path).find_elements(By.TAG_NAME, "option")
    list_transform = []
    for i in find_list:
        list_transform.append(i.text)
    return list_transform   


x_path_nam_hoc = "/html/body/div/form/table/tbody/tr[5]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td[3]/table[2]/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[3]/td[1]/select[1]"
x_path_hoc_ky = "/html/body/div/form/table/tbody/tr[5]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td[3]/table[2]/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[3]/td[1]/select[2]"
x_path_tuan_hoc = "/html/body/div/form/table/tbody/tr[5]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td[3]/table[2]/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[5]/td/select"
#HELLO 
list_nam_hoc  = transform_web_element_to_list(x_path_nam_hoc)
list_hoc_ky   = transform_web_element_to_list(x_path_hoc_ky)
list_tuan_hoc = transform_web_element_to_list(x_path_tuan_hoc)
ten_MSSV = list(driver.find_element(By.CLASS_NAME,"StudentInfoDetails_normal_dl").text)



page_source =BeautifulSoup(driver.page_source,"html.parser")
info_table = page_source.find('table', class_ = "Scheduled_table_dl")
print("-- Complete take the page source -- ")



info_tr = page_source.find_all("td",{'class':"Schedule_tabledetails_td"})
time_table = []
count = 0



    
while count < len(info_tr):
    time_table_temp = []
    for i in  range(7):
        mon_hoc = info_tr[count].get_text()
        if len(mon_hoc) <= 3:
            time_table_temp.append(0)
            count += 1
        elif len(mon_hoc) > 4:
            time_table_temp.append(loc_mon_hoc(mon_hoc))
            count+=1
    time_table.append(time_table_temp)  


with open("thong_tin_SV_TIME_TABLE.csv", "w", encoding="utf-8") as file_info:
    writer = csv.writer(file_info, delimiter=",")
    writer.writerow(ten_MSSV)
    writer.writerow(list_nam_hoc)   
    writer.writerow(list_hoc_ky)
    writer.writerow(list_tuan_hoc)
        
with open("thoi_kho_bieu_output.csv", "w", encoding="utf-8") as f_timetable:
    headers = ['thu_2','thu_3','thu_4','thu_5','thu_6','thu_7', 'chu_nhat']
    writer = csv.writer(f_timetable, delimiter=",")
    writer.writerow(headers)
    for i in time_table:
         writer.writerow([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])
print('-- Complete write time table to CSV file --')
driver.close()
print('-- Close the chrome windown --')