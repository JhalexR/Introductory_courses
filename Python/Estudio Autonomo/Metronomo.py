import time
import winsound

def metronomo(bpm, duracion, tono):
    
    intervalo = 60 / bpm  # Calcula el intervalo de tiempo en segundos para el tempo dado
    while True:
        
        winsound.Beep(tono, duracion)  # Reproduce un tono
        time.sleep(intervalo - duracion / 1000)  # Espera el tiempo restante hasta el próximo tono
        
# Parámetros del metrónomo
bpm = 120  # Beats por minuto
duracion_tono = 100  # Duración del tono en milisegundos
tono = 440  # Frecuencia del tono en Hz (440 Hz es la frecuencia estándar de La)

# Llama a la función del metrónomo con los parámetros especificados
metronomo(bpm, duracion_tono, tono)