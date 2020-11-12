import urllib.request
import pdb
def gethtml(url):
    request = urllib.request.urlopen('http://localhost:8000/Menus')
    #si tiene el charset puesto:
    #html = request.read().decode(request.headers.get_content_charset())
    #si no:
    html = request.read().decode('utf-8')
    return html

url = "http://localhost:8000/Menus"
view = gethtml(url)
print(view)
pdb.set_trace()