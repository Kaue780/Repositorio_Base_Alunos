# Nome: sistema automatico
# Autor: Kauê Lima Marques
# Data: 20/05/2026
# Descrição: Programa para fazer uma entrada manual em sites aplicativos jogos e etc...

import pyautogui as pg

#pg.mouseInfo()

pg.press("win", interval=0.5)
pg.write("chrome", interval=0.2)
pg.press("enter")

pg.typewrite("youtube.com", interval=0.2)
pg.press("enter")

pg.moveTo(387,196)
pg.click()
pg.sleep(3)
pg.typewrite("Renato Garcia")
pg.press("enter")
pg.moveTo(317, 600)
pg.sleep(1.5)
pg.click()
