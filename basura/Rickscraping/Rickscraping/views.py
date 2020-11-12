from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
import pymongo
import dns
from . import variables
from . import funciones
class HomeView(View):
    def home(request):
        return render(request, "home.html")

class MenuView(View):
    def menu(request):
        return render(request, "menus.html")

class ScrapingView(View):
    def scraping(request):
        url = "http://localhost:8000/Menus"
        view = funciones.gethtml(url)
        #primero preparamos el texto:
        view_procesado = view.replace("\n","").replace("> ",">").replace(" <","<")
        #PRUEBA
        lista_etiquetas = ["h1","h2","li","lh","p"]
        valores = []
        for etiqueta in lista_etiquetas:
            if not funciones.ThisTagExists(view_procesado,etiqueta):
                valores.append([etiqueta,False])
                continue
            else:
                length = funciones.GetTagLength(etiqueta,view_procesado)
                etiqueta_array = [etiqueta,[]]
                if length > 1:
                    for count in range(length):
                        if count == 0:
                            continue
                        content = funciones.HomeMadeGetText(etiqueta,view_procesado,count)
                        etiqueta_array[1].append(content)
                    valores.append(etiqueta_array)
                else:
                    count=1
                    content = funciones.HomeMadeGetText(etiqueta,view_procesado,count)
                    valores.append([etiqueta,content])
        #FIN PRUEBA
        arg = {
            'json':valores
        }
        return render(request, "scraping.html", arg)

class SubidaView(View):
    def subida(request):
        #Aquí haremos el comando para subir el Json a la base de datos
        client = pymongo.MongoClient("mongodb+srv://m001-student:m001-mongodb-basics@sandbox.jhgbt.gcp.mongodb.net/admin?retryWrites=true&w=majority")
        db = client.sample_training
        
        #lo de abajo es una prueba, no se sabe muy bien que hacer
        #por eso lo hago manual
        insertado = db.menus.insert_one(variables.objeto)
        args = {
            "objeto":variables.objeto
        }
        client.close()
        return render(request, "subida.html", args)