from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from support.actions import SupportActions

def before_all(context):
    context.driver =  webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
 