import PySimpleGUI as psg
def ask_class_html():
    list_class = []
    layout = [
        [psg.Text("que clases css quieres buscar dentro de la pagina web?")],
        [psg.Input(key="-CSSCLASS-")],
        [psg.Text("Utiliza este input para eliminar los datos que hayas introducido mal")],
        [psg.Input(key="-POP-"), psg.Button("Eliminar")],
        [psg.Text(key="-POPERROR-", size=(40,1), text_color="red")],
        [psg.Text(key="-OUTPUT-",size=(40,4))], [psg.Button("Ok"), psg.Button('Parar de introducir datos')]
    ]

    window = psg.Window("Web Spider", layout)

    while True:
        event, values = window.read()
        if event == "Ok":
            if values["-CSSCLASS-"] != "":
                list_class.append(values["-CSSCLASS-"])
                window["-OUTPUT-"].update("Has introducido esto:" + str(list_class))
                window["-POPERROR-"].update("")
            else:
                window["-OUTPUT-"].update("No has introducido nada!")
        elif event == "Eliminar":
            try:
                del list_class[list_class.index(values["-POP-"])]
                window["-POP-"].update("")
                window["-OUTPUT-"].update("Has introducido esto:" + str(list_class))
            except ValueError as e:
                window["-POPERROR-"].update("Error: " + e)
        elif event == psg.WIN_CLOSED or event == "Parar de introducir datos":
            break
    window.close()
    return list_class