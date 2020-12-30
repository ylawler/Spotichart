import Project.WebScrapeCharts as ws


# -------------------------------------- TESTING ------------------------------------------
import unittest

class test_WebScrapeCharts(unittest.TestCase):


	def setup_webscrape(self):
		self.ws = ws.WebScrapeCharts()
		self.country_code = 'nl'
		self.recurrence = 'daily'
		self.filename = None


	def check_file(self, filename):
		try:
			with open(filename,'r') as rf:
				lines = rf.readlines()
				counter = len(lines)
				return counter == 200
		except:
			return False

	def set_filename(self):
		self.filename = 'test_' + self.country_code + '_' + self.recurrence + '.txt'


	### TEST FUNCTIONS

	def test_get_charts(self):
		self.setup_webscrape()
		self.assertTrue(self.ws.get_charts(self.country_code, self.recurrence))
		self.assertEqual(self.ws.url,'https://spotifycharts.com/regional/nl/daily/latest')

	def test_get_charts_fail(self):
		self.setup_webscrape()
		self.country_code = 'jo'
		self.recurrence = 'daiy'
		self.assertFalse(self.ws.get_charts(self.country_code, self.recurrence))

	
	def test_is_empty(self):
		self.setup_webscrape()
		self.assertTrue(self.ws.is_empty())
		# get the charts
		self.ws.get_charts(self.country_code, self.recurrence)
		self.assertFalse(self.ws.is_empty())

	### TEST SAVING -> done Manually as it creates files
	def test_saving_for_testing(self):
		self.setup_webscrape()
		# USE DIFFERENT COUNTRY CODE AND RECURRENCE
		self.country_code = 'au'
		self.recurrence = 'weekly'
		self.set_filename()

		# Double check not that the file already exists and this test runs into an error
		if not self.check_file(self.filename):
			self.assertTrue(self.ws.save_for_testing(self.country_code, self.recurrence))
			self.assertTrue(self.check_file(self.filename))

	def test_saving_for_testing_fail(self):
		self.setup_webscrape()
		self.country_code = 'ik'
		self.recurrence = 'day'

		self.assertFalse(self.ws.save_for_testing(self.country_code, self.recurrence))



	def test_load_ids_from_file(self):
		self.setup_webscrape()
		self.country_code = 'de'
		self.recurrence = 'daily'
		self.set_filename()

		if self.check_file(self.filename):
			# file exists test the loading ids
			# test whether self.ws is empty
			self.assertTrue(self.ws.is_empty())
			# Test if ids are successfully loaded from file
			self.assertTrue(self.ws.load_ids_from_file(self.country_code, self.recurrence))
			# Test if self.ws is not empty
			self.assertFalse(self.ws.is_empty())

	def test_load_ids_fail(self):
		self.setup_webscrape()
		self.country_code = 'jo'
		self.recurrence = 'dail'
		self.set_filename()

		self.assertFalse(self.ws.load_ids_from_file(self.country_code, self.recurrence))

	def test_load_ids_is_full_fail(self):
		self.setup_webscrape()
		self.country_code = 'us'
		self.recurrence = 'daily'
		self.set_filename()
		self.ws.save_for_testing(self.country_code, self.recurrence)

		self.assertFalse(self.ws.load_ids_from_file(self.country_code, self.recurrence))

	def test_set_default(self):
		self.setup_webscrape()
		self.assertFalse(self.ws.get_charts('jo', 'daily'))
		self.assertEqual(self.ws.url, 'https://spotifycharts.com/regional/jo/daily/latest')

		self.ws.set_default()
		self.assertEqual(self.ws.url, 'https://spotifycharts.com/regional/')


if __name__ == '__main__':
	unittest.main()
