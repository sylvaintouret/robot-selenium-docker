# robot framework stuff
from robot.api.deco import keyword, library
from robot.api import logger
from selenium import webdriver

@library(scope='SUITE', version='0.0', auto_keywords=False, doc_format="TEXT")
class ChromeHeadless:
    """
        This is a library to manage chrome configuration to be able to run either locally (with browser opening) or headless (inside docker)

        Headless Chrome is needed when running on docker.
        
    """
    def __init__(self, headless : bool):
        self.headless = headless
    
    @keyword('get chrome options')
    def chrome_config(self):

        options = webdriver.ChromeOptions()
        if not self.headless:
            return None
        
        options.add_argument("headless")
        options.add_argument("no-sandbox")
        options.add_argument("disable-gpu")
        options.add_argument("disable-dev-shm-usage")

        return options.to_capabilities()