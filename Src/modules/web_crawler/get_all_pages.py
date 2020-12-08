from .get_all_links import get_all_links
from .get_html import get_html
#This function Stores all the links from the webpage visiting all the links recursively
#discriminating the duplicates and those containing ".." in it
def get_all_pages(list_links=["index.html"],webpage="http://localhost:8000/html/"):
    for string_url in list_links:
        get_all_links(get_html(string_url,webpage), list_links)
    return list_links