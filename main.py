import os
import pyautogui
from time import sleep
from dotenv import load_dotenv
from funcao_buscar_img import clica_na_img

pyautogui.FailSafeException

load_dotenv()

SENHA_DISCORD = os.getenv('SENHA_DISCORD')
SENHA_SPOTIFY = os.getenv('SENHA_SPOTIFY')

# Abrindo E-mails

clica_na_img('icone_email')
sleep(4)

# Abrindo Google Chrome

clica_na_img('icone_chrome')
sleep(4)
pyautogui.hotkey('ctrl', 'l')
pyautogui.write('google', interval=0.10)
sleep(1)
pyautogui.press('space')
pyautogui.press('backspace')
pyautogui.press('enter')
sleep(1)
clica_na_img('icone_google')
sleep(3)

# Abrindo Google Calendar

pyautogui.hotkey('ctrl', 't')
pyautogui.hotkey('ctrl', 'l')
pyautogui.write('google calendar', interval=0.10)
sleep(1)
pyautogui.press('space')
pyautogui.press('backspace')
pyautogui.press('enter')
sleep(1)
clica_na_img('google-calendar')
sleep(3)

# Abrindo o Jornal Online de notícias

pyautogui.hotkey('ctrl', 't')
pyautogui.hotkey('ctrl', 'l')
pyautogui.write('globo.com', interval=0.10)
sleep(1)
pyautogui.press('space')
pyautogui.press('enter')
sleep(3)

# Abrindo site treinamento digitação

pyautogui.hotkey('ctrl', 't')
pyautogui.hotkey('ctrl', 'l')
pyautogui.write('edclub.com', interval=0.10)
sleep(1)
pyautogui.press('space')
pyautogui.press('enter')
sleep(5)
clica_na_img('login_edclub')
sleep(1)
clica_na_img('individual_edition')
sleep(1)
clica_na_img('login_google')
sleep(7)
# clica_na_img('supertramp')
# sleep(3)
clica_na_img('iniciar')
sleep(4)

# Abrindo o Discord (para estudos)

pyautogui.hotkey('ctrl', 'shift', 'n')
pyautogui.write('discord.com/login', interval=0.10)
pyautogui.press('space')
pyautogui.press('enter')
sleep(7)
pyautogui.write('samuelsattiro@hotmail.com', interval=0.10)
pyautogui.press('tab')
sleep(2)
# clica_na_img('robo')
# sleep(2)
pyautogui.write(SENHA_DISCORD, interval=0.10)
sleep(2)
pyautogui.press('enter')
# clica_na_img('robo')
sleep(5)


# Abrindo Spotify (música ambiente)

pyautogui.hotkey('ctrl', 't')
pyautogui.hotkey('ctrl', 'l')
pyautogui.write('open.spotify.com/intl-pt', interval=0.10)
pyautogui.press('space')
pyautogui.press('enter')
sleep(5)
clica_na_img('login_spotify')
sleep(4)
clica_na_img('entrar_email_spotify')
pyautogui.write('samuelsattiro@hotmail.com', interval=0.10)
pyautogui.press('enter')
sleep(2)
clica_na_img('entrar_senha')
sleep(2)
clica_na_img('senha_spotify')
sleep(2)
pyautogui.write(SENHA_SPOTIFY, interval=0.10)
pyautogui.press('enter')
sleep(7)
clica_na_img('escolha_spotify')
pyautogui.write('lounge music', interval=0.10)
pyautogui.press('enter')
sleep(2)
clica_na_img('biblioteca_lounge')
sleep(3)
clica_na_img('play_spotify')
sleep(5)
pyautogui.hotkey('win', 'd')

# fim


