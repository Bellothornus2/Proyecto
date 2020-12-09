from src.modules.get_html import get_html
from src.modules.web_scraper.get_all_content import get_all_content
from src.modules.web_scraper.css_class_finder import css_class_finder
import pytest
list_class_html = [
    "PricePack",
    "NamePack",
    "ContentPack",
    "HasCupon",
    "HasParking"
]
dict_class_html = {
    "PricePack":[],
    "NamePack":[],
    "ContentPack":[],
    "HasCupon":[],
    "HasParking":[]
}

@pytest.mark.get_html
def test_get_html():
    assert get_html(string_url="index.html") != "" and get_html(string_url="index.html") != ValueError and (isinstance(get_html(string_url="index.html"),str))

@pytest.mark.get_all_content_is_dict
def test_get_all_content_is_dict():
    assert isinstance(get_all_content(["products.html"],list_class_html,dict_class_html), dict)

@pytest.mark.get_all_content_is_this
def test_get_all_content_is_this():
    assert get_all_content(["products.html"], ["NamePack"], {"NamePack":[]}) == {"NamePack":["Free Pack", "Tier 1 Pack", "Tier 2 Pack", "Tier 3 Pack", "Tier 4 Pack", "Tier 5 Pack"]}

@pytest.mark.css_class_finder_is_dict
def test_css_class_finder_is_dict():
    assert isinstance(css_class_finder(get_html(string_url="products.html"), "NamePack", dict_class_html), dict)

@pytest.mark.css_class_finder_is_this
def test_css_class_finder_is_this():
    dict_class_html = {
    "PricePack":[],
    "NamePack":[],
    "ContentPack":[],
    "HasCupon":[],
    "HasParking":[]
}
    assert css_class_finder(get_html(string_url="products.html"), "NamePack", dict_class_html) == {
    "PricePack":[],
    "NamePack":["Free Pack", "Tier 1 Pack", "Tier 2 Pack", "Tier 3 Pack", "Tier 4 Pack", "Tier 5 Pack"],
    "ContentPack":[],
    "HasCupon":[],
    "HasCupon":[],
    "HasParking":[]
}


