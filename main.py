import cv2
import numpy as np
import mss

def capturar_tela():
    with mss.mss() as sct:
        while True:
            # Captura a tela usando o mss
            screenshot = sct.grab(sct.monitors[1])  # Captura do primeiro monitor (monitor 1)

            # Converte a imagem para um formato que o OpenCV pode manipular (array NumPy)
            frame = np.array(screenshot)

            # Converte de RGBA (mss) para BGR (OpenCV usa BGR como padrão)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)

            # Exibe o frame na janela
            cv2.imshow('Tela ao Vivo', frame)

            # Aguarda por uma tecla, e se for a tecla 'q', sai do loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Fecha todas as janelas do OpenCV
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capturar_tela()
