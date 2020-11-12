import urllib.request
def GetTextInsideHtml(tag):
    #Destripa el Interior
    inside = tag.split("<",-1)[1].split(">",-1)[1]
    #Comprueba si en su interior hay otra etiqueta html
    inside_tag = tag.split("<",-1)[1].split(">",-1)[1].find("<")
    #si sigue habiendo una etiqueta html, sigue destripando su contenido.
    if inside_tag != -1:
        GetTextInsideHtml(inside)
    else:
        return inside

def GetTagLength(etiqueta,html):
    #Devuelve la cantidad de veces que existe esa etiqueta Html en la página web
    #quantity = len(html.split("<"+etiqueta+">",-1))
    quantity = len(html.split("<"+etiqueta,-1))
    return quantity

def HomeMadeGetText(etiqueta,html,count):
    #esto es por si hay una etiqueta html hijo dentro
    tag = html.split("<"+etiqueta,-1)[count].strip().split("</"+etiqueta+">",-1)[0]
    inside_tag = html.split("<"+etiqueta,-1)[count].strip().split("</"+etiqueta+">",-1)[0].find("<")
    #si hay una etiqueta html, destripas su interior
    if inside_tag != -1:
        tag = GetTextInsideHtml(tag)
    return tag.replace(">","")    

def gethtml(url):
    request = urllib.request.urlopen('http://localhost:8000/Menus')
    #si tiene el charset puesto:
    #html = request.read().decode(request.headers.get_content_charset())
    #si no:
    html = request.read().decode('utf-8')
    return html

def ThisTagExists(html,etiqueta):
    if html.find("<"+etiqueta+">") == -1 and html.find("<"+etiqueta) == -1:
        return False
    else:
        return True

def TranslateFromHtmlToJson(html):
    
    return "Hola"