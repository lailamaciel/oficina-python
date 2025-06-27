import pandas as pd
import pyautogui 
import time

tabela = pd.read_csv("alunos.csv")

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("http:simplificapython.com.br/cadastroalunos/index.html")
pyautogui.press("enter")

pyautogui.press("tab")
pyautogui.write("admin")
pyautogui.press("tab")
pyautogui.write("SimplificaPython")
pyautogui.press("enter")



for linha in tabela.index:
    pyautogui.click(x=854, y=344)
    nome = tabela.loc[linha, "Nome"]
    pyautogui.write(str(nome))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "Email"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "Endereco"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "Telefone"]))
    pyautogui.press("tab")
    
    pyautogui.press("enter")

    pyautogui.scroll(5000)



