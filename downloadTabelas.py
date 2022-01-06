from browserconfig import Browserconfig
import time
encoding = "utf-8"

def downloadTabela(x):
    print('downloadTabela')
    driver = Browserconfig.browser(True)

    link = "https://repositorio.seade.gov.br/dataset/1bd90672-72a8-47cb-a34d-ab9eb703735d/" \
        "resource/1c756209-59d3-44bf-9887-539e6a157309/download/tab_pib_"+ str(x) +".xlsx"
    print(link)
    driver.get(link)
    time.sleep(3)