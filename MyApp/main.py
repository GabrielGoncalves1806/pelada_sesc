from typing import Any, List
import flet as ft
from api import update_players
from datetime import date

class HomePage(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.date = date.today()
        self.players_list = ft.ListView([])
        

    def update_list(self):
        self.players_list.controls.clear()
        players = update_players()
        if players != None:
            for pos,player in enumerate(players):
                self.players_list.controls.append(ft.Text(f'{pos+1} - {player}'),)
            print(players)
            self.page.update()
            self.page.add(self.players_list)
            self.page.update()
        else:
            self.page.update()
            self.page.add(self.players_list)


    def build(self):

        return ft.Column(
                [   
                ft.Container(
                    bgcolor=ft.colors.GREY_800, 
                    height=50,
                    width=1000, 
                    border_radius=10,
                    alignment= ft.alignment.center,
                    content=ft.Text(f'Pelada Sesc {self.date}'),
                    ),        
                    
                ft.Row(
                    [
                        ft.ElevatedButton("Adicionar nome a lista"),
                        ft.IconButton(ft.icons.REFRESH, on_click=lambda _: self.update_list())
                    ],
                    alignment= ft.MainAxisAlignment.CENTER
                ),

                self.players_list
                
                ]
        )
    
class Payment(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        pass
                
def main(page: ft.Page):

    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    myapp = HomePage()
    page.views.append(myapp)
    page.update()

ft.app(target=main)