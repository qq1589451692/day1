from selenium import webdriver
import time
import xlwt,xlrd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get('https://www.csdn.net/')
driver.maximize_window()

time.sleep(40)
cookies = driver.get_cookies()
workbook=xlwt.Workbook(encoding='utf-8')  #创建workbook对象
worksheet=workbook.add_sheet('sheet1')  #创建工作表sheet
worksheet.write(0,0,'name') #往表中写内容。第一个参数 行， 第二个参数 列，第三个参数内容
worksheet.write(0,1,'value')
worksheet.write(0,2,'path')
worksheet.write(0,3,'domain')
worksheet.write(0,4,'httpOnly')
worksheet.write(0,5,'secure')
for i in range(1,len(cookies)+1):
    worksheet.write(i, 0, cookies[i - 1]['name'])  #往表中写内容。第一个参数 行， 第二个参数 列，第三个参数内容
    worksheet.write(i, 1, cookies[i - 1]['value'])
    worksheet.write(i, 2, cookies[i - 1]['path'])
    worksheet.write(i, 3, cookies[i - 1]['domain'])
    worksheet.write(i, 4, cookies[i - 1]['httpOnly'])
    worksheet.write(i, 5, cookies[i - 1]['secure'])
workbook.save('csdn_cookies.xls')