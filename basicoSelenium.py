from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome('/drivers/chromedriver.exe')  # Inicia o browser
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.python.org/')  # Acessar a URL especificada
driver.maximize_window()
driver.find_element_by_css_selector('#id-search-field').send_keys("python")  # Digita o texto "python" no input
driver.find_element_by_css_selector('#submit').click()  # Clica no botão de submit
#driver.quit()  # Encerra o browser