from selenium import webdriver
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt
import time
import pandas as pd
import numpy as np

driver = webdriver.Chrome('./chromedriver')
driver.get("https://twitter.com/search?q=%23IndigoByRM&src=trend_click&vertical=trends")
driver.set_window_size(1918, 1078)
time.sleep(5)
driver.execute_script("window.scrollTo(0,1000)")
time.sleep(5)

twiter = {}

likes_trends = []
retweet_trends = []
reply_trends = []

ele_like = driver.find_elements(By.XPATH, "//div[contains(@data-testid,'like')]//span[contains(@data-testid,'app-text-transition-container')]")
ele_retweet = driver.find_elements(By.XPATH, "//div[contains(@data-testid,'retweet')]//span[contains(@data-testid,'app-text-transition-container')]")
ele_reply = driver.find_elements(By.XPATH, "//div[contains(@data-testid,'reply')]//span[contains(@data-testid,'app-text-transition-container')]")

for x in ele_like:            
    likes_trends.append(x.text)
for x in ele_retweet:            
    retweet_trends.append(x.text)                                                   
for x in ele_reply:    
    reply_trends.append(x.text)
driver.close()

twiter["likes"] = likes_trends
twiter["retweet"] = retweet_trends
twiter["reply"] = reply_trends

df = pd.DataFrame(twiter)
df = df.replace(np.nan, '0', regex=True)
df["likes"] = df["likes"].apply( lambda x: x.replace('.','').replace('','0')).astype(int)
df["retweet"] = df["retweet"].apply( lambda x: x.replace('.','').replace('','0')).astype(int)
df["reply"] = df["reply"].apply( lambda x: x.replace('.','').replace('','0')).astype(int)
df["bandera"] = "twiter"
dfg = df.groupby(['bandera']).sum()
ax = dfg.plot(kind = 'bar')
plt.show()

