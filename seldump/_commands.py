# Wrapper object around selenium webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def find(self, xpath: str) -> list :
    return self.driver.find_elements(By.XPATH, xpath)

def try_command(self, func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except self.element_exceptions as e:
        return False

def command_wait(self, xpath: str, timeout: int) -> None:
    _timeout = self.timeout
    if timeout is not None:
        self.timeout_check(timeout)
        _timeout = timeout

    element = WebDriverWait(self.driver, _timeout).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )
    return True

def command_click(self, xpath: str, timeout: int) -> None:
    _timeout = self.timeout
    if timeout is not None:
        self.timeout_check(timeout)
        _timeout = timeout

    element = WebDriverWait(self.driver, _timeout).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )
    element.click()
    return True

def command_sendkeys(self, text: str, xpath: str, timeout: int) -> None:
    _timeout = self.timeout
    if timeout is not None:
        self.timeout_check(timeout)
        _timeout = timeout

    element = WebDriverWait(self.driver, _timeout).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )
    element.send_keys(text)
    return True

def command_get(self, url: str) -> None:
    self.driver.get(url)

def command_dump(self) -> None:
    print(self.source)

def command_dumpxpath(self, xpath):
    elements = self.find(xpath)
    for element in elements:
        print(element.get_attribute('outerHTML'))


# try commands
def command_try_wait(self, xpath: str, timeout: int) -> bool:
    return self.try_command(self.command_wait, xpath, timeout)

def command_try_click(self, xpath: str, timeout: int) -> bool:
    return self.try_command(self.command_click, xpath, timeout)

def command_try_sendkeys(self, text: str, xpath: str, timeout: int) -> bool:
    return self.try_command(self.command_sendkeys, text, xpath, timeout)

