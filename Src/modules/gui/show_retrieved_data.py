import PySimpleGUI as psg
import pymongo
from ..json.transform_json import transform_json_data
from ..json.save_json import save_json_file
from ..json.pretty_json_homemade import pretty_json_homemade


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
        if event == "Archivo Json":
            dict_class_html_row = {}
            dict_class_html_row = transform_json_data(dict_class_html_row, dict_class_html, list_class_html)
            save_json_file(dict_class_html_row)
            break
        elif event == "MongoDBAtlas":
            #we transform the data for MongoDBAtlas
            dict_class_html_row = {}
            dict_class_html_row = transform_json_data(dict_class_html_row, dict_class_html, list_class_html)
            #Here we are connecting to the server
            client = pymongo.MongoClient("mongodb+srv://m001-student:m001-mongodb-basics@sandbox.jhgbt.gcp.mongodb.net/admin?retryWrites=true&w=majority")
            #Here we are connecting to the database
            db = client.amenities
            #Here we are connecting to the collection
            collection = db.packs2
            #here we are inserting the retrieved data
            insertado = collection.insert_one(dict_class_html_row)
            client.close()
            break
        elif event == psg.WIN_CLOSED or event == "Quit":
            break
    window.close()