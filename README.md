<p align="center">
  <img width="150px" src="https://i.ibb.co/bXvzjXm/LOGO-h1.png" alt="Logo del proyecto" />
</p>

# 14 FEBRERO
---

Este es un proyecto en Flask que utiliza OpenCV y MediaPipe para detectar rostros en tiempo real a través de una cámara y superponer un emoji sobre ellos.

## Requisitos

Asegúrate de tener instalado Python 3 y los siguientes paquetes antes de ejecutar el proyecto:

```sh
pip install flask opencv-python mediapipe
```

También necesitarás un archivo de imagen llamado `angry_emoji.png` en la misma carpeta del script para superponerlo en los rostros detectados.

## Uso

1. Clona este repositorio o descarga el archivo.
2. Coloca `angry_emoji.png` en la misma carpeta del script.
3. Ejecuta la aplicación con:
   
   ```sh
   python app.py
   ```
4. Abre un navegador y ve a `http://localhost:5000/` para ver el streaming de video.

## Archivos principales

- `app.py`: Script principal que maneja la detección facial y el servidor Flask.
- `templates/index.html`: Página principal donde se muestra el video en tiempo real.
- `angry_emoji.png`: Imagen del emoji que se superpone en los rostros detectados.

## Explicación del código

- **Captura de video:** Se usa OpenCV para acceder a la cámara.
- **Detección de rostros:** MediaPipe detecta las caras en el fotograma.
- **Superposición de emoji:** Se redimensiona la imagen y se coloca sobre el rostro detectado.
- **Interfaz Web:** Flask transmite el video procesado en tiempo real a través de una ruta `/video_feed`.

## Notas adicionales

- La aplicación usa `cv2.VideoCapture(0)`, por lo que debe ejecutarse en un entorno con una cámara disponible.
- Si el programa no detecta la imagen `angry_emoji.png`, asegúrate de que está en el directorio correcto y tiene un fondo transparente si es necesario.

## Autor

Creado por Miguel.

---

¡Disfruta del proyecto! 🚀

