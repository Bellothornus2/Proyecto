import PySimpleGUI as psg
def ask_index_html():
    layout = [
        [psg.Text("¿desde donde quieres que empiece a coger los enlaces que tiene la página web? Si no Introduces nada, cogerá 'index.html' por defecto", size=(80,2))],
        [psg.Input(key="-INDEX-")],
        [psg.Text(key="-OUTPUT-",size=(40,1))], [psg.Button("Ok"), psg.Button('Quit')]
    ]

    window = psg.Window("Web Spider", layout)

    while True:
        event, values = window.read()
        if event == "Ok":
            if values["-INDEX-"] != "":
                web_index = values["-INDEX-"]
                break
            else:
                web_index = "index.html"
                break
        elif event == psg.WIN_CLOSED or event == "Quit":
            break
    window.close()
    return web_index