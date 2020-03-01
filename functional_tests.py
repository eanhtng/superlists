from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser =webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes to
        # check out its hompage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straitght away

        # She types "Buy peacock feathres" into a text box (Edith's hobby is tying fly-fishing lures)

        # When she hits enter, the page updates, and now the pgae lists "1: Buy peacock feathers" as an item in a to-do lists

        # There is still a text box inviting her to add another item. She enters "Use peacock feathres to make fly" (Edith is very methodical)

        # The page updates again, and now shows both items on her lists

        # Edith wonders whether the site will remimber her lists. Then she sees that the site has generated a unique URL for her -- there is some explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings = 'ignore')
