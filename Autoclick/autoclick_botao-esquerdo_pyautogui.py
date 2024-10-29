import pyautogui
import time

# Tempo de espera antes de começar
time.sleep(5)

try:
    while True:
        pyautogui.click(button='left')  # Simula o clique direito do mouse
        time.sleep(0.1)  # Espera 0.1 segundo entre os cliques
except KeyboardInterrupt:
    print("Autoclicker interrompido.")
