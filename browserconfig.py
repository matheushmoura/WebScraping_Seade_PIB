from selenium import webdriver

class Browserconfig():
    def browser(headless):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {
            "download.default_directory": r"C:\Users\Matheus\Documents\PIBbrasil\SeadeFiles",  # Change default directory for downloads
            "download.prompt_for_download": False,  # To auto download the file
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True
        })
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        if headless == True:
            options.add_argument('headless')
        driver = webdriver.Chrome(options=options)
        return driver