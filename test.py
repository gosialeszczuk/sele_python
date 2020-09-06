from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(
    executable_path=r"C:\Users\Acer\Desktop\Programowanko\sele_python\chromedriver\driver\chromedriver.exe")



def gotoWebpage():
    driver.maximize_window()
    driver.get("http://automationpractice.com/index.php")


def newsletter(email):
    gotoWebpage()
    element = driver.find_element_by_id("newsletter-input")
    element.send_keys(email)
    element = driver.find_element_by_xpath("/html/body/div/div[3]/footer/div/div[1]/div/form/div/button")
    action = ActionChains(driver)
    action.click(on_element=element)
    action.perform()
    element.click()


def sigin():
    gotoWebpage()
    element = driver.find_element_by_xpath("/html/body/div/div[1]/header/div[2]/div/div/nav/div[1]/a")
    element.click()





newsletter("test@test.pl")

