from behave import given, when, then
from selenium.webdriver.common.by import By
import time
from support.actions import SupportActions


@given(u'que tenha acessado a página Automação com Batista')
def step_impl(context):
    context.lista_evidencias = []
    context.acoes = SupportActions(context.driver)
    context.acoes.ler_dados_arquivo_yaml()
    context.driver.get('https://automacaocombatista.herokuapp.com/treinamento/home')
    context.acoes.gerar_imagem_evidencia("passo001.png", context.lista_evidencias)


@when(u'acessar mudança de foco para acessar uma nova janela')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[contains(text(), 'Mudança de foco')]").click()
    context.driver.find_element(By.XPATH, "//*[contains(text(), 'Janela')]").click()
    context.acoes.gerar_imagem_evidencia("passo002.png", context.lista_evidencias)
    context.driver.find_element(By.XPATH, "//*[contains(text(), 'Clique aqui')]").click()


@then(u'deve exibir uma nova janela com link especificado')
def step_impl(context):
    context.acoes.mudar_pagina_em_foco(1)
    elemento = str(context.driver.current_url)
    assert "https://automacaocombatista.herokuapp.com/mudancadefoco/newwindow" in str(elemento)
    context.acoes.gerar_imagem_evidencia("passo003.png", context.lista_evidencias)
    context.acoes.gerar_documento_evidencia("cenario_teste_01.docx", context.lista_evidencias)
    context.acoes.fechar_pagina_em_foco(1)
    context.acoes.mudar_pagina_em_foco(0)


@when(u'acessar a lista de usuários cadastrados')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[contains(text(), 'Formulário')]").click()
    context.acoes.gerar_imagem_evidencia("passo002.png", context.lista_evidencias)
    context.driver.find_element(By.XPATH, "//*[contains(text(), 'Lista de Usuários')]").click()


@then(u'deve exibir a lista de usuários')
def step_impl(context):
    elemento = context.driver.find_element(By.XPATH, "//div[@class='tamanhodiv2']/h5")
    assert "Lista de Usuários!!" in elemento.text
    context.acoes.gerar_imagem_evidencia("passo003.png", context.lista_evidencias)
    context.acoes.gerar_documento_evidencia("cenario_teste_02.docx", context.lista_evidencias)

