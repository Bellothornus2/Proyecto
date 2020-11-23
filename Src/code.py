import urllib.request
def gethtml(url):
    request = urllib.request.urlopen('http://localhost:8000/Menus')
    #si tiene el charset puesto:
    #html = request.read().decode(request.headers.get_content_charset())
    #si no:
    html = request.read().decode('utf-8')
    return html

url = "http://localhost:8000/"
html = gethtml(url)

def get_next_link(page):
    #encuentra el primer enlace desde la posición 0 
    #del parámetro "page"
    start_link = page.find('<a href=')
    #si no lo encuetra me asigna nada en la URL
    #y 0 en la posición
    if start_link == -1:
        url = None
        endpos = 0
    #si lo encuentra, entonces me busca el enlace entre la etiqueta
    #<a> HTML, cambia el parámatero
    else:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
    return url, end_quote

list_links = []

def print_all_links(page):
    while True:
        url, endpos = get_next_link(page)
        if url:
            list_links.append(url)
            page = page[endpos:]
        else:
            break

print_all_links(page)