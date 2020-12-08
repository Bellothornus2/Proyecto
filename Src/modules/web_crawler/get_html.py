#Here we import the library to download the HTMl
import urllib.request
#This function is to download the HTMl in "UTF-8" Codification from a given URI
def get_html(string_url="index.html",webpage="http://localhost:8000/html/"):
    assert string_url != ""
    try:
        request = urllib.request.urlopen(webpage + string_url)
        #si tiene el charset puesto:
        #html = request.read().decode(request.headers.get_content_charset())
        #si no:
        html = request.read().decode('utf-8')
    except:
        raise ValueError(webpage+string_url+' Doesn\'t exists or is unreachable')
    return html