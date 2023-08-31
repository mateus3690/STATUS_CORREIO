from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from time import sleep
class ProcessaWebdriver:
    
    def __init__(self, url, credenciais):
        
        # atributos
        self.url = url
        self.username = credenciais['login']
        self.password = credenciais['password']
        
        #atributos de configurações
        options = Options()
        options.headless = True

        self.driver = Firefox(options=options)
        
        self._boot()
    
    def _boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        
        self.login()
        
        
    def login(self):
        
        wait = WebDriverWait(self.driver, 5)
        event = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/section[2]/a[4]")))
        event.click()
        
        self.driver.find_element(By.ID, "username").send_keys(self.username)
        self.driver.find_element(By.ID, "password").send_keys(self.password)
        self.driver.implicitly_wait(0.8)
         
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/div[1]/section/div/div/form/div[2]/button").click()
        
        
    def leituraHTML(self, indice):
        print('fazendo leitura...')
        sleep(10)
        # montagem do payload
        codigo = self.driver.find_element(By.XPATH, f"/html/body/main/div[1]/div[1]/div/div[2]/section/div[1]/div/div/table/tbody/tr[{indice}]/td/div[1]/div[1]/a").get_attribute('data-codobjeto')
        description = self.driver.find_element(By.XPATH, f"/html/body/main/div[1]/div[1]/div/div[2]/section/div[1]/div/div/table/tbody/tr[{indice}]/td/div[1]/div[2]").text
        
        return {
            "OBJETO": codigo,
            "STATUS": description
        }
            
    def webClose(self):
        self.driver.close()
