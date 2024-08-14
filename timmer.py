import pyaudio
import numpy as np
import time

# Configuración del micrófono
FORMATO = pyaudio.paInt16
CANALES = 1
RATIO = 44100
CHUNK = 1024
LIMITE= 500  # Umbral de detección de ruido

def detect_noise():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMATO, channels=CANALES, rate=RATIO, input=True, frames_per_buffer=CHUNK)
    
    print("Esperando ruido...")
    
    while True:
        data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
        peak = np.max(np.abs(data))
        if peak > LIMITE:
            stream.stop_stream()
            stream.close()
            p.terminate()
            return

def start_timer():
    print("Experimentando... Cronómetro iniciado")
    start_time = time.time()
    try:
        while True:
            elapsed_time = time.time() - start_time
            print(f"\rTiempo transcurrido: {elapsed_time:.2f} segundos", end="")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExperimento detenido")

if __name__ == "__main__":
    detect_noise()
    start_timer()
