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

#This function gets the next link from a given position from the html
def get_next_link(page):
    assert page != ""
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

#This function retrieves the parent direcotry of a link, if any
def retrieve_directory_if_any(link, list_links):
    assert link != ""
    link_splited = link.split("/")
    if len(link_splited) > 1 and not(link in list_links):
        link_without_parent = link_splited[-1]
        link_splited.remove(link_splited[-1])
        directory_parent = "/".join(link_splited)+"/"
    else:
        directory_parent = ""
        link_without_parent = link
    return directory_parent, link_without_parent

#This function Stores all the Links contained in a single HTML File (in this case HTML page)
#NOTE: we have to refactor this, this if has to be simpler
def get_all_links(page, list_links):
    assert page != "" and list_links != [] or list_links == []
    while True:
        string_url, endpos = get_next_link(page)
        if string_url:
            string_parent_diectory, string_url = retrieve_directory_if_any(string_url, list_links)
            if string_url == '#' or string_parent_diectory + string_url in list_links or ".." in string_parent_diectory:
                page = page[endpos+1:]
                continue
            else:
                list_links.append(string_parent_diectory + string_url)
                page = page[endpos:]
        else:
            break
#This function Stores all the links from the webpage visiting all the links recursively
#discriminating the duplicates and those containing ".." in it
def get_all_pages(list_links=[],webpage="http://localhost:8000/html/",url="index.html"):
    if list_links == []:
        list_links.append(url)
    for string_url in list_links:
        get_all_links(get_html(string_url,webpage), list_links)
        #list_links = list(set(list_links))