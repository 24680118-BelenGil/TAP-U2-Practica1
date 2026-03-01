# Juego Piedra - Papel - Tijeras
Crea un programa del juego piedra-papel o tijeras, donde jugaras contra el dispositivo de tu eleccionya sea com una apk o un sitio wed.
## Programa
Usaremos el entorno virtual flet creado anteriormente, abrimos Visual Studio Code e ingresamos a la carpeta del entorno virtual para crear otor archivo llamado **main.py**, donde escribiremos nuestro codigo del juego.
### Librerías
 ```bash
import flet as ft
import random
  ```
### Configuración de Página
 ```bash
def main(page: ft.Page):
    page.title = "Piedra, Papel o Tijera"
    page.bgcolor = "#0C1214"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
  ```
### Definición de variables
 ```bash
    resultado = ft.Text(size=20, weight=ft.FontWeight.BOLD)

    opciones = ["Piedra", "Papel", "Tijera"]
  ```
### Función Jugar
 ```bash
    def jugar(e):
        eleccion_usuario = e.control.data
        eleccion_pc = random.choice(opciones)

        if eleccion_usuario == eleccion_pc:
            mensaje = "¡Empate!😒"
        elif (
            (eleccion_usuario == "Piedra" and eleccion_pc == "Tijera") or
            (eleccion_usuario == "Papel" and eleccion_pc == "Piedra") or
            (eleccion_usuario == "Tijera" and eleccion_pc == "Papel")
        ):
            mensaje = "¡Ganaste! 🎉"
        else:
            mensaje = "Perdiste 😢"

        resultado.value = f"😘Tú: {eleccion_usuario}\n 💻PC: {eleccion_pc}\n\n{mensaje}"
        page.update()
  ```
### Botones
 ```bash
    botones = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.ElevatedButton(
                content=ft.Text("Piedra"),
                style=ft.ButtonStyle(
                bgcolor=ft.Colors.WHITE),
                icon=ft.Icons.LANDSCAPE,
                icon_color=ft.Colors.GREY,
                data="Piedra",
                on_click=jugar
            ),
            ft.ElevatedButton(
                content=ft.Text("Papel"),
                style=ft.ButtonStyle(
                bgcolor=ft.Colors.GREY),
                icon=ft.Icons.DESCRIPTION,
                icon_color=ft.Colors.WHITE,
                data="Papel",
                on_click=jugar
            ),
            ft.ElevatedButton(
                content=ft.Text("Tijera"),
                style=ft.ButtonStyle(
                bgcolor=ft.Colors.WHITE),
                icon=ft.Icons.CONTENT_CUT,
                icon_color=ft.Colors.RED,
                data="Tijera",
                on_click=jugar
            ),
        ],
    )
  ```
### Interfaz Gráfica
 ```bash
    page.add(
        ft.Text("Elige una opción:", size=18),
        botones,
        resultado
    )


ft.app(target=main)
  ```
### Resultado
[Da click aquí para ver el código](./juego.py)
## APK
Ahora contruiremos nuestra **apk** para android, para ello necesitaremos intallar Android Studio y Flutter desde sus sitios oficiales.

Android Studio:
https://developer.android.com/studio?hl=es-419

flutter:
https://docs.flutter.dev/learn/pathway/quick-install
### Resultado
## WED
### Resulado
