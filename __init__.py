import datetime
import time
from src.models.ProcessaWebdriver import ProcessaWebdriver
from src.models.ProcessaSMTP import ProcessaSMTP
from src.utils.appData import appData

def run(): 
    
    try:
        
        webDriver = ProcessaWebdriver(appData()['url'], appData()['loginSentry'])
        indice = 1
        while True:
            print('Iniciando...')
            try:
                dataWeb = webDriver.leituraHTML(indice)
                time.sleep(4)
                ProcessaSMTP(appData()['smtp'], dataWeb['OBJETO'], dataWeb['STATUS'])
                indice += 1
            except Exception:
                break
        print('fim de processamento.')
        webDriver.webClose()
            
    except Exception as e:
        print(e)
        pass
               
 
run()   
