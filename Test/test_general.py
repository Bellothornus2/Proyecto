from src.code import web_crawler

def test_gethtml():
    assert web_crawler.gethtml("index.html") != "" or web_crawler.gethtml("index.html") != ValueError