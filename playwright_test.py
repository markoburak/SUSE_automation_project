from config import WEBPAGE
from UISelectors import general_selectors


def test_initial_window(page):
    page.goto(WEBPAGE)
    assert page.url == 'https://electron-react-boilerplate.js.org/'


def test_title(page):
    page.goto(WEBPAGE)
    title = page.locator(general_selectors['main_screen']['title']).text_content()
    assert title == "Electron React Boilerplate"
