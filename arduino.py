import librosa
import numpy as np
import time
import pygame
import serial 
import time 
import os 

puerto= "COM4"

arduino=serial.Serial(puerto,9600,timeout=1)

ruta=os.getcwd()

# Ruta del archivo de música que deseas cargar
ruta_musica=ruta+'\MarioBros.mp3'

# Cargar la música y obtener la señal de audio y la tasa de muestreo
y, sr = librosa.load(ruta_musica)

# Dividir la música en segmentos de 1 segundo (puedes ajustar la duración según tus necesidades)
segment_duration = 0.5  # 1 segundo
segment_samples = int(sr * segment_duration)
num_segments = len(y) // segment_samples


# Función para clasificar la frecuencia de un segmento de audio
def clasificar_frecuencia(segment):
    # Calcular la transformada de Fourier de corto plazo (STFT) del segmento
    stft = np.abs(librosa.stft(segment))

    # Calcular la energía en diferentes frecuencias (por ejemplo, baja, media, alta)
    energias = np.sum(stft, axis=0)

    # Clasificar la frecuencia en función de la energía
    print(np.mean(energias))
    media_energia = np.mean(energias)

    if media_energia > 500:  # Ajusta este umbral según tus necesidades
        return "alta"
    elif media_energia > 300:  # Ajusta este umbral según tus necesidades
        return "media"
    else:
        return "baja"


# Procesar cada segmento de audio y clasificar la frecuencia

pygame.mixer.init()
pygame.mixer.music.load(ruta_musica)
pygame.mixer.music.play()


for i in range(num_segments):
    segment = y[i * segment_samples : (i + 1) * segment_samples]
    frecuencia = clasificar_frecuencia(segment)
    if(frecuencia=="alta"):
        arduino.write('1'.encode())
    elif(frecuencia =='baja'):
        arduino.write('2'.encode())
    else:
        arduino.write('3'.encode())
    time.sleep(0.5)
    print(f"Segmento {i+1}: Frecuencia {frecuencia}")




""" 

while True :
    comando =input("Ingrese 1 para encender el led ")
    
    arduino.write(comando.encode())
    time.sleep(0.1)
    
    respuesta = arduino.readline().decode().strip()

    print("Respuesta de arduino: ",respuesta) """