from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

driver = webdriver.Chrome(
        executable_path=r"C:\Users\Acer\Desktop\Programowanko\sele_python\chromedriver\driver\chromedriver.exe")


# go to webpage
def gotoWebpage(website):
    driver.get(website)

webpage="http://automationpractice.com/index.php"
gotoWebpage(webpage)

