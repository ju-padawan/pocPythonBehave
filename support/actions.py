from docx import Document
from docx.shared import Inches
import os
from selenium.webdriver.common.by import By
import time
import yaml


class SupportActions():

    def __init__(self, driver):
        self.driver = driver


    
    def mudar_pagina_em_foco(self, nova_pagina):
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[nova_pagina])


    def fechar_pagina_em_foco(self, pagina):
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[pagina])
        self.driver.close()


    def gerar_imagem_evidencia(self, passo, lista_evidencias):
        caminho_arquivo = "results/"+str(passo)
        time.sleep(2)
        self.driver.save_screenshot(caminho_arquivo)
        lista_evidencias.append(passo)


    def gerar_documento_evidencia(self, arquivo_evidencias, lista_evidencias):
        self.documento = Document()
        doc_nome = "results/"+str(arquivo_evidencias)

        count = 0
        tamanho_lista = len(lista_evidencias)

        while(count < tamanho_lista):
            evidencia = "results/"+str(lista_evidencias[count])
            self.documento.add_picture(evidencia, width=Inches(5.85))
            self.documento.save(doc_nome)
            count = count+1
            os.remove(evidencia)


    def ler_dados_arquivo_yaml(self):
        with open('data/dados.yaml') as arquivo:
            dados = yaml.load(arquivo, Loader=yaml.FullLoader)
            #print(dados)
    


