import cv2
import numpy as np

def detectar_lineas(imagen, mode):

    if mode == True:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        
        # Aplicar el filtrado por desenfoque bilateral
        d = 15  # Diámetro del vecindario utilizado para el filtrado bilateral
        sigma_color = 25  # Valor de desviación estándar en el espacio de color
        sigma_space = 90  # Valor de desviación estándar en el espacio de coordenadas
        bilateral_filtered_image = cv2.bilateralFilter(imagen, d, sigma_color, sigma_space)

        # Aplicar el filtrado de mediana a la imagen en escala de grises
        kernel_size = 5  # Tamaño del kernel de filtrado de mediana
        median_filtered_image = cv2.medianBlur(bilateral_filtered_image, kernel_size)

        # Disminuir el brillo mediante la reducción del valor de píxeles
        #brightness_factor = 0.9  # Factor de brillo deseado (0.0 a 1.0)
        #darkened_image = np.clip(median_filtered_image * brightness_factor, 0, 255).astype(np.uint8)

        edges = cv2.Canny(median_filtered_image, threshold1=25, threshold2=120)
        cv2.imshow("gris", imagen)
        cv2.waitKey(0)
        cv2.imshow("bilateral", bilateral_filtered_image)
        cv2.waitKey(0)
        cv2.imshow("mediana", median_filtered_image)
        cv2.waitKey(0)
        cv2.imshow("filtros y brillo", edges)
        cv2.waitKey(0)
        # Aplicar la transformada de Hough para detección de líneas
        lineas = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=80, minLineLength=100, maxLineGap=10)
        return lineas

    else:      
        #Quitar/reducir ruido de la imagen
        gaussian = cv2.GaussianBlur(imagen, (5,5), 0)
        # Convertir la imagen a escala de grises
        gris = cv2.cvtColor(gaussian, cv2.COLOR_BGR2GRAY)
        #equalized_image = cv2.equalizeHist(gris)
        cv2.imshow("Gaussiana, ecualizada y gris", gris)
        cv2.waitKey(0)
        # Aplicar la detección de bordes mediante el algoritmo de Canny
        bordes = cv2.Canny(gris, 150, 200, apertureSize=3)
        cv2.imshow("bordes", bordes)
        cv2.waitKey(0)
        # Aplicar la transformada de Hough para detectar líneas
        lineas = cv2.HoughLinesP(bordes, 1, np.pi/180, threshold=250, minLineLength=100, maxLineGap=10)
        return lineas
    

#Seguimos los pasos para detectar figuras con OpenCV
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
#Simplemente vamos a iterar sobre los contornos detectados, recortarlos y mostrarlos
def tablero_recortado(imagen, contornos):
    # Mostrar únicamente las figuras recortadas que tienen una altura y longitud similares
    for contorno in contornos:
        x, y, w, h = cv2.boundingRect(contorno)
        imagen_recortada = imagen[y:y+h, x:x+w]
        
        if abs(w - h) <= 120:  # Comparar el ancho y largo de la figura recortada
            # Mostrar la figura recortada si el ancho y largo son aproximadamente iguales
            return imagen_recortada
        
    

# Cargar la imagen de entrada
#imagen = cv2.imread('C:\\Users\\sergi\\Desktop\\ProyectoChess\\Pictures\\Captura6.jpg')

# Detectar líneas utilizando la transformada de Hough
#lineas = detectar_lineas(imagen)

# Detectar las figuras geométricas a partir de las líneas
#contornos = detectar_figuras(imagen, lineas)

# Mostrar las regiones recortadas de las figuras geométricas
#mostrar_figuras_recortadas(imagen, contornos)
