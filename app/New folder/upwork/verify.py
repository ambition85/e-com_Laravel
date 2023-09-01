import json
import time
# import undetected_chromedriver as uc
# from undetected_chromedriver import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import threading

with open('acc_links.json', 'r') as f:
    links = json.load(f)

with open('acc_created.txt', 'r') as f:
    emails = f.read().splitlines(False)

def main():
    options = Options()
    while emails:
        email = emails.pop(0)
        try:
            try:
                links[email]
            except:
                continue
            driver = webdriver.Chrome(options=options)
            # driver = uc.Chrome()
            driver.get('https://www.upwork.com/ab/account-security/login')
            time.sleep(2)
            driver.execute_script('document.querySelector("#onetrust-accept-btn-handler").click();')
            driver.find_element(by=By.ID, value='login_username').send_keys(f'{email}\n')
            time.sleep(1)
            driver.find_element(by=By.ID, value='login_password').send_keys('Mickey.623\n')
            time.sleep(7)
            driver.get(links[email])
            time.sleep(15)
            driver.find_element(By.XPATH, "//button[@data-qa='get-started-btn']").click()
            for j in range(4):
                time.sleep(5)
                try:
                    driver.find_element(By.XPATH, "//button[@data-test='skip-button']").click()
                except:
                    pass
            time.sleep(10)
            driver.find_element(By.XPATH, "//button[@data-qa='resume-fill-manually-btn']").click()
            time.sleep(3)
            driver.find_element(By.XPATH, "//input[@aria-labelledby='title-label']").send_keys(role)
            driver.find_element(by=By.XPATH, value='//button[@data-ev-label="wizard_next"]').click()
            time.sleep(3)
            for j in range(3):
                time.sleep(5)
                try:
                    driver.find_element(By.XPATH, "//button[@data-test='skip-button']").click()
                except:
                    pass
            time.sleep(5)
            driver.execute_script("""async function sleep(ms){return new Promise(resolve=>setTimeout(resolve,ms));}document.querySelector("div[id^='dropdown-label']").click();await sleep(2000);document.querySelector("ul[id^='dropdown-menu'] > li:nth-child(3)").click();""")
            driver.find_element(by=By.XPATH, value='//button[@data-ev-label="wizard_next"]').click()
            time.sleep(5)
            driver.execute_script("""async function sleep(ms){return new Promise(resolve=>setTimeout(resolve,ms));}const a=document.querySelector('div[aria-labelledby="token-container-label"]');const b=a.querySelectorAll('div[role="button"]');b.forEach((c)=>{sleep(500).then(()=>{c.click();});});""")
            time.sleep(2)
            driver.find_element(by=By.XPATH, value='//button[@data-ev-label="wizard_next"]').click()
            time.sleep(5)
            driver.find_element(By.XPATH, "//textarea[@aria-labelledby='overview-label']").send_keys(overview)
            driver.find_element(by=By.XPATH, value='//button[@data-ev-label="wizard_next"]').click()
            time.sleep(5)
            driver.execute_script("""async function sleep(ms){return new Promise(resolve=>setTimeout(resolve,ms));}document.querySelectorAll('button[data-qa="category-add-btn"]').forEach(a => {sleep(500).then(()=>{a.click();});});""")
            time.sleep(1)
            driver.find_element(by=By.XPATH, value='//button[@data-ev-label="wizard_next"]').click()
            time.sleep(5)
            driver.find_element(By.XPATH, "//input[@placeholder='$0.00']").send_keys('25')
            driver.find_element(by=By.XPATH, value='//button[@data-ev-label="wizard_next"]').click()
            time.sleep(5)
            driver.find_element(By.XPATH, "//button[@data-qa='open-loader']").click()
            time.sleep(3)
            driver.find_element(By.CSS_SELECTOR, "[id^='image-crop']").send_keys(f'C://avatars//avatar1.png')
            time.sleep(2)
            driver.find_element(by=By.XPATH, value='//button[contains(text(), "Attach photo")]').click()
            time.sleep(10)
            # driver.find_element(by=By.XPATH, value="//*[starts-with(@id, 'dropdown-label')]").click()
            # time.sleep(2)
            # driver.find_element(by=By.XPATH, value="//ul[starts-with(@id, 'dropdown-menu')]/li[222]").click() # 222 number means Ukraine, we need to know which number is phillipine
            ## 222:Ukraine, 167:Philippines
            driver.execute_script("""async function sleep(ms){return new Promise(resolve=>setTimeout(resolve,ms));}document.querySelector("[aria-labelledby*=\'country-label\']").click();await sleep(2000);document.querySelector("ul[id^='dropdown-menu'] > li:nth-child(167)").click();""")
            time.sleep(1)
            driver.find_element(by=By.XPATH, value='//input[@aria-labelledby="street-label"]').send_keys(basic_info['street'])
            driver.find_element(by=By.XPATH, value='//input[@aria-labelledby="city-label"]').send_keys(basic_info['city'])
            time.sleep(1)
            driver.find_element(by=By.CSS_SELECTOR, value='input[id^="typeahead-input"]').send_keys(basic_info['city'])
            time.sleep(3)
            driver.execute_script("""document.querySelector("ul[id^='typeahead-input-control'] > li:nth-child(1)").click()""")
            time.sleep(1)
            driver.find_element(by=By.XPATH, value='//input[@placeholder="Enter number"]').send_keys(basic_info['phone'])
            driver.find_element(by=By.XPATH, value='//button[contains(text(), "Review your profile")]').click()
            time.sleep(3)
            driver.execute_script("""document.querySelector('button[data-qa="submit-profile-top-btn"]').click();""")
            time.sleep(2)
            with open("acc_verified.txt", 'a') as f:
                f.write(f'{email}\n')
            with open("acc_created.txt", 'w') as f:
                f.writelines('\n'.join(emails))

        except Exception as e:
            with open('acc_verify_error.txt', 'a') as f:
                f.write(f'{email}\n')
            with open("acc_created.txt", 'w') as f:
                f.writelines('\n'.join(emails))

