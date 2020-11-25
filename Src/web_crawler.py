#Here we import the library to download the HTMl
import urllib.request
#This function is to download the HTMl in "UTF-8" Codification from a given URI
def gethtml(string_url,webpage="http://localhost:8000/html/"):
    try:
        request = urllib.request.urlopen(webpage + string_url)
        #si tiene el charset puesto:
        #html = request.read().decode(request.headers.get_content_charset())
        #si no:
        html = request.read().decode('utf-8')
    except:
        raise ValueError(webpage+string_url+' Doesn\'t exists or is unreachable')
    return html

#This function gets the next link from a given position from the html
def get_next_link(page):
    #encuentra el primer enlace desde la posición 0 
    #del parámetro "page"
    start_link = page.find('<a href=')
    #si no lo encuetra me asigna nada en la URL
    #y 0 en la posición
    if start_link == -1:
        string_url= None
        end_quote = 0
    #si lo encuentra, entonces me busca el enlace entre la etiqueta
    #<a> HTML, cambia el parámatero
    else:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        string_url= page[start_quote + 1:end_quote]
    return string_url, end_quote

#This function Stores all the Links contained in a single HTML File (in this case HTML page)
def get_all_links(page, list_links):
    while True:
        string_url, endpos = get_next_link(page)
        if string_url:
            if string_url == '#' or string_url in list_links or ".." in string_url:
                page = page[endpos+1:]
                continue
            else:
                list_links.append(string_url)
                page = page[endpos:]
        else:
            break

#This function Stores all the links from the webpage visiting all the links recursively
#discriminating the duplicates and those containing ".." in it
def get_all_pages(list_links):
    for string_url in list_links:
        page = gethtml(string_url)
        get_all_links(page, list_links)
        #list_links = list(set(list_links))