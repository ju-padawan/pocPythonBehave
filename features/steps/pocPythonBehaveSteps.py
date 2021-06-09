from behave import given, when, then
from selenium.webdriver.common.by import By
import time

@given(u'que tenha acessado a página Automação com Batista')
def step_impl(context):
    context.driver.get('https://automacaocombatista.herokuapp.com/treinamento/home')
    context.driver.maximize_window()
    context.driver.save_screenshot("results/passo001.png")


@when(u'acessar mudança de foco para acessar uma nova janela')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[contains(text(), 'Mudança de foco')]").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[contains(text(), 'Janela')]").click()
    context.driver.save_screenshot("results/passo002.png")
    context.driver.find_element(By.XPATH, "//*[contains(text(), 'Clique aqui')]").click()


@then(u'deve exibir uma nova janela com link especificado')
def step_impl(context):
    time.sleep(2)
    context.driver.switch_to.window(context.driver.window_handles[1])
    elemento = str(context.driver.current_url)
    assert "https://automacaocombatista.herokuapp.com/mudancadefoco/newwindow" in str(elemento)
    context.driver.save_screenshot("results/passo003.png")
