import flet as ft
import keyboard

# testes com flet
# pyinstaller --onefile --noconsole main.py

def main(page: ft.Page):
    page.title = "Contador IMB - BYFAB"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.chave = True
  
    


    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    
    def off(e):
        page.chave = False
        page.update()

    def on(e):
        page.chave = True
        page.update()



    def on_key_press(event):

        #print(f'Tecla pressionada: {event.name}')
        if event.name == 'shift' and page.chave == True:
            txt_number.value = str(int(txt_number.value) + 1)
            page.update()



    
    keyboard.on_press(on_key_press)

    page.add(
        ft.Row(
            [
                ft.FilledButton(text="On", on_click=on),
                txt_number,
                ft.FilledButton(text="Pause", on_click=off, bgcolor='red'),

            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    


ft.app(main)