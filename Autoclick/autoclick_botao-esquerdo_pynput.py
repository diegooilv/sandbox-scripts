from pynput.mouse import Button, Controller
import time

mouse = Controller()

# Tempo de espera antes de começar
time.sleep(5)

try:
    while True:
        mouse.press(Button.left)     # Pressiona o botão esquerdo do mouse
        mouse.release(Button.left)   # Solta o botão esquerdo do mouse
        time.sleep(0.2)              # Tempo entre os cliques

except KeyboardInterrupt:
    print("Autoclicker interrompido.")
