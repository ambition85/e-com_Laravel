import time
import requests
# import undetected_chromedriver as uc
# from undetected_chromedriver import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import concurrent.futures
import openai

# Set up your OpenAI API credentials
openai.api_key = "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"

def get_forefront_proposal(description):
    url = "https://streaming-worker.forefront.workers.dev/chat"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9,ru;q=0.8",
        "Content-Type": "application/json",
        "Authorization": """Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6Imluc18yTzZ3UTFYd3dxVFdXUWUyQ1VYZHZ2bnNaY2UiLCJ0eXAiOiJKV1QifQ.eyJhenAiOiJodHRwczovL2NoYXQuZm9yZWZyb250LmFpIiwiZXhwIjoxNjkyNjUwOTQwLCJpYXQiOjE2OTI2NTA4ODAsImlzcyI6Imh0dHBzOi8vY2xlcmsuZm9yZWZyb250LmFpIiwibmJmIjoxNjkyNjUwODcwLCJzaWQiOiJzZXNzXzJVQThrd25zZWtnV1Jxc0ZQYnNjTURJbGRScCIsInN1YiI6InVzZXJfMlVBOGt2Yjg2U090aUtycWZERGFwNjBSTjZMIn0.r0AuCtK-at2j8-W-aKkb9umddONum35zwQ3Iebayo3nzV3ZE9-0LzL5h5TSpaVpvj-_vomOxK6AcRQxc8wmZgNTk2BKNYfuI3Dmv45pTFxHO_6lezmobo-lOGo8Q8CbK0KXXMbvvko26lfVyzTHiZz2NU39bJeXZYzL_KMPpymkTrVbo1D03k_XCo8S8_i7kzwJQW9r7WuUZbIabhluoiFS067uZqvOdrQgYjEDLcxBq280pzzZD4anAjM6dDsWYSGFjiIjaypThastDHxb5XnHbPUWnnGszSGR0qJ8-LIxwfn7tV_8terEliaiIuzWcPUKiWkAlCU55pBw5N5mL0A"""
    }
    payload = {
        "text": """My name is Michael Edwards, Places kind, professinal bid on this project including greetings. starts with Dear Client.\n{}""".format(description),
        "action": "new",
        "parentId": "96405989-1de8-4e8a-8fc2-57f3bbdec83d",
        "workspaceId": "96405989-1de8-4e8a-8fc2-57f3bbdec83d",
        "messagePersona": "default",
        "model": "gpt-3.5-turbo",
        "messages": [],
        "internetMode": "never",
        "hidden": False
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.text.split("end\ndata: \"")[1]

def get_chatgpt_proposal(description):
    # Define your prompt
    prompt = f'Michael Edwards places kind, professinal bid on this project including greetings.\n{description}'
    response = openai.Completion.create(
        engine='text-davinci-003',  # GPT-3.5-turbo model
        prompt=prompt,
        max_tokens=3800,  # Adjust as desired to control response length
        n=1,  # Number of responses to generate
        stop=None,  # Specify a stopping criterion if required
    )
    return response['choices'][0]['text'] # type: ignore

def upwork_login(email, password = "Mickey.623"):
    options = Options()
    driver = webdriver.Chrome(options=options)
    # driver = uc.Chrome()
    driver.maximize_window()
    driver.get('https://www.upwork.com/ab/account-security/login')
    time.sleep(2)
    driver.execute_script('document.querySelector("#onetrust-accept-btn-handler").click();')
    driver.find_element(by=By.ID, value='login_username').send_keys(f'{email}\n')
    time.sleep(2)
    driver.find_element(by=By.ID, value='login_password').send_keys(f'{password}\n')
    time.sleep(7)
    drivers.append([driver,email])

def drivers_ready():
    max_workers = 10 - len(drivers)
    if not max_workers:
        return
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(upwork_login, emails.pop()) for _ in range(max_workers)]
        concurrent.futures.wait(futures)
    # with open("acc_verified.txt", 'w') as f:
    #     f.writelines('\n'.join(emails))

