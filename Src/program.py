from modules.gui.ask_web_page import ask_web_page
from modules.gui.ask_class_html import ask_class_html
from modules.gui.ask_index_html import ask_index_html
from modules.gui.show_retrieved_data import show_retrieved_data
from modules.web_scraper.get_all_content import get_all_content


web_page = ask_web_page()
print(web_page)

list_class_html = ask_class_html()
print(list_class_html)

dict_class_html = {}
for i in list_class_html:
    dict_class_html[i] = []
print(dict_class_html)

web_index = ask_index_html()
print(web_index)

dict_class_html = get_all_content([web_index],list_class_html,dict_class_html)
print(dict_class_html)


show_retrieved_data(dict_class_html, list_class_html)

