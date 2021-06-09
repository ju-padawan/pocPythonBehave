from behave import given, when, then
from selenium.webdriver.common.by import By
import time

@given(u'que tenha acessado a página Automação com Batista')
def step_impl(context):
    context.driver.get('https://automacaocombatista.herokuapp.com/treinamento/home')
    context.driver.maximize_window()


@when(u'acessar a lista de usuários')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[contains(text(), 'Mudança de foco')]").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[contains(text(), 'Janela')]").click()
    context.driver.find_element(By.XPATH, "//*[contains(text(), 'Clique aqui')]").click()


@then(u'deve exibir o resultado da pesquisa')
def step_impl(context):
    time.sleep(2)
    context.driver.switch_to.window(context.driver.window_handles[1])
    elemento = str(context.driver.current_url)
    assert "https://automacaocombatista.herokuapp.com/mudancadefoco/newwindow" in str(elemento)