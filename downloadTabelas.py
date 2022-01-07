from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browserconfig import Browserconfig
import time
encoding = "utf-8"

def downloadTabela():
    print('downloadTabela')
    driver = Browserconfig.browser(True)

    link = "https://repositorio.seade.gov.br/dataset/pib-municipal-2002-2018"
    print(link)
    driver.get(link)
    contador = driver.find_elements(By.CSS_SELECTOR, "#dataset-resources > ul > li > a")
    for x in range(1, len(contador)):
        titulo = driver.find_element(By.CSS_SELECTOR, "#dataset-resources > ul > li:nth-child(" + str(x) + ") > a").text
        if "Tabela - PIB" in titulo:
            print(titulo)
            driver.find_element(By.CSS_SELECTOR, "#dataset-resources > ul > li:nth-child(" + str(x) + ") > div > a").click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dataset-resources > ul > li:nth-child(" + str(x) + ") > div > ul > li:nth-child(2) > a")))
            driver.find_element(By.CSS_SELECTOR, "#dataset-resources > ul > li:nth-child(" + str(x) + ") > div > ul > li:nth-child(2) > a").click()
            time.sleep(4)
