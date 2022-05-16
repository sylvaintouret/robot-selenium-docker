*** Settings ***
# Import Selenium but remove run_on_failure (Screenshots are useless in headless)
Library           SeleniumLibrary     run_on_failure=Nothing    timeout=10    implicit_wait=10
Library           Screenshot
# Our little library (set the option  headless tp true)
Library           ChromeHeadless.py     headless=True

Suite Teardown    Close Browser


*** Keywords ***
# This is our magic keyword to set up chrome using our library
Open Chrome
    [Arguments]     ${url}

    # Call our library to setup the options
    ${options} =    get chrome options      
    
    # Call the Selenium Open browser but add our custom config
    Open Browser    ${url}    browser=chrome    desired_capabilities=${options}

    # Setting the window size is important for the test to run correctly
    Set Window Size     1920    1080


*** Test Cases ***
# Our modest test case
Visit Delia
    Open Chrome     https://www.openstreetmap.org/
    set chrome geolocation      https://www.openstreetmap.org/   47.2118156     -1.5514692

    # Let's click on the geolocate button, and then download the picture of the current location (this is to wait for page to load)
    Click Element       //span[@class='icon geolocate']
    Click Element       //span[@class='icon share']
    Click Element       //input[@value="Télécharger"]
    Take Screenshot     screenshot_location
