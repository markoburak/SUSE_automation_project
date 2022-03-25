import logging
import unittest

from config import WEBPAGE
from UISelectors import general_selectors

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager


class SeleniumTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Chrome(ChromeDriverManager().install())
        cls.driver.get(WEBPAGE)
        cls.driver.maximize_window()

    def test_initial_window(self):
        # get the link of main page
        curr_page = self.driver.current_url
        self.assertEqual(curr_page, "https://electron-react-boilerplate.js.org/")

    def test_title(self):
        try:
            # get the title by the selector
            title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, general_selectors['main_screen']['title'])
                )
            )
            # check if text of the title element is correct
            self.assertEqual(title.text, "Electron React Boilerplate")
        except TimeoutException:
            logging.error("Failed to find title element")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
