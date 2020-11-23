#Here we import the library to download the HTMl
import urllib.request

#we initialize the empty list "list_links" to store all the links here
#and the varaible string "url" to store the root of the content
#we initialize the dictionary who contains the ids of the elements that we want to store 
list_links = []
url = "index.html"
dict_id_html = {
    "PricePack":None,  #Integer
    "NamePack":None,  #String 
    "ContentPack":None,  #Array of two string values
    "HasCupon":None,  #Boolean
    "HasParking":None  #Boolean
}


#This function is to download the HTMl in "UTF-8" Codification from a given URI
def gethtml(url,webpage="http://localhost:8000/html/"):
    try:
        request = urllib.request.urlopen(webpage + url)
    except:
        print(webpage + url)
    #si tiene el charset puesto:
    #html = request.read().decode(request.headers.get_content_charset())
    #si no:
    html = request.read().decode('utf-8')
    return html

#TODO:
"""
Hay que hacer tres funciones
una para coger la posicion de la etiqueta HTML
segundo para coger el texto de un atributo en concreto (da igual su posición)
tercero para coger el texto que va después de la etiqueta
o...
hacer una función para coger el id de la etiqueta
y otra función de coger el texto que hay dentro de esa etiqueta HTMl 
"""
#This function Gets then next link from a given position from the html
def scraper(page):
    start_link = page.find("id=")

def get_next_link(page):
    #encuentra el primer enlace desde la posición 0 
    #del parámetro "page"
    start_link = page.find('<a href=')
    #si no lo encuetra me asigna nada en la URL
    #y 0 en la posición
    if start_link == -1:
        url = None
        end_quote = 0
    #si lo encuentra, entonces me busca el enlace entre la etiqueta
    #<a> HTML, cambia el parámatero
    else:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
    return url, end_quote

#This function Stores all the Links contained in a single HTML File (in this case HTML page)
def print_all_links(page):
    while True:
        url, endpos = get_next_link(page)
        if url:
            if url == '#' or url in list_links or ".." in url:
                page = page[endpos+1:]
                continue
            else:
                list_links.append(url)
                page = page[endpos:]
        else:
            break

#This function Stores all the links from the webpage visiting all the links recursively
#discriminating the duplicates and those containing ".." in it
def get_all_pages(list_links):
    for url in list_links:
        page = gethtml(url)
        print_all_links(page)
        list_links = list(set(list_links))

#Here we take all th links from the root level "index.html"
page = gethtml(url)
print_all_links(page)
print(list_links)

#Then here we take all the links from all the urls from the entire webpage recursively.
get_all_pages(list_links)
print(list_links)

#odio esto!