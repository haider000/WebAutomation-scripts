from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager
from secret import EMAIL,PASSWORD
from time import sleep
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("window-size=1200,900")

driver= webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)



driver.get("https://www.linkedin.com/")

sleep(2)

emailBox = driver.find_element_by_xpath('//*[@id="session_key"]')
emailBox.send_keys(EMAIL)



passBox = driver.find_element_by_xpath('//*[@id="session_password"]')
passBox.send_keys(PASSWORD)



signButton = driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/div[2]/form/button')
signButton.click()

sleep(1)


driver.get("https://www.linkedin.com/mynetwork/invitation-manager/")

sleep(2)

acceptBtn  = driver.find_elements_by_css_selector('.invitation-card__action-btn.artdeco-button.artdeco-button--2.artdeco-button--secondary.ember-view')
                                                   
print(acceptBtn)
print(type(acceptBtn))
print()

for i in acceptBtn:
    i.click()
    sleep(3)

'''
#js commands execution through selenium


driver.execute_script(""" 
let acceptBtns = document.querySelectorAll('.invitation-card__action-btn.artdeco-button.artdeco-button--2.artdeco-button--secondary.ember-view');
for (const btn of acceptBtns){
    btn.click();
}
""") 

'''