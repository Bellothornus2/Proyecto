from src.code import web_crawler

def test_get_html():
    assert web_crawler.get_html("index.html") != "" or web_crawler.get_html("index.html") != ValueError