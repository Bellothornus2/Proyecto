import pytest
from src.modules.web_scraper.css_class_get_content import css_class_get_content

@pytest.mark.css_class_get_content_parking_false
def test_css_class_get_content_parking_false():
    page = '<a class="test">No Parking</a>'
    string_key_class = page.find('class="' + "test" + '"')
    assert css_class_get_content(page, string_key_class) == (False, "/a>")

@pytest.mark.css_class_get_content_parking_true
def test_css_class_get_content_parking_true():
    page = '<a class="test">Parking: Yes</a>'
    string_key_class = page.find('class="' + "test" + '"')
    assert css_class_get_content(page, string_key_class) == (True, "/a>")

@pytest.mark.css_class_get_content_coupon_false
def test_css_class_get_content_coupon_false():
    page = '<a class="test">No Coupon</a>'
    string_key_class = page.find('class="' + "test" + '"')
    assert css_class_get_content(page, string_key_class) == (False, "/a>")

@pytest.mark.css_class_get_content_coupon_true
def test_css_class_get_content_coupon_true():
    page = '<a class="test">Coupon: Yes</a>'
    string_key_class = page.find('class="' + "test" + '"')
    assert css_class_get_content(page, string_key_class) == (True, "/a>")