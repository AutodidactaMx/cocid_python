import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt

RUTA_ORIGEN = "C:/Users/Jesus/Downloads/202101010000TMed.csv"                                        

class Extraccion():
    
    def setup_method(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.vars = {}

    def wait_for_window(self, timeout = 2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def run(self):
        self.driver.get("https://smn.conagua.gob.mx/es/climatologia/temperaturas-y-lluvias/resumenes-mensuales-de-temperaturas-y-lluvias")
        time.sleep(5)

        self.driver.switch_to.frame(0)
        self.driver.find_element(By.ID, "N0").click()
        dropdown = self.driver.find_element(By.ID, "N0")
        dropdown.find_element(By.XPATH, "//option[. = '2021']").click()
        time.sleep(10)
        self.driver.find_element(By.ID, "N1").click()
        dropdown = self.driver.find_element(By.ID, "N1")
        dropdown.find_element(By.XPATH, "//option[. = 'Temperatura Media']").click()
        time.sleep(10)
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.CSS_SELECTOR, "#boton_descargar_datos > .btn").click()

        self.vars["winNueva"] = self.wait_for_window(4000)
        self.vars["winRoot"] = self.driver.current_window_handle    

        time.sleep(10)
        self.driver.close()

accion = Extraccion()
accion.setup_method()
accion.run()

df = pd.read_csv(RUTA_ORIGEN,encoding='mbcs') 
df = df[['Edo','Tmed']]
dfg = df.groupby(['Edo'])['Tmed'].agg('mean')

ax = dfg.plot(kind = 'bar')
plt.show()


  