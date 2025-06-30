# Importar módulos necesarios de Flask y otras librerías.
# Flask: Para crear la aplicación web.
# request: Para manejar las solicitudes HTTP (POST, GET).
# send_from_directory: Para servir archivos estáticos desde un directorio.
# render_template_string: Para renderizar plantillas HTML directamente desde una cadena.
# jsonify: Para devolver respuestas JSON.
# make_response: Para crear respuestas HTTP personalizadas.
import os # Módulo para interactuar con el sistema operativo (rutas de archivos, creación de directorios).
import threading # Módulo para manejar hilos (ejecutar tareas en segundo plano).
from datetime import datetime # Módulo para obtener la fecha y hora actuales.
import cv2 # OpenCV: Librería para procesamiento de imágenes.
import numpy as np # NumPy: Librería para operaciones numéricas, especialmente con arrays.

# Inicializa la aplicación Flask.
app = Flask(__name__)

# --- Configuración de directorios ---
# Rutas fijas para guardar imágenes en un sistema Windows.
# Se recomienda usar rutas absolutas para evitar problemas.
IMAGE_DIR = r"C:\Users\USER\Documents\Embebidos\Codigo_camara - copia\ov7670\imagenes"
PROCESSED_DIR = r"C:\Users\USER\Documents\Embebidos\Codigo_camara - copia\ov7670\procesadas"

# Coordenadas de inicio para alguna lógica futura (actualmente no se usa directamente en el procesamiento).
inicio = [[1.75,1.5],[5.25,1.5],[1.75,4.5],[5.25,4.5]]

