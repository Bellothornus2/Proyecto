from .get_next_link import get_next_link
from .retrieve_directory_if_any import retrieve_directory_if_any
#This function Stores all the Links contained in a single HTML File (in this case HTML page)
def get_all_links(page, list_links):
    assert page != "" and isinstance(list_links, list)
    while True:
        string_url, endpos = get_next_link(page)
        if string_url:
            string_parent_diectory, string_url = retrieve_directory_if_any(string_url, list_links)
            if string_url == '#' or string_parent_diectory + string_url in str(list_links) or ".." in string_parent_diectory:
                page = page[endpos+1:]
                continue
            else:
                list_links.append(string_parent_diectory + string_url)
                page = page[endpos:]
        else:
            break