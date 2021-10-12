# robot framework stuff
from robot.api.deco import keyword, library
from robot.api import logger
from selenium import webdriver
from robot.libraries.BuiltIn import BuiltIn

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

    @keyword('set chrome geolocation')
    def chrome_geolocation(
        self, 
        url : str, 
        latitude : float = 47.218371, 
        longitude : float = -1.553621, 
        accuracy : int = 100):
        
        """
        This functions grant the permission to use GPS location and sets the position based on input latitude and longitude
        """

        selib = BuiltIn().get_library_instance('SeleniumLibrary')
        webdriver = selib.driver
        webdriver.execute_cdp_cmd(
            "Browser.grantPermissions",
                {
                    "origin": url,
                    "permissions": ["geolocation"]
                },
        )

        params = {
            "latitude": latitude,
            "longitude": longitude,
            "accuracy": accuracy
        }
        logger.info(f"Setting Chrome Gelocation to  : {params}")
        webdriver.execute_cdp_cmd("Emulation.setGeolocationOverride", params)