def process_bid(url):
    driver, email = drivers.pop(0)
    driver.get(url)
    prompt = driver.execute_script('return document.querySelector(".job-description").innerText;')
    driver.find_element(by=By.CSS_SELECTOR, value='button[aria-label="Apply Now"]').click()
    time.sleep(5)
    try:
        driver.execute_script('document.querySelector(".up-modal-dialog button").click()')
        time.sleep(1)
    except:
        pass
    try:
        driver.execute_script('document.querySelectorAll(".up-checkbox-label")[1].click()')
        driver.execute_script("""async function sleep(ms){return new Promise(resolve=>setTimeout(resolve,ms));}document.querySelector(".up-dropdown-icon").click();await sleep(1000);document.querySelectorAll("li[role='option']")[3].click();""")
    except:
        pass
    proposal = get_forefront_proposal(prompt)
    proposal = proposal.replace("\\n","\n")
    try:
        driver.find_element(by=By.XPATH, value='//textarea[@aria-labelledby="cover_letter_label"]').send_keys(proposal) # type: ignore
        driver.find_element(by=By.XPATH, value='//button[contains(text(), "Set a bid")]').click()
        time.sleep(2)
        driver.find_element(by=By.XPATH, value='//input[@max="50"]').clear()
        driver.find_element(by=By.XPATH, value='//input[@max="50"]').send_keys("50")
        driver.find_element(by=By.XPATH, value='//button[contains(text(), "Bid")]').click()
        time.sleep(2)
        driver.find_element(by=By.XPATH, value='//button[contains(text(), "Send for 50 Connects")]').click()
        time.sleep(5)
    except:
        return
    try:
        driver.find_element(by=By.CLASS_NAME, value="up-modal-dialog")
        driver.execute_script("""async function sleep(ms){return new Promise(resolve=>setTimeout(resolve,ms));}document.querySelector("input[name='checkbox']").click();await sleep(500);document.querySelectorAll(".up-modal-footer button")[1].click()""")
        time.sleep(3)
        driver.execute_script("""async function sleep(ms){return new Promise(resolve=>setTimeout(resolve,ms));}document.querySelector("input[name='checkbox']").click();await sleep(500);document.querySelectorAll(".up-modal-footer button")[1].click()""")
        time.sleep(5)
    except:
        pass
    driver.close()
    with open("acc_used.txt", 'a') as f:
        f.write(f'{email}\n')

def place_bid(urls):
    max_workers = len(urls)
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(process_bid, (url)) for url in urls]
        concurrent.futures.wait(futures)

def main():
    global drivers
    global emails
    drivers = []
    try:
        with open('acc_verified.txt', 'r') as f:
            emails = f.read().splitlines(False)
    except:
        return
    email = "michael.edy623@gmail.com"
    password = "Mickey.623"
    options = Options()
    driver = webdriver.Chrome(options=options)
    # driver = uc.Chrome()
    driver.maximize_window()
    driver.get('https://www.upwork.com/ab/account-security/login')
    time.sleep(2)
    driver.execute_script('document.querySelector("#onetrust-accept-btn-handler").click();')
    driver.find_element(by=By.ID, value='login_username').send_keys(f'{email}\n')
    time.sleep(2)
    driver.find_element(by=By.ID, value='login_password').send_keys(f'{password}\n')
    time.sleep(7)
    # driver.get('https://www.upwork.com/nx/jobs/search/?sort=recency&ontology_skill_uid=996364628025274386&category2_uid=531770282580668418')
    driver.get('https://www.upwork.com/nx/jobs/search/?sort=recency&subcategory2_uid=531770282584862733&payment_verified=1')
    prev = []
    while True:
        curr = []
        sections = driver.find_elements(by=By.TAG_NAME, value="section")[1:]
        for section in sections:
            try:
                client_country = section.find_element(by=By.XPATH, value="//small[@data-test='client-country']").text.replace('\n','').strip()
                if client_country in ["India", "Pakistan", "Bangladesh"]:
                    continue
                else:
                    curr.append(section.find_element(by=By.TAG_NAME, value="a").get_attribute("href"))
            except:
                client_country = ''
        # curr = [ section.find_element(by=By.TAG_NAME, value="a").get_attribute("href") for section in sections ]
        if not prev:
            prev = curr
        else:
            news = set(curr) - set(prev)
            if len(news):
                prev = curr
                place_bid(news)
            else:
                time.sleep(30)
        drivers_ready()
        driver.refresh()

if __name__ == "__main__":
    main()
