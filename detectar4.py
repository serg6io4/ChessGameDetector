import cv2
import numpy as np

def detectar_lineas(imagen):
    # Convertir la imagen a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # Aplicar la detección de bordes mediante el algoritmo de Canny
    bordes = cv2.Canny(gris, 150, 200, apertureSize=3)
    
    # Aplicar la transformada de Hough para detectar líneas
    lineas = cv2.HoughLinesP(bordes, 1, np.pi/180, threshold=250, minLineLength=100, maxLineGap=10)
    
    return lineas

def detectar_figuras(imagen, lineas):
    # Crear una imagen en blanco del mismo tamaño que la imagen original
    mascara = np.zeros_like(imagen)
    
    # Dibujar las líneas encontradas sobre la máscara
    for linea in lineas:
        x1, y1, x2, y2 = linea[0]
        cv2.line(mascara, (x1, y1), (x2, y2), (255, 255, 255), 2)
    
    # Convertir la máscara a escala de grises
    gris = cv2.cvtColor(mascara, cv2.COLOR_BGR2GRAY)
    
    # Aplicar el algoritmo de detección de contornos
    contornos, _ = cv2.findContours(gris, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    return contornos

def mostrar_figuras_recortadas(imagen, contornos):
    # Mostrar únicamente las figuras recortadas que tienen una altura y longitud similares
    for contorno in contornos:
        x, y, w, h = cv2.boundingRect(contorno)
        figura_recortada = imagen[y:y+h, x:x+w]
        
        if abs(w - h) <= 100:  # Comparar el ancho y largo de la figura recortada
            # Mostrar la figura recortada si el ancho y largo son aproximadamente iguales
            cv2.imshow('Figura Recortada', figura_recortada)
            cv2.waitKey(0)
        
    cv2.destroyAllWindows()

# Cargar la imagen de entrada
imagen = cv2.imread('C:\\Users\\sergi\\Desktop\\ProyectoChess\\Pictures\\Captura2.jpg')

# Detectar líneas utilizando la transformada de Hough
lineas = detectar_lineas(imagen)

# Detectar las figuras geométricas a partir de las líneas
contornos = detectar_figuras(imagen, lineas)

# Mostrar las regiones recortadas de las figuras geométricas
mostrar_figuras_recortadas(imagen, contornos)
