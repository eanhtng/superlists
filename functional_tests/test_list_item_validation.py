
from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    @skip
    def tets_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        # The home page refershes, and there is an error message saying
        # that list items cannot be blank
        # She tries agian with  some text for the item, which now works
        # Persersely, she now decides to submit a second blank list item
        # She receivies a similar warning on the list page
        # And she can correct it by filling some text in
        self.fail('write me!')
