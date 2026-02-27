import pyautogui

from time import sleep

def clica_na_img(img):
    imagem = 'img/' + img + '.png'
    sleep(1)
    local_imagem = pyautogui.locateOnScreen(imagem, confidence=0.9)
    return pyautogui.click(local_imagem)