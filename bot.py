import os
from dotenv import load_dotenv

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from urllib3.util import url

# Constants
FILE: str = ("C:\\Users\\ander\\OneDrive - Presidência da República\\"
             "Base de Dados\\Entrega Geral Completa.xlsm")
DOWNLOAD_FOLDER: str = "D:\\TEMP\\"
SHEET_NAME: str = "Geral"
load_dotenv()


class Bot:
    """
    Classe de conexão com a página do bot
    """

    def __init__(self):
        options = Options()
        options.add_experimental_option("prefs", {
            "download.default_directory": DOWNLOAD_FOLDER,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
            "detach": True,
        })
        ignored_exceptions = (NoSuchElementException,
                              StaleElementReferenceException)
        self.driver = webdriver.Chrome(options=options)


    def conecta_pagina(self, url):
        self.driver.get(url)
        return self.driver

    def realiza_login(self, username: str, password: str):
        pass


# Ler a planilha
#df = pd.read_excel(FILE, sheet_name=SHEET_NAME)


# Criar uma lista de nomes para ser consultada
#for index, row in df.iterrows():
#       print(row['CANDIDATO'])

if __name__ == "__main__":
    bot = Bot()
    bot.conecta_pagina("https://sinc.presidencia.gov.br/entrar/")
    bot.realiza_login(SINC_USERNAME, SINC_PASSWORD)
