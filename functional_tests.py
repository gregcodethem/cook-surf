from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_choose_a_website_end_template(self):
		self.browser.get('http://192.168.99.100:8000/')

		self.assertIn('Teaching Site Builder', self.browser.title)
		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main()