# Crear las carpetas si no existen.
# exist_ok=True evita un error si las carpetas ya están creadas.
os.makedirs(IMAGE_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

# Variables globales para el seguimiento de la última imagen procesada y un bloqueo de hilo.
last_processed_image = None # Almacena el nombre de la última imagen procesada.
lock = threading.Lock() # Un bloqueo para asegurar que solo un hilo acceda a 'last_processed_image' a la vez.

# --- Funciones de procesamiento de imágenes ---

def rgb565_to_rgb888(rgb565_bytes):
    """
    Convierte datos de imagen en formato RGB565 (16 bits por píxel) a RGB888 (24 bits por píxel).
    RGB565 es común en cámaras de bajo costo debido a su eficiencia de memoria.
    RGB888 es el formato estándar para la mayoría de las operaciones de imagen (ej. OpenCV).

    Args:
        rgb565_bytes (bytes): Secuencia de bytes que representa la imagen en formato RGB565.

    Returns:
        bytes: Secuencia de bytes que representa la imagen en formato BGR888 (OpenCV usa BGR por defecto).
    """
    result = bytearray() # Usamos bytearray para construir los bytes de manera eficiente.
    for i in range(0, len(rgb565_bytes), 2): # Iteramos cada 2 bytes, ya que cada píxel RGB565 ocupa 2 bytes.
        pixel = (rgb565_bytes[i] << 8) | rgb565_bytes[i+1] # Combina los 2 bytes para formar el valor de píxel de 16 bits.

        # Extrae los componentes R, G, B del píxel RGB565.
        # R: 5 bits más significativos.
        # G: 6 bits intermedios.
        # B: 5 bits menos significativos.
        r = (pixel >> 11) & 0x1F
        g = (pixel >> 5) & 0x3F
        b = pixel & 0x1F

        # Expande los componentes a 8 bits (0-255).
        # Esto se hace replicando los bits más significativos en los bits menos significativos.
        r = (r << 3) | (r >> 2)
        g = (g << 2) | (g >> 4)
        b = (b << 3) | (b >> 2)

        # Agrega los componentes al resultado. OpenCV espera el orden BGR.
        result.extend([b, g, r])
        # Si quisieras RGB: result.extend([r, g, b])

    return bytes(result) # Convierte el bytearray a bytes inmutables.

def save_bmp(width, height, rgb888_data, filename):
    """
    Guarda los datos de la imagen RGB888 en un archivo BMP.
    Esta función crea un encabezado BMP y luego escribe los datos de píxeles.

    Args:
        width (int): Ancho de la imagen.
        height (int): Alto de la imagen.
        rgb888_data (bytes): Datos de la imagen en formato BGR888.
        filename (str): Ruta completa del archivo BMP a guardar.
    """
    # Calcula el tamaño de una fila de píxeles, asegurando que sea un múltiplo de 4 bytes para el padding BMP.
    row_size = (width * 3 + 3) & ~3
    padding = row_size - width * 3 # Calcula el padding necesario al final de cada fila.
    bmp_data = bytearray() # Para almacenar los datos de píxeles con el padding.

    # Los archivos BMP almacenan las filas de píxeles de abajo hacia arriba.
    # Por eso se itera desde el final al principio.
    for row in range(height - 1, -1, -1):
        start = row * width * 3 # Inicio de la fila en los datos originales.
        end = start + width * 3 # Fin de la fila en los datos originales.
        bmp_data.extend(rgb888_data[start:end]) # Agrega los datos de la fila.
        bmp_data.extend(b'\x00' * padding) # Agrega el padding si es necesario.

    # Calcula el tamaño total del archivo BMP.
    file_size = 54 + len(bmp_data) # 54 bytes para el encabezado + tamaño de los datos de píxeles.

    # Crea el encabezado BMP (Bitmap File Header y DIB Header).
    # Este es un formato estándar para archivos BMP de 24 bits.
    bmp_header = bytearray([
        0x42, 0x4D, # "BM" signature
        *file_size.to_bytes(4, 'little'), # Tamaño del archivo
        0x00, 0x00, # Reservado
        0x00, 0x00, # Reservado
        0x36, 0x00, 0x00, 0x00, # Offset a los datos de píxeles (54 bytes)

        # DIB Header (BITMAPINFOHEADER)
        0x28, 0x00, 0x00, 0x00, # Tamaño del DIB Header (40 bytes)
        *width.to_bytes(4, 'little'), # Ancho de la imagen
        *height.to_bytes(4, 'little'), # Alto de la imagen
        0x01, 0x00, # Planos de color (siempre 1)
        0x18, 0x00, # Bits por píxel (24 para RGB888)
        0x00, 0x00, 0x00, 0x00, # Tipo de compresión (0 para sin comprimir)
        *len(bmp_data).to_bytes(4, 'little'), # Tamaño de los datos de la imagen
        0x13, 0x0B, 0x00, 0x00, # Resolución horizontal (píxeles por metro)
        0x13, 0x0B, 0x00, 0x00, # Resolución vertical (píxeles por metro)
        0x00, 0x00, 0x00, 0x00, # Número de colores en la paleta (0 si no se usa paleta)
        0x00, 0x00, 0x00, 0x00  # Número de colores importantes (0 si todos son importantes)
    ])

    # Escribe el encabezado y los datos de píxeles en el archivo.
    with open(filename, "wb") as f:
        f.write(bmp_header)
        f.write(bmp_data)

def process_image(filename):
    """
    Procesa una imagen BMP para detectar objetos por color y calcular su distancia.
    Guarda la imagen procesada con las detecciones dibujadas.

    Args:
        filename (str): Ruta completa del archivo BMP original a procesar.
    """
    global last_processed_image # Accede a la variable global.
    print(f"[🧠 Procesando] {filename}")
    img = cv2.imread(filename) # Lee la imagen usando OpenCV.
    if img is None: # Verifica si la imagen se leyó correctamente.
        print(f"[⚠️ Error] No se pudo leer la imagen {filename}")
        return

    # --- Preprocesamiento de la imagen ---
    # ⬇️ Opción: comenta esta parte si quieres toda la imagen
    #alto = img.shape[0]
    #img = img[:alto // 2, :] # Recorta la imagen a la mitad superior (si es necesario).
    img = cv2.flip(img, 1)  # Voltea la imagen horizontalmente (efecto espejo).
    img = cv2.flip(img, 0) # Voltea la imagen verticalmente (de arriba a abajo).

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # Convierte la imagen de BGR a HSV.
    # HSV (Hue, Saturation, Value) es un espacio de color más robusto para la detección de color.

    # --- Definición de rangos de color HSV ---
    # Diccionario con los rangos de HSV para diferentes colores.
    # Cada color puede tener múltiples rangos (ej. el rojo tiene un rango bajo y uno alto en H).
    colores = {
        "naranja": [
            ([6, 100, 100], [20, 255, 255])  # Rango de HSV para el naranja.
        ],
        "rojo": [
            ([0, 70, 50], [5, 255, 255]), # Primer rango para el rojo (parte baja del tono).
            ([170, 70, 50], [180, 255, 255]) # Segundo rango para el rojo (parte alta del tono).
        ],
        "verde": [
            ([35, 50, 50], [85, 255, 255]) # Rango para el verde.
        ],
        "azul": [
            ([90, 50, 50], [130, 255, 255]) # Rango para el azul.
        ]
    }

    cuadros = [] # Lista para almacenar los cuadros delimitadores de los objetos detectados.
    # Máscara para evitar detectar la misma región con diferentes colores (solapamiento).
    mask_usada = np.zeros(hsv.shape[:2], dtype=np.uint8)

    # --- Detección de colores y contornos ---
    for color, rangos in colores.items():
        mask_total = None
        for lower, upper in rangos:
            lower_np = np.array(lower, dtype=np.uint8)
            upper_np = np.array(upper, dtype=np.uint8)
            # Crea una máscara binaria donde los píxeles dentro del rango HSV son blancos, y el resto negros.
            mask = cv2.inRange(hsv, lower_np, upper_np)
            mask_total = mask if mask_total is None else cv2.bitwise_or(mask_total, mask) # Combina máscaras si hay múltiples rangos.

        # Eliminar regiones ya etiquetadas con otros colores.
        # Esto asegura que cada objeto sea detectado como un solo color.
        mask_final = cv2.bitwise_and(mask_total, cv2.bitwise_not(mask_usada))
        mask_usada = cv2.bitwise_or(mask_usada, mask_final) # Actualiza la máscara de regiones usadas.

        # Encuentra los contornos en la máscara final.
        # RETR_EXTERNAL: Recupera solo los contornos más externos.
        # CHAIN_APPROX_SIMPLE: Comprime segmentos horizontales, verticales y diagonales, dejando solo los puntos finales.
        contours, _ = cv2.findContours(mask_final, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            area = cv2.contourArea(cnt) # Calcula el área del contorno.
            if area > 5: # Filtra contornos pequeños (ruido).
                x, y, w, h = cv2.boundingRect(cnt) # Obtiene el cuadro delimitador (x, y, ancho, alto) del contorno.
                cuadros.append((x, y, w, h, color)) # Almacena la información del cuadro y el color.

    # --- Calibración y dibujo de resultados ---
    # K es una constante de calibración para el cálculo de distancia.
    # Puede ser determinada empíricamente: K = (distancia_real_cm * diametro_en_pixeles_a_esa_distancia)
    K = 1500

    for (x, y, w, h, color) in cuadros:
        # Define el color BGR para dibujar en la imagen según el color detectado.
        color_bgr = {
            "rojo": (0, 0, 255),    # BGR para rojo
            "naranja": (0, 140, 255), # BGR para naranja
            "verde": (0, 255, 0),   # BGR para verde
            "azul": (255, 0, 0)     # BGR para azul
        }.get(color, (255, 255, 255)) # Blanco por defecto si el color no está mapeado.

        # Dibuja un rectángulo alrededor del objeto detectado.
        cv2.rectangle(img, (x, y), (x + w, y + h), color_bgr, 2)

        # Calcula el diámetro promedio en píxeles.
        diametro_pixels = (w + h) / 2
        # Calcula la distancia en cm usando la constante K.
        distancia_cm = K / diametro_pixels if diametro_pixels > 0 else 0

        # Crea el texto a mostrar en la imagen.
        texto = f"{color} {distancia_cm:.1f}cm"
        # Dibuja el texto en la imagen.
        cv2.putText(img, texto, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color_bgr, 2)

    # --- Guardado de la imagen procesada ---
    processed_name = os.path.basename(filename).replace(".bmp", "_processed.jpg") # Crea un nuevo nombre para la imagen procesada.
    processed_path = os.path.join(PROCESSED_DIR, processed_name) # Ruta completa de la imagen procesada.
    cv2.imwrite(processed_path, img) # Guarda la imagen procesada como JPG.

    # Actualiza el nombre de la última imagen procesada de forma segura (con bloqueo de hilo).
    with lock:
        last_processed_image = processed_name
    print(f"[✔️ Procesamiento completo] Imagen guardada en: {processed_path}")

# --- Rutas de la API Flask ---

@app.after_request
def apply_cors_headers(response):
    """
    Función que se ejecuta después de cada solicitud para añadir cabeceras CORS.
    Esto permite que la API sea accedida desde diferentes dominios (útil para desarrollo web).
    También cierra la conexión después de cada solicitud.
    """
    response.headers["Access-Control-Allow-Origin"] = "*" # Permite solicitudes desde cualquier origen.
    response.headers["Connection"] = "close" # Indica al cliente que cierre la conexión.
    return response

@app.route("/upload_raw_image_flash/", methods=["POST"])
def upload_image():
    """
    Endpoint para recibir imágenes RAW (RGB565) enviadas por un dispositivo (ej. ESP32 con cámara).
    Los datos de la imagen deben incluir el ancho y alto al principio.
    """
    data = request.get_data() # Obtiene los datos binarios enviados en el cuerpo de la solicitud POST.
    if len(data) < 4: # Verifica que los datos tengan al menos 4 bytes (para ancho y alto).
        return jsonify({"status": "error", "message": "Datos insuficientes."}), 400 # Error 400 Bad Request

    # Extrae el ancho y alto de los primeros 4 bytes.
    width = int.from_bytes(data[0:2], 'big') # Ancho (primeros 2 bytes, big-endian).
    height = int.from_bytes(data[2:4], 'big') # Alto (siguientes 2 bytes, big-endian).
    image_data = data[4:] # El resto de los datos son la imagen RGB565.

    # Verifica que el tamaño de los datos de la imagen coincida con el esperado.
    if len(image_data) != width * height * 2: # Cada píxel RGB565 ocupa 2 bytes.
        return jsonify({"status": "error", "message": "Tamaño de datos incorrecto para la imagen."}), 400

    # Convierte los datos de la imagen a RGB888.
    rgb888_data = rgb565_to_rgb888(image_data)
    # Genera un nombre de archivo único basado en la fecha y hora.
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = os.path.join(IMAGE_DIR, f"img_{timestamp}.bmp") # Ruta completa para guardar la imagen BMP.
    save_bmp(width, height, rgb888_data, filename) # Guarda la imagen BMP.

    # Inicia el procesamiento de la imagen en un hilo separado.
    # Esto evita bloquear la respuesta HTTP mientras la imagen se procesa.
    # daemon=True asegura que el hilo se cerrará cuando la aplicación principal se cierre.
    threading.Thread(target=process_image, args=(filename,), daemon=True).start()

    # Prepara la respuesta JSON para el cliente.
    response = jsonify({
        "status": "ok",
        "message": f"Imagen {width}x{height} recibida y guardada",
        "filename": filename
    })
    response.headers["Connection"] = "close" # Cierra la conexión HTTP.
    return response

@app.route("/processed_image/<path:filename>")
def serve_processed_image(filename):
    """
    Endpoint para servir las imágenes procesadas.
    Permite que un navegador solicite una imagen específica por su nombre.
    """
    response = make_response(send_from_directory(PROCESSED_DIR, filename)) # Sirve el archivo desde el directorio de procesadas.
    # Cabeceras para evitar el caché del navegador, asegurando que siempre se cargue la última versión.
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

@app.route("/last_image_name")
def last_image_name():
    """
    Endpoint que devuelve el nombre de la última imagen procesada.
    Utilizado por el frontend para saber qué imagen mostrar.
    """
    with lock: # Accede a 'last_processed_image' de forma segura.
        if last_processed_image:
            full_path = os.path.join(PROCESSED_DIR, last_processed_image)
            if os.path.exists(full_path): # Verifica si el archivo realmente existe.
                return jsonify({"image_name": last_processed_image})
    return jsonify({"image_name": None}) # Devuelve None si no hay imagen procesada.

@app.route("/view_image/<image_name>")
def view_image(image_name):
    """
    Endpoint para mostrar una imagen procesada específica en una página HTML.
    Esta página se actualiza automáticamente para mostrar la última imagen si cambia.
    """
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Visualización de LEDs detectados</title>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #121212; color: #eee; text-align: center; }}
            img {{ max-width: 90%; height: auto; border: 3px solid #444; margin-top: 20px; }}
            h2 {{ margin-top: 20px; }}
        </style>
    </head>
    <body>
        <h2 id="title">Imagen Procesada: {image_name}</h2>
        <img id="processedImage" src="/processed_image/{image_name}?t={datetime.now().timestamp()}" alt="Imagen procesada" />
        <p>(Se actualiza automáticamente cuando llega una imagen nueva)</p>

        <script>
            let currentImage = "{image_name}"; // Almacena el nombre de la imagen actual.

            async function checkNewImage() {{
                try {{
                    // Realiza una solicitud al endpoint '/last_image_name' para obtener la última imagen.
                    const response = await fetch('/last_image_name');
                    const data = await response.json();
                    // Si hay una nueva imagen y es diferente a la actual:
                    if (data.image_name && data.image_name !== currentImage) {{
                        currentImage = data.image_name; // Actualiza el nombre de la imagen actual.
                        const img = document.getElementById('processedImage');
                        // Actualiza la fuente de la imagen. Se añade un timestamp para evitar el caché del navegador.
                        img.src = `/processed_image/${{currentImage}}?t=${{new Date().getTime()}}`;
                        document.getElementById('title').textContent = 'Imagen Procesada: ' + currentImage; // Actualiza el título.
                    }}
                }} catch (error) {{
                    console.error('Error al consultar la última imagen:', error);
                }}
            }}

            setInterval(checkNewImage, 1000);  // Llama a 'checkNewImage' cada 1 segundo para verificar actualizaciones.
        </script>
    </body>
    </html>
    """
    return render_template_string(html) # Renderiza la cadena HTML.

@app.route("/last_image")
def last_image():
    """
    Endpoint que redirige a la vista de la última imagen procesada si existe.
    """
    with lock: # Accede a 'last_processed_image' de forma segura.
        if last_processed_image:
            return view_image(last_processed_image) # Llama a la función que renderiza la vista de la imagen.
    return "No hay imagen procesada disponible." # Mensaje si no hay imagen.

@app.route("/")
def home():
    """
    Página de inicio del servidor, simplemente un mensaje de confirmación.
    """
    return "Servidor listo para recibir imágenes."

# --- Ejecución del servidor Flask ---
if __name__ == "__main__":
    # Inicia el servidor Flask.
    # host="0.0.0.0": Hace que el servidor sea accesible desde cualquier IP en la red.
    # port=8000: El puerto en el que el servidor escuchará las solicitudes.
    # debug=False: Deshabilita el modo de depuración (no recomendado para producción).
    # threaded=True: Permite que el servidor maneje múltiples solicitudes concurrentemente usando hilos.
    app.run(host="0.0.0.0", port=8000, debug=False, threaded=True)