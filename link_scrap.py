#Author : Md. Tareq Ahamed
#Member of Knight Squad
#Contact me : https://www.facebook.com/TareqAhamed8/ 

from selenium import webdriver
import time
import re
import webbrowser
import sys

PATH = "C:\Program Files (x86)\chromedriver.exe"
# PATH = "C:\Program Files\Mozilla Firefox\geckodriver.exe"
start_time = time.time()

argu = webdriver.ChromeOptions()
# argu.add_argument('headless')
argu.add_experimental_option("debuggerAddress", "localhost:9222")
browser = webdriver.Chrome(PATH, options=argu)  # you have to specify the path with driver
# browser = webdriver.Firefox(PATH)

link_list = []

for i in range(set_the_range):
    browser.get('https://gmail.com')  # target domain
    time.sleep(2)

    view_path = browser.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[8]/div/div[1]/div[3]/div/table/tbody/tr[1]').click()
    text = browser.find_elements_by_xpath(
        '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div/div[1]')
    for element in text:
        print(element.text)
        link = re.search("(?P<url>https?://[^\s]+)", element.text).group("url")
        link_list.append(link)
    delete = browser.find_element_by_xpath('//*[@id=":4"]/div[2]/div[1]/div/div[2]/div[3]').click()
    time.sleep(2)
for link in link_list:
    print(link)
