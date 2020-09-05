from selenium import webdriver



driver = webdriver.Chrome(
    executable_path=r"C:\Users\Acer\Desktop\Programowanko\sele_python\chromedriver\driver\chromedriver.exe")


# go to webpage
def gotoWebpage():
    driver.get("http://automationpractice.com/index.php")

def newsletter():
    gotoWebpage()
    element=driver.find_element_by_id("newsletter-input")
    element.send_keys("test@test.com")
   # element.find_element_by_xpath("//*[@id="newsletter_block_left"]/div/form/div/button")
    # element.find_element_by_class_name("alert alert-success")


newsletter()
