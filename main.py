from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

names = "job-card-container--clickable"
path = "/usr/bin/chromedriver"
url = 'https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C' \
      '%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0 '
driver = webdriver.Chrome(executable_path=path)
driver.get(url)


def login():
    sleep(10)
    signin = driver.find_element_by_link_text("Sign in")
    signin.click()
    name = driver.find_element_by_name("session_key")
    password = driver.find_element_by_name("session_password")
    name.send_keys("dataentrybadar@gmail.com")
    password.send_keys("Pakistan11")
    password.send_keys(Keys.ENTER)


login()
sleep(20)
company_list = driver.find_elements_by_class_name(names)


def application_send():
    easy_button = driver.find_element_by_css_selector(
        'button[class="jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view"]')
    easy_button.click()
    number = driver.find_element_by_name(
        "urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2251558793,9,phoneNumber~nationalNumber)")
    # uncheck = driver.find_element_by_id("follow-company-checkbox")
    submit = driver.find_element_by_link_text("Next")
    # uncheck.click()
    number.send_keys("234567891")
    submit.click()
    submit = driver.find_element_by_link_text("Next")
    submit.click()
    experience = driver.find_elements_by_name("urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2300331824,14582858,numeric)")
    experience.send_keys("1")
    submit = driver.find_element_by_link_text("Review")
    submit.click()
    submit = driver.find_element_by_link_text("")
    submit.click()

# application_send()

# print(company_list[0].text)
for company in company_list:
    print(company.text)
    application_send()
    company.click()
