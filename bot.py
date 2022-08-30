from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from random import choices

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.monsterenergypromo.de/redeem-code")
sleep(5)
driver.find_element(By.ID, "inputEmail").send_keys("monsterpunkte@abcdy.de")
driver.find_element(By.ID, "inputPassword").send_keys("F4Yr#dEahq")
WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,"//button[@Class='btn btn-primary' and text()='Anmelden']"))).click()


# Alphabet, weil habe vergessen wie das nochmals geht...
#letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X"]
# Codefunktion
def randomCode():
    driver.find_element(By.NAME, "code[code][code1]").send_keys("K")
    driver.find_element(By.NAME, "code[code][code2]").send_keys(choices(letters, weights=(67, 33, 33, 22, 67, 33, 22, 33, 44, 22, 22, 33, 22, 33, 55, 11, 11, 55, 11, 22, 89), k=1))
    driver.find_element(By.NAME, "code[code][code3]").send_keys(choices(letters, weights=(67, 33, 33, 22, 67, 33, 22, 33, 44, 22, 22, 33, 22, 33, 55, 11, 11, 55, 11, 22, 89), k=1))
    driver.find_element(By.NAME, "code[code][code4]").send_keys(choices(letters, weights=(67, 33, 33, 22, 67, 33, 22, 33, 44, 22, 22, 33, 22, 33, 55, 11, 11, 55, 11, 22, 89), k=1))
    driver.find_element(By.NAME, "code[code][code5]").send_keys(choices(letters, weights=(67, 33, 33, 22, 67, 33, 22, 33, 44, 22, 22, 33, 22, 33, 55, 11, 11, 55, 11, 22, 89), k=1))
    driver.find_element(By.NAME, "code[code][code6]").send_keys(choices(letters, weights=(67, 33, 33, 22, 67, 33, 22, 33, 44, 22, 22, 33, 22, 33, 55, 11, 11, 55, 11, 22, 89), k=1))
    driver.find_element(By.NAME, "code[code][code7]").send_keys(choices(letters, weights=(67, 33, 33, 22, 67, 33, 22, 33, 44, 22, 22, 33, 22, 33, 55, 11, 11, 55, 11, 22, 89), k=1))
    driver.find_element(By.NAME, "code[code][code8]").send_keys(choices(letters, weights=(67, 33, 33, 22, 67, 33, 22, 33, 44, 22, 22, 33, 22, 33, 55, 11, 11, 55, 11, 22, 89), k=1))
    driver.find_element(By.NAME, "code[code][code9]").send_keys(choices(letters, weights=(67, 33, 33, 22, 67, 33, 22, 33, 44, 22, 22, 33, 22, 33, 55, 11, 11, 55, 11, 22, 89), k=1))
    driver.find_element(By.NAME, "code[code][code10]").send_keys(choices(letters, weights=(67, 33, 33, 22, 67, 33, 22, 33, 44, 22, 22, 33, 22, 33, 55, 11, 11, 55, 11, 22, 89), k=1))
    sleep(1)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='form-group']//button[@Class='btn-primary btn' and text()='Bestätigen']"))).click()
    sleep(5)

#Feld löschen
def clearField():
    driver.find_element(By.NAME, "code[code][code10]").send_keys(Keys.BACKSPACE)
    driver.find_element(By.NAME, "code[code][code9]").send_keys(Keys.BACKSPACE)
    driver.find_element(By.NAME, "code[code][code8]").send_keys(Keys.BACKSPACE)
    driver.find_element(By.NAME, "code[code][code7]").send_keys(Keys.BACKSPACE)
    driver.find_element(By.NAME, "code[code][code6]").send_keys(Keys.BACKSPACE)
    driver.find_element(By.NAME, "code[code][code5]").send_keys(Keys.BACKSPACE)
    driver.find_element(By.NAME, "code[code][code4]").send_keys(Keys.BACKSPACE)
    driver.find_element(By.NAME, "code[code][code3]").send_keys(Keys.BACKSPACE)
    driver.find_element(By.NAME, "code[code][code2]").send_keys(Keys.BACKSPACE)
    driver.find_element(By.NAME, "code[code][code1]").send_keys(Keys.BACKSPACE)

#i = Wie oft machen Sachen?
for i in range(500):
    randomCode()
    clearField()

    




'''randomString = ''
    for i in range(9):
        randomString += choices(letters) 
    fin = "K" + randomString
    print(fin)
    driver.find_element(By.NAME, "code[code][code1]").send_keys(fin)'''




