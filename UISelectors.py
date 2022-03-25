id_selector = lambda id_: f"[id='{id_}']"
class_selector = lambda class_: f"[class='{class_}']"

general_selectors = {
    "main_screen": {
        "title": f"h1{class_selector('hero__title')}"
    }
}
