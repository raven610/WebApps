# lblcgpa
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import xlwt

def find_marks(pin,driver):
	driver.get("https://eweb.gitam.edu/mobile/Pages/NewGrdcrdInput1.aspx")
	elem = Select(driver.find_element_by_id("cbosem"))
	elem.select_by_value('5')
	pin_box = driver.find_element_by_id("txtreg")
	pin_box.send_keys(str(pin))
	button = driver.find_element_by_id("Button1")
	button.click()
	delay = 0
	try:
		WebDriverWait(driver, delay).until(EC.alert_is_present(),'Timed out waiting on popup to appear.')
		alert = driver.switch_to.alert
		alert.accept()
		return ["NA","NA"]
	except TimeoutException:
		try:
			myElem = WebDriverWait(driver, delay+3).until(EC.presence_of_element_located((By.ID, 'lblcgpa')))
			cgpa = driver.find_element_by_id('lblcgpa')
			name = driver.find_element_by_id('lblname')
			return [cgpa.text,name.text]
		except TimeoutException:
			return "Loading took too much time!"
	back = driver.find_element_by_id("Button1")
	back.click()

# print("::::Works Only for 2021 Graduates::::")
# semister = int(input("Enter Semister : "))
# branch = input("Enter branch: ")
# section = input("Enter Your Section : ")
# startPin = int('221710'+branch+section+'01')
startpin = 221710300000
pins=[]
# pins = [startpin+i for i in range(69)]
for i in range(16):
	startpin+=1000
	for j in range(69):
		startpin+=1
		pins.append(startpin)
	startpin-=69
# print(pins)
# exit()
driver = webdriver.Chrome()
marks = []
for i in pins:
	marks.append([i,find_marks(i,driver)])
	
f = open('marks.txt','w')
for i in marks:
	f.write(str(i[0])+' '+str(i[1][0])+' '+str(i[1][1])+'\n')
f.close()
driver.close()

style0 = xlwt.easyxf('font: name Times New Roman, color-index red')
wb = xlwt.Workbook()
ws = wb.add_sheet('CSE Marks',style0)
ws.write(0,0,'Pin')
ws.write(0,1,'Name')
ws.write(0,2,'CGPA')
j = 1
for i in marks:
	if i[1][0] == "NA":
		continue
	ws.write(j,0,str(i[0]),style0)
	ws.write(j,1,str(i[1][1]),style0)
	ws.write(j,2,str(i[1][0]),style0)
	j+=1
wb.save('allsgpa.xls')
