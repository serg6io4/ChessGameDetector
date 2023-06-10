# ChessGameDetector
Identification of digital chessboards through artificial intelligence applied to images


En la primera versión únicamente se detectaban las líneas del tablero así como los márgenes de la imagen y demás. Era bastante ineficaz, fui variando un poco la capacidad de como se establece  los parámetros dentro de HoughLinesP, y con esto se fue manejando la cantidad detectada de líneas dentro de la imagen. Cabe resaltar que estaba muy alejado de lo que se quería buscar.

La segunda versión, fue una implementación extra a la versión 1 en la que se optaba por detectar las líneas con los parámetros establecidos anteriormente pero ahora se buscaba lo que encerraba las lineas con sus intersecciones buscando entre ellas lo más parecido a un cuadrado. 

La tercera versión se centra partiendo de la versión dos con las líneas que encierren un cuadrado, además se le añade una condición que los ángulos que formen estas líneas(esto se puede conseguir con la arcotangente que forma dos líneas rectas, aunque no sé si lo implementé del todo bien), deben ser de 90º más o menos, todo tiene umbral. Esto también me daba bastante errores y terminé por buscar algo más certero.

La cuarta versión utiliza la detección de las líneas por la trasnformada de Hough y luego busco aquellas líneas que acabo de pintar sobre la imagen que encierren la forma de un cuadrado, centrándome en su contorno, después de eso pido que se me recorten esos "cuadrados", y luego tengo un array de cuadrados, los cuales voy a clasificar y quedarme con aquellos que cumplan con que tengan más o menos mismo ancho y largo(aquí también meto un umbral y debe ser alto porque algunas imágenes no me las pilla). Con esto consigo que ya extraiga la imagen de cuadrado en su cierta medida, aunque la captura 3 falla.
