import PySimpleGUI as psg
def ask_web_page():
    layout = [
        [psg.Text("Elige que sitio web quieres scrapear, si no, se scrapeará uno por defecto (http://localhost:5000)")],
        [psg.Input(key="-WEBPAGE-")],
        [psg.Text(key="-OUTPUT-",size=(40,2))], [psg.Button("Ok"), psg.Button('Quit')]
    ]

    window = psg.Window("Web Spider", layout)

    while True:
        event, values = window.read()
        if event == "Ok":
            if values["-WEBPAGE-"] != "":
                webpage=values["-WEBPAGE-"]
            else:
                webpage="http://localhost:5000/"
            break
        elif event == psg.WIN_CLOSED or event == "Quit":
            break
    window.close()
    return webpage