import flet as ft
import random

def main(page: ft.Page):
    page.title = "Piedra, Papel o Tijera"
    page.bgcolor = "#0C1214"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    resultado = ft.Text(size=20, weight=ft.FontWeight.BOLD)

    opciones = ["Piedra", "Papel", "Tijera"]

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

    page.add(
        ft.Text("Elige una opción:", size=18),
        botones,
        resultado
    )

ft.app(target=main)
