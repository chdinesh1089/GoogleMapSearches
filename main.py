from selenium import webdriver
import time
import csv
#from processing import exists


def writeToCsv(name: str, phone: str, email: str, link: str):
    with open('results.csv', 'a', newline='') as csvfile:
        fieldnames = ['name', 'phone','email','link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #if not exists(name):
        writer.writerow({'name': name, 'phone': phone, 'email': email, 'link': link})
driver = webdriver.Chrome()
keyword = "gyms hyderabad"
keyword = keyword.replace(' ','+')
driver.get("https://www.google.com/maps/search/"+keyword+"/")
time.sleep(1)
#searches = driver.find_elements_by_class_name("section-result-content")
for _k in range(3):
    for i in range(0,20):
        time.sleep(3)
        searches = driver.find_elements_by_class_name("section-result-content")
        len(searches)
        title = searches[i].find_element_by_class_name("section-result-title")
        name=(title.text)
        xpath = '//*[contains(concat( " ", @class, " " ), concat( " ", "section-info-line", " " ))]'
        searches[i].click()
        time.sleep(2)
        info_sections = driver.find_elements_by_xpath(xpath)
        eorw=[]
        phone =''
        for i in info_sections:
            try:
                phone = int((i.text).replace(' ', ''))
            except ValueError:
                k = i.text
                if (
                    k.endswith('.net') or
                    k.endswith('.com') or
                    k.endswith('.in') or
                    k.endswith('.gov') or
                    k.endswith('.org') or
                    k.endswith('.me')):
                    eorw.append(i.text)

        driver.execute_script(script="window.history.back(-1);")
        time.sleep(1)
        # current_url = driver.current_url
        # print(current_url)
        mail =''
        site = ''
        for i in eorw:
            if '@' in i:
                mail = i
            else:
                site = i
                site.replace('Menu\n','')
        writeToCsv(name,phone,mail,site)
        print(phone,mail,site)
    time.sleep(2)
    next = driver.find_element_by_xpath('//*[@aria-label=" Next page "]')
    next.click()
driver.quit()