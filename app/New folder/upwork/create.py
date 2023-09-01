import time
# import undetected_chromedriver as uc
# from undetected_chromedriver import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from datetime import datetime

def main():
    name = {'first' : 'Michael' , 'last' : 'Edwards'}
    now = datetime.now()
    year = now.strftime("%y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    filename = f'{year}-{month}-{day}.txt'
    try:
        with open(filename, 'r') as f:
            st = int(f.readline())+1
    except:
        with open(filename, 'w') as f:
            f.write('0')
        st = 0
    #count = int(input("how many : "))
    options = Options()
    for i in range(st, st+200):
        iii = str(i).zfill(3)
        email = f"michael.edy623+{month}{day}{iii}@gmail.com"
        driver = webdriver.Chrome(options=options)
        # driver = uc.Chrome()
        driver.get('https://www.upwork.com/nx/signup/?dest=home')
        time.sleep(2)
        driver.execute_script('document.querySelector("#onetrust-accept-btn-handler").click();')
        driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div/div/div/div/div/div[1]/fieldset/div/div[2]/div').click()
        driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div/div/div/div/div/div[2]/button').click()
        time.sleep(2)
        driver.find_element(by=By.XPATH, value='//*[@id="first-name-input"]').send_keys(name['first'])
        driver.find_element(by=By.XPATH, value='//*[@id="last-name-input"]').send_keys(name['last'])
        driver.find_element(by=By.XPATH, value='//*[@id="redesigned-input-email"]').send_keys(email)
        driver.find_element(by=By.XPATH, value='//*[@id="password-input"]').send_keys('Mickey.623')
        driver.find_element(by=By.XPATH, value='//*[@id="signupForm-redesigned"]/fieldset/div[2]').click()
        driver.find_element(by=By.ID, value='button-submit-form').click()
        time.sleep(5)
        with open("acc_created.txt", "a") as f:
            f.write(f'{email}\n')
        with open(filename, 'w') as f:
            f.write(str(i))

if __name__ == "__main__":
    main()
