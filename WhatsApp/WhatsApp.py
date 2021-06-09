from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='C:\\Users\dishan\Documents\chromedriver_win32\chromedriver.exe')
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of receipant:')
msg = input('Enter your message:')
count = int(input("Enter the count:"))
input('Press Enter after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

for i in range(count):
    msg_box.send_keys(msg)
    time.sleep(2)
    button = driver.find_element_by_class_name('_1E0Oz')
    button.click()
