import PySimpleGUI as psg
from ..json.transform_json import transform_json_data
from ..json.save_json import save_json_file
from ..json.pretty_json_homemade import pretty_json_homemade
from ..json.save_atlas import save_atlas

def show_retrieved_data(dict_class_html, list_class_html):
    data = pretty_json_homemade(dict_class_html)
    col = [[psg.Text(data)]]
    layout = [
        [psg.Text("Esto son los datos que hemos podido coger, quieres guardarlos en un archivo json o en MongoDBAtlas?", size=(80,2))],
        [psg.Column(col, size=(600,500), scrollable=True)],
        [psg.Button("Archivo Json"),psg.Button("MongoDBAtlas"), psg.Button('Quit')]
    ]

    window = psg.Window("Web Spider", layout)

    while True:
        event, values = window.read()
        dict_class_html_row = {}
        dict_class_html_row = transform_json_data(dict_class_html_row, dict_class_html, list_class_html)
        if event == "Archivo Json":
            save_json_file(dict_class_html_row)
            break
        elif event == "MongoDBAtlas":
            save_atlas(dict_class_html_row)
            break
        elif event == psg.WIN_CLOSED or event == "Quit":
            break
    window.close()