import flet as ft
from time import sleep
from random import randint

def main(page: ft.Page):
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    count = ft.Text('0',size=25)
    slider = ft.Container(bgcolor=ft.colors.GREEN, width=1,height=20,border_radius=5)

    pf = ft.FilePicker()

    def num(e):
        for num in range(0,randint(1,100)):
            count.value = f'{num}%'
            slider.width = num
            page.update()
            sleep(.05)

    def pick_files_result(e: ft.FilePickerResultEvent):
        e.selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        e.selected_files.update()

    files = ft.FilePicker(on_result=pick_files_result)
    page.add(  
            ft.Column(
                [
                ft.Text('QUAL O A CHANCE DE VOCÊ DAR A BUNDA HOJE?'),
                ft.Row(
                    [
                    count,
                    slider,
                    
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.ElevatedButton("APERTE", on_click=num)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
    )
print('oi')
ft.app(main)
