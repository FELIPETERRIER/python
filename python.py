
#https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time


#pyautogui.PASE = 0.5
time.sleep(1.5)

pyautogui.click(x=848, y=752)

pyautogui.click(x=445, y=437)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=439, y=373)
pyautogui.write("felipeterrier@yahoo.com.br")

pyautogui.press("tab")
pyautogui.write("banana")
pyautogui.press("tab")
pyautogui.press("enter")



import pandas as pd 

tabela = pd.read_csv("produtos.csv")

print(tabela)



for linha in tabela.index:
   
    pyautogui.click(x=653, y=294)
    
    codigo = tabela.loc[linha, "codigo"]
    
    pyautogui.write(str(codigo))
    
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") 
    
    pyautogui.scroll(5000)
   

