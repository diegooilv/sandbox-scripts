#include <iostream>
#include <windows.h>
#include <conio.h>

bool running = true;

// Função do autoclicker
void autoclicker() {
    while (running) {
        // Simula o clique esquerdo do mouse
        mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0);
        mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0);

        // Pausa de 0,1 segundos entre os cliques
        Sleep(100);
    }
}

// Função para monitorar o atalho de teclado (Ctrl + P)
void monitorShortcut() {
    while (true) {
        // Verifica se Ctrl + P foi pressionado
        if (GetAsyncKeyState(VK_CONTROL) && GetAsyncKeyState('P')) {
            running = false; // Para o autoclicker
            break;
        }
        Sleep(50); // Aguarda um pouco antes de verificar novamente
    }
}

int main() {
    // Cria duas threads: uma para o autoclicker e outra para monitorar o atalho
    CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)autoclicker, NULL, 0, NULL);
    monitorShortcut();

    std::cout << "Autoclicker interrompido." << std::endl;
    return 0;
}
