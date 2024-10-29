# Wrapper object around selenium webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException, TimeoutException




class Seldump:
	def __init__(self):
		self.timeout = 10
		self.options = self.gen_options()
		self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
						options=self.options)
		self.results = []


		self.element_exceptions = ( NoSuchElementException, TimeoutException )

	def gen_options(self):
		chrome_options = Options()
		chrome_options.binary_location = "/usr/bin/google-chrome"
		chrome_options.add_argument("--no-sandbox")
		#chrome_options.add_argument("--headless")
		chrome_options.add_argument("--disable-dev-shm-usage")

		return chrome_options



	@property
	def source(self):
		return self.driver.page_source

	@property
	def timeout(self):
		"""Get the current timeout."""
		return self._timeout

	@timeout.setter
	def timeout(self, value):
		self.timeout_check(value)
		self._timeout = value

	def timeout_check(self, value):
		if not isinstance(value, int) or value < 0:
			raise ValueError("timeout must be a positive integer")


	from ._commands import (
		find,
		try_command,
		command_wait,
		command_click,
		command_sendkeys,
		command_get,
		command_dump,
		command_dumpxpath,
		command_try_wait,
		command_try_click,
		command_try_sendkeys
		)