if __name__ == "__main__":
    global  basic_info, roles, role, overview
    basic_info={
        'street': 'Globe Theather Building',
        'city': 'Manila',
        'phone': '84408374'
    }
    roles = [
        "Frontend Developer| React| Next| Vue",
        "Javascript Developer| ExpressJS| React| MongoDB",
        "PHP Developer| Wordpress| Laravel| React",
        "Python Developer| Django| React| Angular",
        "Shopify Developer| React| Vue| Angular"
    ]
    role = "Nodejs | Python | Laravel | React | Vue"
    overview = """As a full stack website developer having experience in various type of website developments running in web frameworks such as Django, Flutter, React, Angular.
    Having done many projects for the last 5 years, i can become a experienced full stack developer.
    My goal of the jobs is that there has to be no one thing unclear or bug in my clients project.
    However the most important thing is to deliver the product within specific timeframe.
    I'm trying hard to become a top one in freelancer.com
    My major tech stacks are here.

    //===== Full Stack =====//
    Database : MySQL, MongoDB, PostgreSQL, Cassandra, Microsoft SQL Server, MariaDB
    Backend : Python ( Django, Flask, FastAPI ), PHP, Laravel, Nodejs ( Express ), C# (ASP.NET)
    Frontend : Javascript ( React, Vue ), HTML, CSS, Bootscrap

    //===== Data Scrapping =====//
    Python ( Selenium, Scrapy, Beautifulsoup, Requests )
    PHP ( cURL, ZenRows, Gouttle )

    //===== Mobile Application =====//
    Flutter/Dart, Xamarin, Swift
    """

    threads = []
    for i in range(5):
        t = threading.Thread(target=main)
        threads.append(t)
    # Start the threads
    for t in threads:
        t.start()
    # Wait for all threads to finish
    for t in threads:
        t.join()
    print("All threads completed.")
