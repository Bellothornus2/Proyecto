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