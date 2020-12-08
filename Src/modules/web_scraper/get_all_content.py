from ..get_html import get_html
from .css_class_finder import css_class_finder
#Here we take all the content of the pages
def get_all_content(list_links, list_class_html, dict_class_html):
    for url in list_links:
        page = get_html(url)
        for class_html in list_class_html:
            dict_class_html = css_class_finder(page,class_html, dict_class_html)
    return dict_class_html