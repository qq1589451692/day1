from selenium import webdriver
import time
import xlwt,xlrd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get('https://www.csdn.net/')
driver.maximize_window()

workbook=xlrd.open_workbook('csdn_cookies.xls')
sheet=workbook.sheet_by_name('sheet1')
cookie_list=[]
for row_num in range(1,sheet.nrows):
    cookie_dict={}
    cookie_dict['name'] = sheet.cell_value(row_num, 0)
    cookie_dict['value'] = sheet.cell_value(row_num, 1)
    cookie_dict['path'] = sheet.cell_value(row_num, 2)
    cookie_dict['domain'] = sheet.cell_value(row_num, 3)
    cookie_dict['httpOnly'] =bool( sheet.cell_value(row_num, 4) )
    cookie_dict['secure'] = bool( sheet.cell_value(row_num, 5) )
    cookie_list.append(cookie_dict)
for cookie in cookie_list:
    driver.add_cookie(cookie)
time.sleep(5)
driver.refresh()