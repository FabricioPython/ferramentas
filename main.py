import flet as ft
import keyboard

# testes com flet
# pyinstaller --onefile --noconsole main.py

def main(page: ft.Page):
    page.title = "Contador IMB - BYFAB"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.chave = True
    page.bgcolor = '#219ebc'
    page.theme = ft.Theme(color_scheme_seed='#023047')
    page.dark_theme = ft.Theme(color_scheme_seed=ft.Colors.BLUE)


    count = ft.Text(
            "0",
            size=20,
            color=ft.Colors.WHITE,
            weight=ft.FontWeight.NORMAL,
        )
    
    def set_number(e):
        if not len(txt_number.value) == 0:
            count.value = int(txt_number.value)
            txt_number.value = ''
            page.update()

        
    def off(e):
        page.chave = False
        page.update()


    def on(e):
        page.chave = True
        page.update()


    txt_number = ft.TextField(text_align=ft.TextAlign.RIGHT, width=100)

    dlg = ft.AlertDialog(
    title=ft.Text("Defina um número:", size=20),
    content=txt_number,
    alignment=ft.alignment.center,
    on_dismiss=set_number,
    title_padding=ft.padding.all(25))

    page.update()


    def on_key_press(event):

        #print(f'Tecla pressionada: {event.name}')
        if event.name == 'shift' and page.chave == True:
            count.value = str(int(count.value) + 1)
            page.update()



    
    keyboard.on_press(on_key_press)

    page.add(
        ft.Row([count],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(
            [
                ft.FilledButton(text="On", on_click=on),
                ft.FilledButton(text="Pause", on_click=off, bgcolor='red'),

            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        ),
        ft.Row([
        ft.FilledButton(text="Set", 
                        on_click=lambda e: page.open(dlg),
                          bgcolor='#023047')],
                          alignment=ft.MainAxisAlignment.CENTER)

    )
    


ft.app(main)