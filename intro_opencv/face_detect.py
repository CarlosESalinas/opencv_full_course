import cv2 as cv

# Leer la imagen desde el archivo
img = cv.imread('assets/group 1.jpg')
cv.imshow('People group', img)

# Convertir la imagen a escala de grises
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Lady', gray)

# Cargar el clasificador de Haar para detección facial
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# Detectar caras en la imagen en escala de grises
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
print(f'Number of faces found = {len(faces_rect)}')

# Dibujar rectángulos alrededor de las caras detectadas en la imagen original
# Iterar sobre las coordenadas (x, y, ancho, alto) de cada cara detectada
for (x, y, w, h) in faces_rect:
    
    # Dibujar un rectángulo alrededor de la cara en la imagen original
    # - La función cv.rectangle toma la imagen original 'img'
    # - Las coordenadas del vértice superior izquierdo son (x, y)
    # - Las coordenadas del vértice inferior derecho son (x+w, y+h)
    # - El color del rectángulo es (0, 255, 0) que representa verde en el formato BGR
    # - El grosor del rectángulo es 2 píxeles
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

# Mostrar la imagen con los rectángulos dibujados alrededor de las caras detectadas
cv.imshow('Detected Faces', img)

# Esperar hasta que se presione una tecla (0 indica esperar indefinidamente)
cv.waitKey(0)