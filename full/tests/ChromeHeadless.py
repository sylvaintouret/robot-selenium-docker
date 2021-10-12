# robot framework stuff
from robot.api.deco import keyword, library
from robot.api import logger

# selenieum
from selenium import webdriver
from robot.libraries.BuiltIn import BuiltIn
import os

@library(scope='SUITE', version='0.0', auto_keywords=False, doc_format="TEXT")
class ChromeHeadless:
    """
        This is a library to manage chrome configuration to be able to run either locally (with browser opening) or headless (inside docker)

        Headless Chrome is needed when running on docker.
        
    """
    def __init__(self, headless : bool):
        self.headless = headless

    @keyword('get chrome options')
    def chrome_config(self, download_dir : str = None):
        """
        This functions defines the capabilities depending if chrome is headless or not

        > Example: By not setting the download folder
        ```robot
        *** Keywords ***
        Open Chrome
            [Arguments]     ${url}
            ${options} =    get chrome options
            Open Browser    ${url}    browser=chrome    desired_capabilities=${options}
            Set Window Size     1920    1080
        ```

        > Example: By setting the download folder to ./download
        ```robot
        *** Keywords ***
        Open Chrome
            [Arguments]     ${url}
            ${options} =    get chrome options  download_dir=./download
            Open Browser    ${url}    browser=chrome    desired_capabilities=${options}
            Set Window Size     1920    1080
        ```
            
        """

        options = webdriver.ChromeOptions()
        
        # define download directory if specified
        if download_dir:
            
            if not os.path.exists(download_dir):
                os.makedirs(download_dir)
            # IMPORTANT - ENDING SLASH V IMPORTANT
            logger.info(f"Setting Chrome Download dir to : {download_dir}")
            prefs = {
                    "profile.default_content_settings.popups": 0,
                    "download.default_directory": f"{download_dir}", 
                    "directory_upgrade": True
                }

            options.add_experimental_option("prefs", prefs)

        if not self.headless:
            return options.to_capabilities() 
        
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
        selib.driver.execute_cdp_cmd(
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
        selib.driver.execute_cdp_cmd("Emulation.setGeolocationOverride", params)
    
